from decor import Decor
from macgyver import MacGyver
from items import Items
from guard import Guard
from displayterminalmode import DisplayTerminalMode


FILE = 'structure.maze'

def input_user():

	return input()
	
def main():

	structure = Decor(FILE)
	hero = MacGyver(structure)
	stuff = Items(structure)
	pnj = Guard(structure)
	displaying = DisplayTerminalMode()
	
	while True:
		
		if hero.position in stuff.positions:
			stuff.picked_up_items(hero.position)
		displaying.refresh(structure, hero, stuff, pnj)
		choice = input_user()
		
		previous_position = hero.position
		
		hero.movement(choice)
		
		if structure.is_hallways(hero):
			continue
		else:
			hero.position = previous_position
			continue
		

main()
	


	