""" This file is filled with constants and objects and the player class,
	all of which are used across the entire program. Every file imports this.
"""

import pygame as pg
import sys
import os

pg.init()
pg.font.init()
os.environ["SDL_VIDEO_CENTERED"] = "1" 

SCREEN_SIZE = (550, 600)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
TC = 50	# coords of top corner of screen (50,50)

LINE_THICKNESS, LINE_LENGTH = 8, 50
RADIUS = 8

BG_COLOR = '#e0d1a6'
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (120, 125, 140)

RED = (255,0,0)
L_RED = (255,160,200)
ORANGE = (250,70,5)
L_ORANGE = (230, 135, 100)
YELLOW = (255,250,10)
L_YELLOW = (230,225,100)
GREEN = (0,255,0)
L_GREEN = (180,255,180)
BLUE = (0,0,255)
L_BLUE = (160,200,255)
PURPLE = (155, 45, 205)
L_PURPLE = (190,135,220)

COLORS = [RED, ORANGE, YELLOW, GREEN, PURPLE, BLUE]
L_COLORS = [L_RED, L_ORANGE, L_YELLOW, L_GREEN, L_PURPLE, L_BLUE]

class Player:
	def __init__(self):
		self._name = ""
		self._color = None
		self._l_color = None
		self._points = 0
		
	@property
	def name(self):
		return self._name
		
	@name.setter
	def name(self, string):
		self._name = string
		
	@property
	def color(self):
		return self._color
		
	@color.setter
	def color(self, clr):
		self._color = clr
		self._l_color = L_COLORS[COLORS.index(self._color)]
		
	@property
	def l_color(self):
		return self._l_color
		
	@property
	def points(self):
		return self._points
		
	def update_points(self, n):
		self._points += n
	
	def reset_points(self):
		self._points = 0
		
player1 = Player()
player2 = Player()
# Below are default names, should the player not enter a name
player1.name = "Player1"
player2.name = "Player2"
