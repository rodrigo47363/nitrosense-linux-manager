import sys
import psutil
import os
import json
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                             QProgressBar, QTimer, QPushButton, QComboBox,
                             QLineEdit, QHBoxLayout, QMessageBox)

class NitroSenseLinux(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.profiles = load_profiles()
        self.current_profile = None
        self.load_profile_ui()
        
    def initUI(self):
        layout = QVBoxLayout()

        # CPU Widgets
        self.cpu_temp_label = QLabel("Temperatura CPU: N/A °C", self)
        layout.addWidget(self.cpu_temp_label)

        self.cpu_usage_label = QLabel("Uso CPU: N/A %", self)
        layout.addWidget(self.cpu_usage_label)

        self.cpu_usage_bar = QProgressBar(self)
        layout.addWidget(self.cpu_usage_bar)

        # GPU Widgets
        self.gpu_temp_label = QLabel("Temperatura GPU: N/A °C", self)
        layout.addWidget(self.gpu_temp_label)

        self.gpu_usage_label = QLabel("Uso GPU: N/A %", self)
        layout.addWidget(self.gpu_usage_label)

        self.gpu_usage_bar = QProgressBar(self)
        layout.addWidget(self.gpu_usage_bar)

        # Profile management
        profile_layout = QHBoxLayout()
        
        self.profile_selector = QComboBox(self)
        self.profile_selector.addItem("Seleccionar Perfil")
        profile_layout.addWidget(self.profile_selector)

        self.profile_name_input = QLineEdit(self)
        self.profile_name_input.setPlaceholderText("Nombre del perfil")
        profile_layout.addWidget(self.profile_name_input)

        self.save_profile_button = QPushButton("Guardar Perfil", self)
        profile_layout.addWidget(self.save_profile_button)
        self.save_profile_button.clicked.connect(self.save_current_profile)

        self.edit_profile_button = QPushButton("Editar Perfil", self)
        profile_layout.addWidget(self.edit_profile_button)
        self.edit_profile_button.clicked.connect(self.edit_profile)

        self.delete_profile_button = QPushButton("Eliminar Perfil", self)
        profile_layout.addWidget(self.delete_profile_button)
        self.delete_profile_button.clicked.connect(self.delete_profile)
        
        layout.addLayout(profile_layout)

        self.setLayout(layout)
        self.setWindowTitle('NitroSense Linux Avanzado')

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)

    def update_metrics(self):
        cpu_temp = self.get_cpu_temperature()
        cpu_usage = self.get_cpu_usage()

        gpu_temp = self.get_gpu_temperature()
        gpu_usage = self.get_gpu_usage()

        self.cpu_temp_label.setText(f"Temperatura CPU: {cpu_temp} °C")
        self.cpu_usage_label.setText(f"Uso CPU: {cpu_usage} %")
        self.cpu_usage_bar.setValue(cpu_usage)

        self.gpu_temp_label.setText(f"Temperatura GPU: {gpu_temp} °C")
        self.gpu_usage_label.setText(f"Uso GPU: {gpu_usage} %")
        self.gpu_usage_bar.setValue(gpu_usage)
    
    def load_profile_ui(self):
        self.profile_selector.clear()
        self.profile_selector.addItem("Seleccionar Perfil")
        for profile in self.profiles:
            self.profile_selector.addItem(profile["name"])
        self.profile_selector.currentIndexChanged.connect(self.load_profile)
    
    def save_current_profile(self):
        profile_name = self.profile_name_input.text()
        if not profile_name:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un nombre para el perfil.")
            return

        profile = {
            "name": profile_name,
            "cpu_fan_speed": "auto",  # Placeholder, add logic to get these values
            "gpu_fan_speed": "auto",
            "power_mode": "balanced"
        }
        save_profile(profile)
        self.profiles.append(profile)
        self.load_profile_ui()
        QMessageBox.information(self, "Perfil Guardado", f"Perfil '{profile_name}' guardado exitosamente.")

    def load_profile(self):
        selected_profile_name = self.profile_selector.currentText()
        if selected_profile_name == "Seleccionar Perfil":
            return
        
        for profile in self.profiles:
            if profile["name"] == selected_profile_name:
                self.current_profile = profile
                self.apply_profile(profile)
                break
    
    def apply_profile(self, profile):
        # Logic to apply the profile
        # Apply CPU fan speed
        if profile["cpu_fan_speed"] == "auto":
            self.set_fan_speed("cpu", "auto")
        else:
            self.set_fan_speed("cpu", profile["cpu_fan_speed"])

        # Apply GPU fan speed
        if profile["gpu_fan_speed"] == "auto":
            self.set_fan_speed("gpu", "auto")
        else:
            self.set_fan_speed("gpu", profile["gpu_fan_speed"])

        # Apply power mode
        self.set_power_mode(profile["power_mode"])
        
        QMessageBox.information(self, "Perfil Aplicado", f"Perfil '{profile['name']}' aplicado exitosamente.")

    def edit_profile(self):
        selected_profile_name = self.profile_selector.currentText()
        if selected_profile_name == "Seleccionar Perfil":
            QMessageBox.warning(self, "Error", "Seleccione un perfil para editar.")
            return

        for profile in self.profiles:
            if profile["name"] == selected_profile_name:
                profile["cpu_fan_speed"] = "manual"  # Placeholder, add logic to edit these values
                profile["gpu_fan_speed"] = "manual"
                profile["power_mode"] = "high_performance"
                save_profiles(self.profiles)
                QMessageBox.information(self, "Perfil Editado", f"Perfil '{profile['name']}' editado exitosamente.")
                break
    
    def delete_profile(self):
        selected_profile_name = self.profile_selector.currentText()
        if selected_profile_name == "Seleccionar Perfil":
            QMessageBox.warning(self, "Error", "Seleccione un perfil para eliminar.")
            return

        self.profiles = [profile for profile in self.profiles if profile["name"] != selected_profile_name]
        save_profiles(self.profiles)
        self.load_profile_ui()
        QMessageBox.information(self, "Perfil Eliminado", f"Perfil '{selected_profile_name}' eliminado exitosamente.")

    def get_cpu_temperature(self):
        try:
            temp_file = "/sys/class/thermal/thermal_zone0/temp"
            if os.path.isfile(temp_file):
                with open(temp_file, 'r') as f:
                    temp = f.read()
                return float(temp) / 1000
        except Exception as e:
            print(f"Error al obtener la temperatura de la CPU: {e}")
        return None

    def get_cpu_usage(self):
        try:
            return psutil.cpu_percent(interval=1)
        except Exception as e:
            print(f"Error al obtener el uso de la CPU: {e}")
        return None

    def get_gpu_usage(self):
        try:
            result = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE)
            gpu_usage = int(result.stdout.decode('utf-8').strip())
            return gpu_usage
        except Exception as e:
            print(f"Error al obtener el uso de la GPU: {e}")
        return None

    def get_gpu_temperature(self):
        try:
            result = subprocess.run(['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE)
            gpu_temp = int(result.stdout.decode('utf-8').strip())
            return gpu_temp
        except Exception as e:
            print(f"Error al obtener la temperatura de la GPU: {e}")
        return None

    def set_fan_speed(self, component, speed):
        # Placeholder function for setting fan speed
        print(f"Setting {component} fan speed to {speed}")
        # Actual implementation will depend on the hardware and system configuration
        # Here you could use tools like 'fancontrol' or write to specific sysfs files

    def set_power_mode(self, mode):
        # Placeholder function for setting power mode
        print(f"Setting power mode to {mode}")
        # Actual implementation will depend on the system configuration
        # You might use tools like 'tlp' or adjust settings via sysfs or ACPI

def save_profile(profile, filename="profiles.json"):
    try:
        with open(filename, 'r') as file:
            profiles = json.load(file)
    except FileNotFoundError:
        profiles = []

    profiles.append(profile)
    
    with open(filename, 'w') as file:
        json.dump(profiles, file, indent=4)

def load_profiles(filename="profiles.json"):
    try:
        with open(filename, 'r') as file:
            profiles = json.load(file)
        return profiles
    except FileNotFoundError:
        return []

def save_profiles(profiles, filename="profiles.json"):
    with open(filename, 'w') as file:
        json.dump(profiles, file, indent=4)

def main():
    app = QApplication(sys.argv)
    ex = NitroSenseLinux()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
