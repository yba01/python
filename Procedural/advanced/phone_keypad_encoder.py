def correspondance(char) :
	match char:
		case "0" :
			return "a"
		case "1" :
			return "b"
		case "2" :
			return "c"
		case "3" :
			return "d"
		case "4" :
			return "e"
		case "5" :
			return "f"
		case "6" :
			return "g"
		case "7" :
			return "h"
		case "8" :
			return "i"
		case "9" :
			return "j"
		case " " :
			return "00"
		case "A" | "a" :
			return "2"
		case "B" | "b" :
			return "22"
		case "C" | "c" :
			return "222"
		case "D" | "d" :
			return "3"
		case "E" | "e" :
			return "33"
		case "F" | "f" :
			return "333"
		case "G" | "g" :
			return "4"
		case "H" | "h" :
			return "44"
		case "I" | "i" :
			return "444"
		case "J" | "j" :
			return "5"
		case "K" | "k" :
			return "55"
		case "L" | "l" :
			return "555"
		case "M" | "m" :
			return "6"
		case "N" | "n" :
			return "66"
		case "O" | "o" :
			return "666"
		case "P" | "p" :
			return "7"
		case "Q" | "q" :
			return "77"
		case "R" | "r" :
			return "777"
		case "S" | "s" :
			return "7777"
		case "T" | "t" :
			return "8"
		case "U" | "u" :
			return "88"
		case "V" | "v" :
			return "888"
		case "W" | "w" :
			return "9"
		case "X" | "x" :
			return "99"
		case "Y" | "y" :
			return "999"
		case "Z" | "z" :
			return "9999"
		case _ :
			return char


def separator(text, corresp) :
	if text=='' :
		return corresp
	else:
		if text[-1]==corresp[0] :
			return f'0{corresp}'
		else:
			return f'{corresp}'
		

def text_to_phonetext(text) :
	phone = ''
	for char in text :
		phone += separator(phone, correspondance(char))
	return phone

print(text_to_phonetext('J’ai 17,5 en algo'))
