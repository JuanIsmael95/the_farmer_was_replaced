set_world_size(8)
clear()

size = get_world_size()

def plantar_calabazas():
	for i in range(size):
		for j in range(size):
			if(get_ground_type() != Grounds.Soil):
				till()
			plant(Entities.Pumpkin)
			move(East)
		move(North)

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
				
def esperar():
	for i in range(2):
		pet_the_piggy()
		do_a_flip()


	
	
def main():
	plantar_calabazas()
	se_puede_cosechar()
	harvest()
while(True):
	main()