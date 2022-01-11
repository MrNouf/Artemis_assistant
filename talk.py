import pyttsx3
import sys

engine = pyttsx3.init()
voices = engine.getProperty("voices")
arg = sys.argv[1::]

def talk(text=arg):
	engine.say(text)
	engine.runAndWait()

talk()