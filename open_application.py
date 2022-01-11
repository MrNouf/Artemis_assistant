import os
import talk

def open_application(app):
	if "chrome" in app:
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
		return

	elif "firefox" in app or "mozilla" in app:
		os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
		return

	elif "minecraft" in app:
		os.startfile(os.path.expanduser('~')+"curseforge/minecraft/Install/minecraft.exe")
		return

	elif "lol" in app or "league of legend" in app:
		os.startfile("C:/Riot Games/League of Legends/LeagueClient.exe")
		return

	elif "osu" in app :
		os.startfile(os.path.expanduser('~')+"/AppData/Local/osu!/osu!.exe")
		return

	elif "office" in app :
		os.startfile("C:/Program Files/LibreOffice/program/soffice.exe")

	else:

		talk.talk("Je ne trouve rien de ce nom")
		return
