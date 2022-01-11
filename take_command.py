import speech_recognition as sr

listener = sr.Recognizer()

def take_command(name, mode="manuel"):
	command = None
	if mode == "auto":
		try :
			with sr.Microphone() as source :
				print("Listening")
				voice = listener.listen(source)
				command = listener.recognize_google(voice, language = "fr-FR")
				command = command.lower()
				if name in command or "ok" in command :
					command = command.replace(name,"").replace("ok ", "")
					return command
				else :
					return None
		except:
			print("Erreur")
	elif mode == "manuel":
		command = input(">")
		return(command)