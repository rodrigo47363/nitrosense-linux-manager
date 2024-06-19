# NitroSense Linux Manager

NitroSense Linux Manager is a Python application built with PyQt5, designed to manage performance profiles and monitor CPU and GPU usage on Linux systems, focusing particularly on Nvidia graphics cards.

## Features

- **Hardware Monitoring:**
  - CPU temperature and usage
  - GPU temperature and usage using `nvidia-smi`
  
- **Profile Management:**
  - Create, edit, and delete custom performance profiles
  - Automatic or manual fan speed adjustment for CPU and GPU
  
- **Graphical User Interface (GUI):**
  - Utilizes PyQt5 for an intuitive and user-friendly interface
  - Real-time performance metrics display

## Installation and Usage

### Requirements

To use NitroSense Linux Manager, make sure you have the following installed:

- Python 3.x
- PyQt5
- psutil
- Access to system commands (`nvidia-smi` for GPU monitoring)

### Installing Dependencies

You can install the necessary dependencies using the following commands:

```bash
sudo apt update
sudo apt install python3-pyqt5 psutil nvidia-smi
```

### Cloning the Repository

You can clone this repository by running the following command in your terminal:

```bash
git clone https://github.com/rodrigo47363/nitrosense-linux-manager.git
```

### Running NitroSense

Once dependencies are installed and the repository is cloned, you can run NitroSense Linux Manager with the following command:

```bash
python3 nitrosense.py
```

This will open the graphical user interface where you can manage performance profiles and monitor hardware.

## Contributing

Contributions are welcome! If you find any issues or have enhancements in mind, please open an issue or submit a pull request.

## Author

Developed by [rodrigo47363](https://github.com/rodrigo47363/).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

# Gestor NitroSense para Linux

NitroSense Linux Manager es una aplicación en Python desarrollada con PyQt5, diseñada para gestionar perfiles de rendimiento y monitorizar el uso de CPU y GPU en sistemas Linux, con un enfoque particular en tarjetas gráficas Nvidia.

## Características

- **Monitorización de Hardware:**
  - Temperatura y uso de CPU
  - Temperatura y uso de GPU utilizando `nvidia-smi`
  
- **Gestión de Perfiles:**
  - Crear, editar y eliminar perfiles personalizados de rendimiento
  - Ajuste automático o manual de la velocidad del ventilador para CPU y GPU
  
- **Interfaz Gráfica de Usuario (GUI):**
  - Utiliza PyQt5 para una interfaz intuitiva y fácil de usar
  - Visualización en tiempo real de métricas de rendimiento

## Instalación y Uso

### Requisitos

Para utilizar NitroSense Linux Manager, asegúrate de tener instalado lo siguiente:

- Python 3.x
- PyQt5
- psutil
- Acceso a comandos del sistema (`nvidia-smi` para monitorización de GPU)

### Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta los siguientes comandos en tu terminal:

```bash
sudo apt update
sudo apt install python3-pyqt5 psutil nvidia-smi
```

### Clonación del Repositorio

Puedes clonar este repositorio ejecutando el siguiente comando en tu terminal:

```bash
git clone https://github.com/rodrigo47363/nitrosense-linux-manager.git
```

### Ejecución de NitroSense

Una vez instaladas las dependencias y clonado el repositorio, puedes ejecutar NitroSense Linux Manager con el siguiente comando:

```bash
python3 nitrosense.py
```

Esto abrirá la interfaz gráfica de usuario donde podrás gestionar perfiles de rendimiento y monitorizar el hardware.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes mejoras en mente, por favor, abre un problema o envía una solicitud de extracción.

## Autor

Desarrollado por [rodrigo47363](https://github.com/rodrigo47363/).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
```
