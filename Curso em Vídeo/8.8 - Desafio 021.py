#Reproduzir um arquivo mp3

"""
import vlc
p = vlc.MediaPlayer("file:///path/to/track.mp3")
p.play()
"""
'''
musicPath = 'C:/Users/andre/Desktop/Curso de Python/Curso em Vídeo/music/file.mp3'

#Por OS
import os
os.startfile(musicPath)

#Por Webbrowser
import webbrowser
webbrowser.open(musicPath)

#por pyglet
#import pyglet
#song = pyglet.media.load(musicPath)
#song.play()
#pyglet.app.run()
'''



#import pygame
from pygame import mixer, event
mixer.init()
mixer.music.load('file2.mp3')
mixer.music.play()

input("Pressione qualquer tecla para parar.")



