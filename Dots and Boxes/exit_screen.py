from common import *

class ExitScreen:
	def __init__(self, player):
		self.winner_font = pg.font.SysFont("Comic Sans SF", 50)
		self.btn_font = pg.font.SysFont("Comic Sans SF", 30)
		self.player = player
		self.winning_color = self.player.color
		self.button_size = (150, 100)
		self.pa_btn = pg.Surface(self.button_size)
		self.pa_btn_rect = self.pa_btn.get_rect()
		self.pa_btn_rect.x = 50
		self.pa_btn_rect.y = 400
		self.q_btn = pg.Surface(self.button_size)
		self.q_btn_rect = self.q_btn.get_rect()
		self.q_btn_rect.x = 350
		self.q_btn_rect.y = 400
		self.running = True
		self.choice = None
	
	def draw_text(self):
		winner_str1 = f"Winner is {self.player.name}"
		winner_str2 = f"with {self.player.points} boxes!"
		winner_surface1 = self.winner_font.render(winner_str1, True, self.player.color)
		winner_rect1 = winner_surface1.get_rect(center = (SCREEN_SIZE[0] // 2, 100))
		winner_surface2 = self.winner_font.render(winner_str2, True, self.player.color)
		winner_rect2 = winner_surface2.get_rect(center = (SCREEN_SIZE[0] // 2, 150))
		SCREEN.blit(winner_surface1, winner_rect1)
		SCREEN.blit(winner_surface2, winner_rect2)
	
	def draw_buttons(self):
		# Play Again button
		self.pa_btn.fill(PURPLE)
		pa_txt = self.btn_font.render("Play Again", True, BLACK)
		pa_txt_rect = pa_txt.get_rect(center = \
			(self.pa_btn_rect.width // 2, self.pa_btn_rect.height // 2))
		self.pa_btn.blit(pa_txt, pa_txt_rect)
		SCREEN.blit(self.pa_btn, self.pa_btn_rect)
		# Quit Button
		self.q_btn.fill(PURPLE)
		q_txt = self.btn_font.render("Quit", True, BLACK)
		q_txt_rect = q_txt.get_rect(center = \
			(self.q_btn_rect.width // 2, self.q_btn_rect.height // 2))
		self.q_btn.blit(q_txt, q_txt_rect)
		SCREEN.blit(self.q_btn, self.q_btn_rect)		
	
	def event_loop(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				#print("mouse button down")
				pos = pg.mouse.get_pos()
				if self.pa_btn_rect.collidepoint(pos):
					#print("Play Again")
					self.choice = "Play Again"
				elif self.q_btn_rect.collidepoint(pos):
					#print("Quit")
					self.choice = "Quit"
		
	def main_loop(self):
		while not self.choice:
			self.event_loop()
			SCREEN.fill(BG_COLOR)
			self.draw_text()
			self.draw_buttons()
			pg.display.update()
		return self.choice
		
