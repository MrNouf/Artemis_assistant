import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes
import scanner
import downloader
import os
import take_command
import subprocess
from open_application import open_application
from talk import talk

listener = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
engine = pyttsx3.init()
voices = engine.getProperty("voices")
wikipedia.set_lang("fr")
stop = False
mode = "manuel"
say = None

def Run():
	global mode
	global say
	command = take_command.take_command("artemis",mode)
	print(command)
	try:
		if command == None:
			pass
		elif 'joue' in command :
			song = command.replace("joue", "")
			print('playing')
			talk("je mets" + song)
			lien = pywhatkit.playonyt(song, False, False)
			try :
				downloader.player(lien)
			except youtube_dl.utils.DownloadError :
				print("Une erreur est survenue")

		elif 'heure' in command :
			heure = datetime.datetime.now().strftime('%H')
			minute = datetime.datetime.now().strftime('%M')
			talk(f'Il est {heure} heure {minute}')
		elif 'qui est' in command :
			person = command.replace("qui est","")
			try : 
				info = wikipedia.summary(person, 5)
				say = subprocess.Popen(["py", "talk.py", info], shell=False) #demare le processus en arriere plan pour pouvoir l'arreter avec stop plus tard
				print(info)

			except wikipedia.exceptions.PageError :
				talk("je ne trouve rien sur cette personne")

			except wikipedia.exceptions.DisambiguationError :
				talk("Il y a trop de sujet different la dessus")

		elif "c'est quoi" in command :
			sujet = command.replace("c'est quoi","")
			try : 
				info = wikipedia.summary(sujet, 5)
				say = subprocess.Popen(["py", "talk.py", info], shell=False)
				print(info)
			except wikipedia.exceptions.PageError :
				talk("je ne trouve rien la dessus")
			except wikipedia.exceptions.DisambiguationError :
				talk("Il y a trop de sujet différent la dessus")
			
		elif 'blague' in command :
			talk(pyjokes.get_joke())
		
		elif "scanner" in command :
			scanner.Start()

		elif "telecharge " in command:
			video = command.replace("telecharge ", "")
			talk(f"je telecharge {video}")
			os.chdir(downloader.get_music_path())
			lien = pywhatkit.playonyt(video.strip(),False,False)
			downloader.dwl(lien)
			print(video)
		elif "lance" in command or "ouvre" in command :
			app = command.replace("lance","").replace("ouvre","")
			talk(f"Je lance {app}")
			open_application(app)
		elif "auto" in command or "automatique" in command :
			mode = "auto"

		elif "manuel" in command :
			mode = "manuel"

		elif "change le chemin" in command :
			talk("Saisissez le chemin")
			downloader.set_music_path(input("Entrez le chemin >"))

		elif "cherche" in command :
			sujet = command.replace("cherche","")
			pywhatkit.search(sujet)
		
		elif "arrete " in command or "stop" in command:
			if say.poll() is None :
				say.kill()

			else:
				talk("Au revoir")
				global stop
				stop = True

		else :
			talk("Je ne comprend pas")
			
	except ValueError:
		print("Une erreur est survenue")



if __name__ == '__main__':
	
	while stop != True :
		Run()