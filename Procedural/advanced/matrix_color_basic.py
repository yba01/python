def show_matrix(blue_position, ordre) :
	RED = '\033[91m'
	BLUE = '\033[94m'
	ENDC = '\033[0m' 
	BOX = '❏'

	color_bas = ''
	color_haut = ''
	if blue_position=='H' :
		color_haut = BLUE
		color_bas = RED
	else :
		color_haut = RED
		color_bas = BLUE
		
	print('\n')
	for i in range(ordre) :
		for j in range(ordre) :
			if j>i :
				print(color_haut+BOX+ENDC, end='    ')
			elif i==j :
				print(BOX, end='    ')
			else:
				print(color_bas+BOX+ENDC, end='    ')
		print('\n')
				

ordre = 1
while ordre<6 :
	ordre = input("Enter the matrix size : ")
	if not ordre.isnumeric() :
		ordre = 1
	else:
		ordre = int(ordre)
	
blue_position = ""
while blue_position!="B" and blue_position!="H" :
	blue_position = input("Enter the position of the blue color. You can choose B(bas) or H(haut): ")

show_matrix(blue_position, ordre)


		
		
		
		
		
		
		
		
		
		
		
		
