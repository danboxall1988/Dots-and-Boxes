import pygame as pg
from common import *

class Board:
	""" Takes care of the visual element of the game """
	def __init__(self):
		# these are the lines that have already been selected
		self.lines = [] 
		self.font = pg.font.SysFont("Comic Sans SF", 50)
		
	def draw_dots(self):
		""" Draws a 10x10 grid of dots """
		for row in range(10):
			for col in range(10):
				pg.draw.circle(SCREEN, BLACK, (row * LINE_LENGTH + TC, \
					col * LINE_LENGTH + TC), RADIUS)
					
	def draw_lines(self):
		""" Draws all of the lines that have already been selected """
		for line in self.lines:
			pg.draw.rect(SCREEN, line[0], line[1].rect)
	
	def draw_scores(self):
		p1_string = f"{player1.name}: {player1.points}"
		p2_string = f"{player2.name}: {player2.points}"
		p1_surface = self.font.render(p1_string, True, player1.color)
		p2_surface = self.font.render(p2_string, True, player2.color)
		SCREEN.blit(p1_surface, (50, 520))
		SCREEN.blit(p2_surface, (50, 555))
				
	def draw(self):
		self.draw_lines()
		self.draw_dots()
		self.draw_scores()
		
	def update(self, line, color):
		self.lines.append((color, line))
		

class Highlight:
	""" This is used to highlight a single line when the mouse is
		hovering over it
	"""
	def __init__(self, w, h, x, y):
		#self.active is set to false when the line has been selected
		self._active = True 
		self.surface = pg.Surface((w, h))
		self._rect = self.surface.get_rect()
		self._rect.x = x
		self._rect.y = y
		self.width = w
		self.height = h
	
	@property
	def active(self):
		return self._active
		
	def deactivate(self):
		self._active = False
	
	@property
	def rect(self):
		return self._rect
			
	def draw(self, color):
		pg.draw.rect(SCREEN, color, self.rect)


class Game:
	""" Main game """
	def __init__(self):
		self.done = False
		self.board = Board()
		# True when the mouse is hovering over a line
		self.line_highlighted = False
		# This is the line the mouse is hovering over
		self.highlighted_line = None
		self.whose_turn = player1
		# A multidimensional list of all the possible horizontal 
		# lines. Set to zero until the line has been selected, then set to 1
		self.h_lines = []
		# Same as h_lines, but for verticals
		self.v_lines = []
		# Filled with instances of Highlight class, one for each
		# possible line
		self.highlights = []
		self.setup_highlights_and_line_grids()
		# Either 'h' or 'v', depending on whether line is vertical or horizontal
		self.horv = ''
		# Used to get the position of the selected line
		self.line_index = None
		self.total_boxes = 0
		self.clock = pg.time.Clock()
		
	def setup_highlights_and_line_grids(self):
		# horizontal highlights and h_lines
		for row in range(10):
			h_line_row = []
			for col in range(9):
				self.highlights.append(Highlight(LINE_LENGTH, LINE_THICKNESS, 
					col * LINE_LENGTH + TC, row * LINE_LENGTH + TC - RADIUS // 2))
				h_line_row.append(0)
			self.h_lines.append(h_line_row)
				
		# vertical highlights and v_lines
		for row in range(9):
			v_line_row = []
			for col in range(10):
				self.highlights.append(Highlight(LINE_THICKNESS, LINE_LENGTH,
					col * LINE_LENGTH + TC - RADIUS // 2, row * LINE_LENGTH + TC))
				v_line_row.append(0)
			self.v_lines.append(v_line_row)
					
		#print(self.h_lines)
	
	def check_for_highlights(self):
		""" Checks if the mouse is hovering over a line, and if it is
			highlights the line
		"""
		pos = pg.mouse.get_pos()
		for line in self.highlights:
			if line.rect.collidepoint(pos) and line.active:
				#print(line.rect.x, line.rect.y)
				line.draw(self.whose_turn.l_color)
				self.line_highlighted = True
				self.highlighted_line = line
				return
		self.line_highlighted = False
	
	def switch_player(self):
		if self.whose_turn == player1:
			self.whose_turn = player2
		else:
			self.whose_turn = player1
	
	def fill_line_grid(self):
		""" When a line has been selected, this method calculates the 
			line's array coordinates, and then sets the relevent index
			to 1
		"""
		pos = self.highlights.index(self.highlighted_line)
		# if the line clicked is a horizontal line
		if pos < 90:
			#print(pos // 9, pos % 9)
			self.horv = 'h'
			self.h_lines[pos // 9][pos % 9] = 1
			#print(f"horizont: [{pos // 9}][{pos % 9}]")
		else:
			pos -= 90
			#print(pos // 10, pos % 10)
			self.horv = 'v'
			self.v_lines[pos // 10][pos % 10] = 1
			#print(f"vertical: [{pos // 10}][{pos % 10}]")
		self.line_index = pos
	
	def check_for_boxes(self):
		""" After a line is selected, checks for completed boxes """
		box_count = 0
		# if horizontal line selected
		if self.horv == 'h':
			# get the coords
			row, col = self.line_index // 9, self.line_index % 9
			# check for complete boxes above if possible
			if row >= 1:
				if self.h_lines[row - 1][col] and self.v_lines[row - 1][col] \
					and self.v_lines[row - 1][col + 1]:
						box_count += 1
			# check for boxes below if possible
			if row <= 8:
				if self.h_lines[row + 1][col] and self.v_lines[row][col] \
					and self.v_lines[row][col + 1]:
						box_count += 1
		# if vertical line selected
		elif self.horv == 'v':
			row, col = self.line_index // 10, self.line_index % 10
			# check for boxes to left if possible
			if col >= 1:
				if self.v_lines[row][col - 1] and self.h_lines[row][col - 1] \
					and self.h_lines[row + 1][col - 1]:
						box_count += 1
			# check for boxes to right if possible
			if col <= 8:
				if self.v_lines[row][col + 1] and self.h_lines[row][col] \
					and self.h_lines[row + 1][col]:
						box_count += 1
		return box_count
				
	def event_loop(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN and self.line_highlighted:
				self.total_boxes = 81 # send straight to exit screen
				self.board.update(self.highlighted_line, self.whose_turn.color)
				self.highlighted_line.deactivate()
				self.fill_line_grid()
				boxes = self.check_for_boxes()
				self.whose_turn.update_points(boxes)
				self.total_boxes += boxes
				#print(self.total_boxes)
				self.switch_player()
				
	def main_loop(self):
		while self.total_boxes < 81:
			self.event_loop()
			SCREEN.fill(BG_COLOR)
			#SCREEN.fill(WHITE)
			self.check_for_highlights()
			self.board.draw()
			pg.display.update()
			self.clock.tick(60)
			#print(self.line_highlighted) 
		if player1.points > player2.points:
			return player1
		else:
			return player2
