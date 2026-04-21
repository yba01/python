
RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA   = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)
COLOR = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
CHOSEN = []
MENU = "\n0-RED\n1-GREEN\n2-BLUE\n3-YELLOW\n4-CYAN\n5-MAGENTA"

def ask_for_size() :
	while True :
		ordre = input("ENTER THE MATRIX SIZE : ")
		if ordre.isnumeric() and int(ordre)>4 :
			return int(ordre)
		else:
			print('THE SIZE MUST BE A VALID NUMBER GREATER THAN 4!!!', end='\n\n')

def ask_for_color(position) :
	while True :
		color = input(f"{MENU}\nCHOOSE A COLOR FOR THE {position} POSITION: ")
		if color.isnumeric() and 0<=int(color)<=5 and COLOR[int(color)] not in CHOSEN :
			CHOSEN.append(COLOR[int(color)])
			return COLOR[int(color)]
		else:
			print('PLEASE CHOOSE A NOT CHOSEN VALID NUMBER!!!')

def rgb_color(color_0, color_1) :
    r = int(( color_0[0] + color_1[0] ) / 2)
    g = int(( color_0[1] + color_1[1] ) / 2)
    b = int(( color_0[2] + color_1[2] ) / 2)
    return f"\033[38;2;{r};{g};{b}m🆈\033[0m"

def show_matrix(ordre, ADDP ,EDDP ,SDP ,ADDS ,EDDS ,SDS) :
	print('\n')
	for i in range(ordre) :
		for j in range(ordre) :
			if j>i and i+j>ordre-1 :
				print(rgb_color(ADDP, ADDS), end='    ')
			elif j>i and i+j<ordre-1 :
				print(rgb_color(ADDP, EDDS), end='    ')
			elif j<i and i+j<ordre-1 :
				print(rgb_color(EDDP, EDDS), end='    ')
			elif j<i and i+j>ordre-1 :
				print(rgb_color(EDDP, ADDS), end='    ')
			elif j==i and i+j==ordre-1 :
				print(rgb_color(SDP, SDS), end='    ')
			elif j==i and i+j!=ordre-1 :
				print(rgb_color(SDP, (0,0,0)), end='    ')
			elif j!=i and i+j==ordre-1 :
				print(rgb_color((0,0,0), SDS), end='    ')		
		print('\n')

def create_and_color_matrix() :
	ordre = ask_for_size()
	ADDP = ask_for_color('ADDP')
	EDDP = ask_for_color('EDDP')
	SDP = ask_for_color('SDP')
	ADDS = ask_for_color('ADDS')
	EDDS = ask_for_color('EDDS')
	SDS = ask_for_color('SDS')
	show_matrix(ordre, ADDP ,EDDP ,SDP ,ADDS ,EDDS ,SDS)

create_and_color_matrix()
