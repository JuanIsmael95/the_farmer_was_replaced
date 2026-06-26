set_world_size(8)
clear()
mayor = 0
x_mayor = -1
y_mayor = -1
size = get_world_size()

def reiniciar():
	global mayor
	global x_mayor
	global y_mayor
	mayor = -1
	x_mayor = -1
	y_mayor = -1

def volver_inicio():
	pos_actual = (get_pos_x(), get_pos_y())

	for i in range(pos_actual[1]):
		move(South) 
			
	for i in range(pos_actual[0]):
		move(West)

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

def check_agua():
	if get_entity_type() == Entities.Carrot:
		if num_items(Items.Water) > 0 and get_water() < 0.75:
			use_item(Items.Water)
 
def aversita(i, j):
	total = i + j
	if total % 2 == 0:
		return True
	else:
		return False

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