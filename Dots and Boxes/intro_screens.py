from common import *

class NameSetter:
	""" This class handles the intro of the game, that is it gets
		both players names and allows them to choose which color they
		will play with
	"""
	def __init__(self):
		self.textbox = pg.Surface((200, 50))
		self.textbox_rect = self.textbox.get_rect(center = \
			(SCREEN_SIZE[0] // 2, 175))
		self.font = pg.font.SysFont("Comic Sans SF", 50)
		self.name = None
		self.name_entered = False
		self.btn = pg.Surface((200, 120))
		self.btn_font = pg.font.SysFont("Comic Sans SF", 30)
		self.btn_rect = self.btn.get_rect(center = \
			(SCREEN_SIZE[0] // 2, 450))
	
	def setup(self):
		self.enter_name(player1)
		self.enter_name(player2)
		
	def enter_name(self, player):
		""" Contains main loop, which is called twice, once for each
			player.
		"""
		self.name_entered = False
		self.name = ""
		while not self.name_entered:
			self.event_loop()
			self.draw(player)
		if len(self.name) > 0:
			player.name = self.name
			
	def event_loop(self):
		""" Handles keystrokes and quit actions """
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_BACKSPACE:
					self.name = self.name[:-1]
				elif event.key == pg.K_RETURN:
					self.name_entered = True						
					#print("enter")
					continue						
				elif event.unicode.isalnum():
					if len(self.name) <= 7:
						self.name += event.unicode.upper()
			elif event.type == pg.MOUSEBUTTONDOWN:
				pos = pg.mouse.get_pos()
				if self.btn_rect.collidepoint(pos):
					self.name_entered = True
	
	def draw(self, player):
		SCREEN.fill(BG_COLOR)
		self.draw_textbox()
		self.draw_title(player)
		self.draw_button()
		pg.display.update()
	
	def draw_button(self):
		self.btn.fill(PURPLE)
		text = self.btn_font.render("Enter", True, BLACK)
		text_rect = text.get_rect(center = \
			(self.btn_rect.width // 2, self.btn_rect.height // 2))
		self.btn.blit(text, text_rect)
		SCREEN.blit(self.btn, self.btn_rect)
		
	def draw_textbox(self):
		self.textbox.fill(GREY)
		# Set up text entered by keyboard
		text = self.font.render(self.name, True, BLACK)
		text_rect = text.get_rect(center = \
			(self.textbox_rect.width // 2, self.textbox_rect.height // 2))
		# Blit text to textbox
		self.textbox.blit(text, text_rect)
		# Blit textbox to screen
		SCREEN.blit(self.textbox, self.textbox_rect)
							
	def draw_title(self, player):
		# Print first line of title to screen
		title = self.font.render(player.name, True, BLACK)
		title_rect = title.get_rect(center = \
			(SCREEN_SIZE[0] // 2, 50))
		SCREEN.blit(title, title_rect)
		# Print second line of title to screen
		title2 = self.font.render("Enter your name", True, BLACK)
		title2_rect = title2.get_rect(center = \
			(SCREEN_SIZE[0] // 2, 100))
		SCREEN.blit(title2, title2_rect)


class ColorSetter:
	""" This class is used for each player to pick which color
		they would like to play with
	"""
	def __init__(self):
		self.colors = []
		self.color_rects = []
		self.color_chosen = False
		self.font = pg.font.SysFont("Comic Sans SF", 50)
		
	def setup(self):
		""" Sets up the colors of each player. setup_color_rects()
			is run once for each player, so that they cannot choose
			the same colors.
		"""
		self.colors = COLORS.copy()
		self.setup_color_rects()
		self.get_color(player1)
		self.color_chosen = False
		self.setup_color_rects()
		self.get_color(player2)
	
	def setup_color_rects(self):
		""" Populate a list of rects, containing the positions of 
			each color block that can be selected
		"""
		self.color_rects = []
		color_count = len(self.colors)
		gap_count = color_count - 1
		mid = SCREEN_SIZE[0] // 2
		size = color_count * 50 + gap_count * 20
		start_x = mid - size // 2
		#print(size)
		for i in range(color_count):
			surface = pg.Surface((50, 50))
			rect = surface.get_rect()
			rect.x = start_x + i * 50 + i * 20
			rect.y = 400
			self.color_rects.append(rect)
				
	def get_color(self, player):
		""" This is the main loop """
		while not self.color_chosen:
			self.event_loop(player)
			SCREEN.fill(BG_COLOR)
			self.draw_colors()
			self.draw_title(player)
			pg.display.update()
			
	def event_loop(self, player):
		""" Handles mouse action and sets color """
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				for i, rect in zip(range(len(COLORS)), self.color_rects):
					if rect.collidepoint(pg.mouse.get_pos()):
						player.color = self.colors[i]
						self.colors.remove(player.color)
						self.color_chosen = True
	
	def draw_title(self, player):
		# Print first line of title to screen
		title = self.font.render(player.name, True, BLACK)
		title_rect = title.get_rect(center = \
			(SCREEN_SIZE[0] // 2, 50))
		SCREEN.blit(title, title_rect)
		title2 = self.font.render("Choose your color", True, BLACK)
		title2_rect = title2.get_rect(center = \
			(SCREEN_SIZE[0] // 2, 100))
		SCREEN.blit(title2, title2_rect)

			
	def draw_colors(self):
		for rect, color in zip(self.color_rects, self.colors):
			surface = pg.Surface((50, 50))
			surface.fill(color)
			SCREEN.blit(surface, rect)


