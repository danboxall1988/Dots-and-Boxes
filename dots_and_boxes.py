from common import *
from game import *
from exit_screen import *

def run_game():
	while True:
		game = Game()
		player1.reset_points()
		player2.reset_points()
		winner = game.main_loop()
		exit = ExitScreen(winner)
		choice = exit.main_loop()
		if choice == "Quit":
			break
			
if __name__ == "__main__":
	pg.init()
	pg.font.init()
	os.environ["SDL_VIDEO_CENTERED"] = "1"  
	run_game()
	pg.quit()
