import pyttsx3 as ps
import datetime 
import wikipedia 
import speech_recognition as sr
engine=ps.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def timeGet():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
def listenCmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print('Processing....')
            query=r.recognize_google(audio,language='en-in')
        except Exception as e:
            print(e)
            print("not get")
            query=""
    return query
if __name__ == "__main__":
    # speak("hello")
    # timeGet()
    while(True):
        q=listenCmd().lower()
        if "search" in q:
            q = q.replace("search","")
            result=wikipedia.summary(q,sentences=2)
            print(result)
            speak(result)
        elif "time" in q:
            timeGet()
        elif "off" in q:
            break




