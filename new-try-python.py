#new try python 
# reco vocal 
 
import sys 
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import random
import wikipedia
import source

listener = sr.Recongnizer()
engine = pyttsx3.intit()
engine.setPrperty("voice", "french")
engine.setProperty("rate", 170)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def greetme():
    current_hour = int(datetime.datetime.now().hour)
    if 0<= current_hour < 12:
        talk ("Bonjours TOI")
    if 12 <=current_hour < 18:
        talk("bon apres midi")
    else :
        talk ("bonsoir")

#set french voice
voices = engine.getProperty("voices")
engine.setProperty("voice",)


greetme()
engine.say("comment vas tu?")
engine.runAndWait

def alexa_command() -> str:

    wiht sr.Microphone() as source :
    print("listenning ....")
        listener.pause_treshold = 5
        voice = listener.listen(source)
        command = listener.recongnize_google(voice, language="fr-FR")
        command= command.lower()
        print(command)
        if "alexa" in command:
            comande = command.replace("alexa","")
            print(command)
    return command
command = ""
def run_alexa():
    alexa_command = alexa_command()
    if "musique" in command :
        song = command.replace("musique","")
        talk("musique en cours ...")
        pywhatkit.playonyt(song)
    elif "heure" in command :
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("il est actumement"+ time)
    elif "qui est" in command :
        person = command.replace("qui est ","")
        wikipedia.set.lang("fr")
        info = wikipedia.summary(person, 1)
    elif "sortir" in command :
        talk("DESOLER non")
    elif "desactive toi " in command :
        talk("Merci de m'avoir utiliser ")
        sys.exit()
    else :
        talk("pls repete")



if __name__ == '__main__':
    while True :
        run_alexa()
