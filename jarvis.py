import tkinter as tk  # Importa tkinter para crear la interfaz gráfica
import pyttsx3  # Importa la librería para convertir texto a voz
import speech_recognition as sr  # Importa la librería para reconocimiento de voz
import webbrowser  # Importa la librería para abrir el navegador web
import json  # Importa la librería para trabajar con archivos JSON
import os  # Importa la librería para funciones del sistema operativo
import sys  # Importa la librería para interactuar con el sistema


if getattr(sys, 'frozen', False):  # Verifica si el programa está empaquetado como ejecutable
    carpeta_base = sys._MEIPASS  # Si es ejecutable, usa la carpeta temporal del empaquetado
else:
    carpeta_base = os.path.dirname(os.path.abspath(__file__))  # Si no, usa la carpeta del script

ruta_json = os.path.join(carpeta_base, "comandos.json")  # Construye la ruta completa al archivo JSON

# Cargar comandos desde JSON
try:
    with open(ruta_json, "r") as archivo:  # Intenta abrir el archivo JSON en modo lectura
        comandos = json.load(archivo)  # Carga el contenido del JSON en la variable 'comandos'
except FileNotFoundError:
    raise FileNotFoundError(f"No se encontró el archivo comandos.json en {ruta_json}")  # Error si no encuentra el archivo

# Inicializar voz y reconocedor
voz = pyttsx3.init()  # Inicializa el motor de texto a voz
reconocedor = sr.Recognizer()  # Crea un objeto para reconocimiento de voz

# Crear ventana Tkinter
ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Jarvis")  # Establece el título de la ventana
ventana.geometry("400x250")  # Define el tamaño de la ventana (ancho x alto)

# Label para mostrar mensajes
mensaje = tk.StringVar()  # Crea una variable especial de Tkinter para texto variable
mensaje.set("")  # Inicializa la variable con texto vacío
label = tk.Label(ventana, textvariable=mensaje, font=("Arial", 14))  # Crea una etiqueta con la variable de texto
label.pack(pady=20)  # Coloca la etiqueta en la ventana con espacio vertical

# Función para hablar y mostrar mensaje
def hablar(texto):
    mensaje.set(texto)       # Actualiza el texto en la interfaz gráfica
    voz.say(texto)           # Prepara el texto para ser convertido a voz
    voz.runAndWait()         # Reproduce el audio y espera a que termine

# Función para escuchar comando
def escuchar_comando():
    try:
        with sr.Microphone() as fuente:  # Abre el micrófono como fuente de audio
            hablar("Estoy escuchando...")  # Indica que está listo para escuchar
            audio = reconocedor.listen(fuente)  # Escucha el audio del micrófono
        
        comando = reconocedor.recognize_google(audio, language="es-AR")  # Convierte audio a texto usando Google
        hablar(f"Escuché: {comando}")  # Repite lo que entendió

        # Buscar comando en el JSON
        encontrado = False  # Bandera para saber si encontró el comando
        for clave, url in comandos.items():  # Recorre todos los comandos del JSON
            if clave in comando.lower():  # Si la palabra clave está en el comando
                hablar(f"Abriendo {clave.capitalize()}")  # Anuncia qué va a abrir
                webbrowser.open(url)  # Abre la URL en el navegador
                encontrado = True  # Marca que encontró el comando
                break  # Termina el bucle

        if not encontrado:  # Si no encontró el comando en el JSON
            hablar("Lo escuché, pero no tengo una orden para eso")  # Informa que no reconoce el comando

    except sr.UnknownValueError:  # Error cuando no puede entender el audio
        hablar("No entendí lo que dijiste")  # Informa el error
    except sr.RequestError:  # Error de conexión con el servicio de reconocimiento
        hablar("Hubo un problema con la conexión")  # Informa el error

# Botón para activar escucha
boton = tk.Button(ventana, text="Escuchar comando", command=escuchar_comando)  # Crea botón que ejecuta la función
boton.pack(pady=10)  # Coloca el botón en la ventana con espacio vertical

# Mensaje inicial al abrir la ventana
hablar("Hola, soy Jarvis")  # Saludo inicial al iniciar el programa

# Mantener la ventana abierta
ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica