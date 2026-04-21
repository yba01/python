def remove_space(text) :
	_text = ''
	for char in text :
		if char != ' ' :
			_text += char
	return _text

def get_number(text) :
	return text.split('-')
	
def isnumber(number) :
	if number.isnumeric() and len(number)==9 and (number[:2]=='77' or number[:2]=='78' or number[:2]=='76' or number[:2]=='70' or number[:2]=='75') :
		return 1
	return 0
	
def get_valid_and_novalid(text) :
	numbers = get_number(remove_space(text))
	valid = []
	not_valid = []
	for number in numbers:
		if isnumber(number) :
			valid.append(number)
		else:
			if number :
				not_valid.append(number)
	return valid, not_valid

def add_op(number, op) :
	for deb in op :
		if number==deb :
			return 1
	return 0
	
def get_number_by_operator(valid) :
	orange = tigo = expresso = promobile = 0
	for number in valid :
		orange += add_op(number[:2], ["77", "78"])
		tigo += add_op(number[:2], ["76"])
		expresso += add_op(number[:2], ["70"])
		promobile += add_op(number[:2], ["75"])
		# if number[:2]=='77' or number[:2]=='78' :
		# 	orange += 1
		# elif number[:2]=='76' :
		# 	tigo += 1
		# elif number[:2]=='70' :
		# 	expresso += 1
		# else:
		# 	promobile += 1
	return orange, tigo, expresso, promobile
	
	
def show_number(valid, invalid) :
	print(f'+-----------------------------+')
	print(f'|  Valid     |    Invalid     |')
	print(f'+-----------------------------+')
	for i in range(max(len(valid), len(invalid))) :
		if i<len(valid) and i<len(invalid) :
			print(f'|{valid[i]}   |	{invalid[i]}')
		elif i<len(valid) and not i<len(invalid) :
			print(f'|{valid[i]}   |                |')
		elif not i<len(valid) and i<len(invalid) :
			print(f'|            |	{invalid[i]}	')
	print(f'+-----------------------------+')
			
			
	
		
def show_operator(valid) :
	sn, ti, ex, pr = get_number_by_operator(valid)
	print(f'+-----------------------------+')
	print(f'| Operator     |              |')
	print(f'+-----------------------------+')
	print(f'|Orange        |       {sn}      |')	
	print(f'|Tigo          |       {ti}      |')	
	print(f'|Expresso      |       {ex}      |')	
	print(f'|Promobile     |       {pr}      |')
	print(f'+-----------------------------+')	
	
	
def number_checking(text) :
	valid, invalid = get_valid_and_novalid(text)
	if valid or invalid :
		show_number(valid, invalid)
		print('\n\n')
	else:
		print("Empty output : there 's no number") 
	show_operator(valid)
	

if __name__== "__main__" :
	##test value	
	text0 = ""
	#text1 = "77 123 45 67-78 987 65 43-76 111 22 33"
	#text2 = "77 123 45 67-79 123 45 67-76 1112233-70 123 45 678-75 987 65 43"
	text3 = "77 123 45-78 98 76 54-75 123 45 6a-70 123 45 67-76 12 34 56 78"
	#text4 = " 77 123 45 67 -78  987 65 43- 76 111 22 33 -70 123 45 67 "
	#text5 = "77 123 45 67-78abcdefghi-76 111 22 33-70 1234 567-75 98 76 54 32-75 123 45 67"
	#text6 = "77 123 45 67-77 765 43 21-78 987 65 43-78 111 22 33-70 123 45 67-75 987 65 43"
	text7 = "77 123 45 67--78 987 65 43---76 111 22 33"
	# text = input("Give a serie of number separated by '-': ") 
	print(number_checking(text3))

		
