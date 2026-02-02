# Jarvis Python - Asistente Virtual

## Probar el Asistente (Sin instalación)

Si te gustaria probar a Jarvis sin configurar un entorno de Python, podes descargar el archivo ejecutable listo para usar desde la sección de **[Releases](https://github.com/fedepolito/jarvis-python/releases)**. Solo hay que descargar el archivo `.exe`, ejecutarlo y listo.

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
