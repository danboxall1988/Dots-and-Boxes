from common import *
from game import *
from exit_screen import *
from intro_screens import *

def run_game():
	""" The entry point of the game """
	name_screen = NameSetter()
	name_screen.setup()
	while True:
		color_screen = ColorSetter()
		color_screen.setup()
		game = Game()
		player1.reset_points()
		player2.reset_points()
		winner = game.main_loop()
		exit = ExitScreen(winner)
		choice = exit.main_loop()
		if choice == "Quit":
			break
			
if __name__ == "__main__": 
	run_game()
	pg.quit()
