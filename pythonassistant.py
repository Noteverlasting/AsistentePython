
# importamos la dependencia  y le asignamos un alias
import speech_recognition as sr
import pyttsx3
import io 
import datetime
import pyjokes  # Para chistes
import pywhatkit  # Para enviar mensajes de WhatsApp
import webbrowser  # Para abrir páginas web

nombre_asi = "La asombrosa Petunia María, prima lejana de Pepa Pig"

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
            text = r.recognize_google(audio, language='es-ES') #reconoce el audio y lo convierte a texto
            print("Has dicho: " + text)
            return text #retorna el texto reconocido
        except:
            print("Lo siento, no he podido entenderte.")

# audio_pc() 

#Funcion para que la máquina hable lo que hayamos escrito
def respuesta_pc(texto):
    try:
        engine = pyttsx3.init()  # Inicializa el motor de texto a voz
        engine.setProperty('rate', 200)  # Ajusta la velocidad de la voz (150 es un valor común)
        engine.setProperty('volume', 1)  # Ajusta el volumen (0.0 a 1.0)
        engine.say(texto) #Convierte el texto a voz
        engine.runAndWait()  # Espera a que termine de hablar
    except:
        print("Lo siento, no he podido hablar.")

# respuesta_pc("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")  # Prueba de la función de respuesta

#FUNCIONES EXTRA

def dia_semana():
    #Obtenemos el dia de la semana
    dia = datetime.date.today()
    # print(dia.weekday()) #Imprime el número del día de la semana (0=lunes, 6=domingo)

    nombres_dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    respuesta_pc(f"Hoy es {nombres_dias[dia.weekday()]}")  # Responde con el nombre del día de la semana

# dia_semana()

def hora_actual():
    #Variable para almacenar la hora actual
    hora = datetime.datetime.now()
    mensajehora = f"Son las {hora.hour} horas, {hora.minute} minutos y {hora.second} segundos"
    respuesta_pc(mensajehora)


# hora_actual()

def saludo():
    hora = datetime.datetime.now()
    if 6 <= hora.hour < 14:
        ahora ="Buenos días"
    elif 14 <= hora.hour < 20:
        ahora ="Buenas tardes"
    else:
        ahora ="Buenas noches"

    respuesta = f"{ahora}, soy {nombre_asi}, tu asistente virtual. ¿En qué puedo ayudarte, puerqui?"
    respuesta_pc(respuesta)

# saludo()

def centro_de_peticiones():
    saludo()
    #bucle infinito hasta que la detengamos para que escuche
    
    while True:
        try:
            respuesta_pc("Estoy escuchando, puerqui. ¿Qué quieres que haga por ti?")  # Mensaje inicial
            peticion = audio_pc()
            print(f"Petición recibida: {peticion}")
            #Preparamos las peticiones que procesará el asistente
            if "dime la hora" in peticion:
                hora_actual()
                continue
            elif "qué día es hoy" in peticion:
                dia_semana()
                continue
            elif "eso es todo" in peticion or "fin del programa" in peticion:
                respuesta_pc("Hasta luego, puerqui")
                break
            elif "cuéntame un chiste" in peticion:
                respuesta_pc(pyjokes.get_joke(language='es', category='all'))
                continue
            elif "reproduce" in peticion:
                respuesta_pc("A tus ordenes puerquita")
                pywhatkit.playonyt(peticion)
                continue

        except:
            respuesta_pc("Lo siento, no he podido entenderte. Por favor, inténtalo de nuevo.")


centro_de_peticiones()