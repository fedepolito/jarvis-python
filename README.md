# Jarvis Python - Asistente Virtual

Este proyecto es un asistente virtual desarrollado en Python que combina una interfaz gráfica con procesamiento de comandos por voz para automatizar la apertura de sitios web y aplicaciones.

## Funcionalidades principales

* **Reconocimiento de voz**: Utiliza la librería SpeechRecognition para procesar órdenes verbales.
* **Interfaz Gráfica**: Construida con Tkinter para ofrecer una experiencia de usuario visual.
* **Comandos configurables**: El sistema lee un archivo comandos.json para mapear palabras clave a URLs.

## Instalación y Configuración

Para ejecutar este asistente en tu máquina local, sigue estos pasos:

1. **Requisitos**: Tener instalado Python 3.10 o superior.
2. **Instalar dependencias**:
   ```bash
   pip install SpeechRecognition pyttsx3
