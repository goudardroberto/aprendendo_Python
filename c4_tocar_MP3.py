"""Programa em Python que abre e reproduz o áudio de um arquivo MP3."""
from pygame import mixer

mixer.init()
mixer.music.load('ex.mp3')
mixer.music.play()
x = input('Digite algo para parar a música...')
