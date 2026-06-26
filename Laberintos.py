#This is a really lazy approach to the solution, only viable in at max 3x3 mazes, unless it requires to deviate from a straight line

clear()
size  = get_world_size()
do_a_flip()
while(True):
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 3) #Create a 3x3 maze
	while(get_entity_type() != Entities.Treasure):
		
		'''If the drone can move in a direction, it moves untill the end of the path, so it can't change paths
			while its moving. I will change this code to be more optimal in the future'''
		
		if can_move(East):
			while(can_move(East)):
				move(East)
		elif can_move(West):
			while(can_move(West)):
				move(West)
		if can_move(North):
			while(can_move(North)):
				move(North)
		elif can_move(South):
			while(can_move(South)):
				move(South)
	harvest()
