import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def talk_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'joachim' in command:
                command = command.replace('joachim', '')
                print(command)
    except:
        pass
    return command


def run_joachim():
    command = talk_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M: %p')
        print(time)
        talk('Current time is ' + time)
    elif 'Who is' in command:
        person = command.replace('Who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'Are you single' in command:
        talk('I am in a relationship with the Internet')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'What is' in command:
        person1 = command.replace('What is', '')
        info1 = wikipedia.summary(person1, 1)
        print(info1)
        talk(info1)       
    else:
        talk('Please come again')


while True:
    run_joachim()
