#This is my second version of the main implementing sunflowers

set_world_size(8)
clear()
mayor = 0
x_mayor = -1
y_mayor = -1
size = get_world_size()

'''
This function only resets the max values to its original value for the main.
'''
def reiniciar():
	global mayor
	global x_mayor
	global y_mayor
	mayor = -1
	x_mayor = -1
	y_mayor = -1
'''
This function moves the drone from its position to the initial grid (0,0)
'''
def volver_inicio():
	pos_actual = (get_pos_x(), get_pos_y())

	for i in range(pos_actual[1]):
		move(South) 
			
	for i in range(pos_actual[0]):
		move(West)

'''
This function calculates how many times the drone has to move to arrive to the 
sunflower with the most petals and moves to it
'''
def cosechar_girasol():
	pos_actual = (get_pos_x(), get_pos_y())
	iteraciones_vertical = pos_actual[1] - y_mayor
	iteraciones_horizontal = pos_actual[0] - x_mayor
	
	for i in range(abs(iteraciones_vertical)): 
		if iteraciones_vertical < 0:
			move(North)
		else:
			move(South)
			
	for i in range(abs(iteraciones_horizontal)):
		if iteraciones_horizontal < 0:
			move(East)
		else:
			move(West)

	while can_harvest() == False:
		pet_the_piggy()
	harvest()
	plant(Entities.Sunflower)

'''
This function checks if the current box has enough water, if not, it uses water
'''
def check_agua():
	if get_entity_type() == Entities.Carrot:
		if num_items(Items.Water) > 0 and get_water() < 0.75:
			use_item(Items.Water)
'''
This function checks if the current box is an even diagonal
'''
def aversita(i, j):
	total = i + j
	if total % 2 == 0:
		return True
	else:
		return False
'''
This function first checks the return value of aversita(), if it's True it plants a tree. Then if it's one of the first 3 rows,
it plants sunflowers and calls the function buscar_girasol(), and plant carrots in each other row.
'''
def plantar(i, j):
	if aversita(i, j):
		plant(Entities.Tree)
	else:
		if(get_ground_type() != Grounds.Soil):
			till()
		if i < 3:
			plant(Entities.Sunflower)
			buscar_girasol()
		else:
			plant(Entities.Carrot)

'''
This function checks the current box, which is always a sunflower, and saves its position
if it has more petals than the gratest.
'''
def buscar_girasol():
	temp = measure()
	if temp >= mayor:
		global mayor
		global x_mayor
		global y_mayor
		mayor = temp
		x_mayor = get_pos_x()
		y_mayor = get_pos_y()

do_a_flip()
while(True):
	for i in range(get_world_size()):
		for j  in range(get_world_size()):
			if can_harvest():
				if get_entity_type() != Entities.Sunflower:
					harvest()
				plantar(i, j)   
			check_agua()

			move(East)
		move(North)
	print(mayor, x_mayor, y_mayor)
	cosechar_girasol()
	reiniciar()
	volver_inicio()
