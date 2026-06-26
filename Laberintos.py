clear()
size  = get_world_size()
do_a_flip()
while(True):
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 3)
	while(get_entity_type() != Entities.Treasure):

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