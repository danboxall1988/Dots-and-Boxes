import pygame as pg
import sys
import os

SCREEN_SIZE = (550, 600)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
TC = 50	# coords of top corner of screen (50,50)

LINE_THICKNESS, LINE_LENGTH = 8, 50
RADIUS = 8

BG_COLOR = '#e0d1a6'
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
L_RED = (255,200,200)
BLUE = (0,0,255)
L_BLUE = (220,220,255)
PURPLE = (155, 45, 205)

COLORS = [RED, BLUE]
L_COLORS = [L_RED, L_BLUE]

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
player1.color = RED
player2.color = BLUE
player1.name = "Player1"
player2.name = "Player2"
