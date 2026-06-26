'''
Here I try to maximize the value of pumpkins before being able to use more than one drone.
That's why I set the world size to 8, so i can have the maximum value of the 8x8 pumpkin without it being
too slow
'''

set_world_size(8)
clear()

#I don't set size=8 in case I use this code for a bigger farm
size = get_world_size()
'''
This function only plants pumpkins in all the grid, nothing really complicated here.
'''
def plantar_calabazas():
	for i in range(size):
		for j in range(size):
			if(get_ground_type() != Grounds.Soil):
				till()
			plant(Entities.Pumpkin)
			move(East)
		move(North)
'''
This function is made to check if there is any dead pumpkin in the farm and the 8x8 pumpkin can't be made.
it starts with a boolean value set to false, and the loop only ends if the drone checks all pumpkins and there isn't
any dead pumpkin, in case a replanted pumpkin becomes again in a dead pumpkin.
'''
def se_puede_cosechar():
	mal = False
	while(mal == False):
		mal = True
		for i in range(size):
			for j in range(size):
				if can_harvest() == False:
					if(get_entity_type() == Entities.Dead_Pumpkin):
						plant(Entities.Pumpkin)
						mal = False
				move(East)
			move(North)

'''
This function only exists because in early versions when the farm was smaller I had to wait before checking for dead pumpkins, 
because usually when the check began, the pumpkin in (0,0) wasn't grown yet, the drone saw nothing wrong and later it would grow into a dead one.
But when the farm is bigger it isn't needed.
'''
def esperar():
	for i in range(2):
		pet_the_piggy()
		do_a_flip()


	
'''
Nothing to say here I think :$
'''
def main():
	plantar_calabazas()
	se_puede_cosechar()
	harvest()
while(True):
	main()
