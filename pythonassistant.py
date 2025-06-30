
# importamos la dependencia  y le asignamos un alias
import speech_recognition as sr
import pyttsx3
import io 

# funcion para que la máquina escuche lo que decimos y lo convierta a texto
def audio_pc():
    #definimos el reconocedor de voz dandole un alias y creamos un objeto reconocedor
    r = sr.Recognizer()
    #usamos el microfono como fuente de audio
    with sr.Microphone() as source:
        r.pause_threshold = 0.5 #tiempo de espera para que el usuario hable (ideal entre 0.5 y 0.8)
        print("Escuchando...") #mensaje para saber que podemos empezar a hablar
        audio = r.listen(source) #escucha el audio del micrófono
        print("Reconociendo...") #mensaje para saber que se está procesando el audio
        try:
            text = r.recognize_google(audio, Language='es-ES') #reconoce el audio y lo convierte a texto
            print("Has dicho: " + text)
            return text #retorna el texto reconocido
        except:
            print("Lo siento, no he podido entenderte.")

# audio_pc() 

#Funcion para que la máquina hable lo que hayamos escrito
def respuesta_pc(texto):
    try:
        engine = pyttsx3.init()  # Inicializa el motor de texto a voz
        engine.setProperty('rate', 150)  # Ajusta la velocidad de la voz (150 es un valor común)
        engine.setProperty('volume', 1)  # Ajusta el volumen (0.0 a 1.0)
        engine.say(texto) #Convierte el texto a voz
        engine.runAndWait()  # Espera a que termine de hablar
    except:
        print("Lo siento, no he podido hablar.")

respuesta_pc("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")  # Prueba de la función de respuesta