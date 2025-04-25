# Importa la librería para reconocimiento de voz
import speech_recognition as sr
# Importa la librería para convertir texto a voz
from gtts import gTTS
# Importa la función para reproducir sonidos
import playsound
# Importa funciones del sistema operativo (para manipular rutas y archivos)
import os

# Función para convertir un mensaje de texto en voz y reproducirlo
def speak(message):
    tts = gTTS(text=message, lang="es", slow=False)  # Convierte texto a voz en español
    filename = os.path.dirname(__file__) + "\\voice.mp3"  # Define la ruta del archivo de audio temporal
    tts.save(filename)  # Guarda el archivo de audio
    playsound.playsound(filename)  # Reproduce el audio
    os.remove(filename)  # Elimina el archivo una vez reproducido

# Función para escuchar mediante el micrófono y convertir el audio a texto
def listen():
    r = sr.Recognizer()  # Crea un reconocedor de voz
    with sr.Microphone() as source:  # Usa el micrófono como fuente de audio
        r.adjust_for_ambient_noise(source)  # Ajusta el reconocimiento al ruido ambiental
        
        print("Listening ...")  # Imprime un mensaje en consola
        beep()  # Reproduce un sonido de "beep" antes de escuchar
    
        audio = r.listen(source)  # Escucha el audio del micrófono
        said = ""  # Inicializa la variable que contendrá el texto

        try:
            # Intenta reconocer el audio usando la API de Google
            said = r.recognize_google(audio, language='es-ES')
        except Exception as e:
            print("Exception: " + str(e))  # Imprime la excepción si ocurre un error

    return said  # Retorna el texto reconocido

# Función que reproduce un sonido "beep" desde un archivo de audio
def beep():
    filename = os.path.dirname(__file__) + "\\sounds\\beep.mp3"  # Ruta del sonido "beep"
    playsound.playsound(filename)  # Reproduce el sonido

# Función que deletrea un texto, separando y poniendo en mayúscula cada carácter
def spell_out(text):
    spelled = ', '.join(char.upper() for char in text)  # Convierte cada carácter en mayúscula y los separa por coma
    return spelled  # Retorna el texto deletreado

# Función que convierte texto en números (solo los tres primeros casos están implementados)
def text_to_number(text):
    if text.startswith("uno") or text.startswith("un"):  # Si empieza con "uno" o "un"
        return 1
    if text.startswith("dos"):
        return 2
    if text.startswith("tres"):
        return 3
