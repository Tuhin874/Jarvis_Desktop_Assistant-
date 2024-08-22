
import pyttsx3
import eel
import time
import speech_recognition as sr
import pywhatkit as kit





engine = pyttsx3.init() 
voices = engine.getProperty('voices')         #taking voices
# print(voices)                              
# print(voices[0].id)                              
engine.setProperty('voice', voices[1].id)     #taking voices(0 asnd 1) change it to change the voice
engine.setProperty('rate',174) #To slow down(0 - 100) and fast the voice speed(100 - 200)


@eel.expose
def speak(audio):
    audio = str(audio)
    # print(f"Speaking: {audio}")  # Debugging line
    eel.DisplayMessage(audio)
    engine.say(audio)                              #speak function
    eel.receiverText(audio)
    engine.setProperty('volume' , 1.0)
    engine.runAndWait()


@eel.expose
def speakwithout(audio):
    engine.say(audio)                               #speak function
    eel.receiverText(audio)
    engine.setProperty('volume' , 1.0)
    engine.runAndWait()  


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(0.4)
       
    except Exception as e:
        return ""
    
    return query.lower()





@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        if "open youtube" in query:
            speak("Sure sir....")
            speak("What do you want to search on youtube?")
            tt = takecommand().lower()
            if tt!="":
                speak("Wait sir i am searching....")
                kit.playonyt(f"{tt}")
                time.sleep(2)
            else:
                speak("I'm sorry, I didn't catch that.")
        elif "open" in query:
            from Engine.features import openCommand
            openCommand(query)
        elif "close" in query:
            from Engine.features import closeCommand
            closeCommand(query)
        elif "youtube" in query:
            from Engine.features import playYoutube
            playYoutube(query)
        elif "search" in query:
            from Engine.features import search
            search(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from Engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                    
                whatsApp(contact_no, query, message, name)
        else:
            from Engine.features import chatBot
            chatBot(query)
    except:
        print("Some error occurred")
    
    eel.ShowHood()