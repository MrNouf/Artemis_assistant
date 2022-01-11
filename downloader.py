import os
import youtube_dl
import pywhatkit
from talk import talk

music_path = "D:/music"

ydl_opts = {
    					#'outtmpl':music_path,
   						'format': 'bestaudio/best',
    					'postprocessors': [{
       					'key': 'FFmpegExtractAudio',
        				'preferredcodec': 'wav',
						'preferredquality': '192',}],}

def set_music_path(path):
	global music_path
	music_path = path

def get_music_path():
	global music_path
	return music_path

def get_video_title(lien):
	global ydl_opts
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info_dict = ydl.extract_info(lien, download=False)
		video_title = info_dict.get('title', None)
	return video_title


def dwl(lien):
	global ydl_opts
	global music_path
	video_title = get_video_title(lien)
	print(video_title)
	print(exist(video_title,music_path))
	if exist(video_title,music_path):
		talk("Le fichier existe déja voulez vous quand meme le telecharger ?")
		ans = input("Le fichier existe déja voulez vous quand meme le telecharger ? (Y/n)>")
		if ans.lower() == "y" :
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([lien.strip()])
		elif ans.lower() == "n":
			pass
	else :
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([lien.strip()])
	
def exist(name,path):
	print(path)
	for file in os.listdir(path) :
		if name in file :
			return True
	return False

def player(lien):
	path = get_music_path()
	video_title = get_video_title(lien)
	if exist(video_title, path):
		for f in (f for f in os.listdir(path) if video_title in f):
			file = f
		print(f'{path}/"{file}"')
		os.system("start "+path+'/"'+file+'"')
	else :
		song = pywhatkit.playonyt(lien,True)
