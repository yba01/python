from checknumber import get_valid_and_novalid 	
import os
CLASS = ["6e", "5e", "4e", "3e", "2nd", "1st", "Tle"]	
def get_firstname() :
	while True :
		firstname = input("Enter a valid student's firstname: ")
		if firstname.isalnum() :
			return firstname
			
def get_name() :
	while True :
		name = input("Enter a valid student's name: ")
		if name.isalnum() :
			return name

def not_exist(tab, phone) :
	for student in tab :
		if student["Number"]==phone :
			return False
	return True

def get_number() :
	while True:
		number = input("Enter a valid student's number: ")
		valid, _ = get_valid_and_novalid(number)
		if len(valid)==1 :
			return valid[0]
		
def get_class() :
	while True :
		classe = input("Enter a valid class:\n1- 6e\n2- 5e\n3- 4e\n4- 3e\n5- 2nd\n6- 1st\n7- Tle\n: ")
		if classe.isnumeric() and 0<= int(classe) - 1 <=7 :
			return CLASS[int(classe) - 1]
		
def get_note(note) :
	while True :
		note_ = input(f'Enter a valid student {note} note: ')
		if note_.isnumeric() and 0<=int(note_)<=20:
			return int(note_) 
			
def calcul_mean(proj, dev, exam) :
	return round((proj + dev + exam)/3, 2)
	
def student_information(tab) :
	firstname = get_firstname()
	name = get_name()
	number = ''
	while True:
		number = get_number()
		if not_exist(tab, number):
			break

	classe = get_class()
	proj = get_note('project')
	dev = get_note('devoir')
	exam = get_note('exam')
	mean = calcul_mean(proj, dev, exam)
	return {"Firstname":firstname, "Name":name, "Number":number, "Class":classe, "Proj":proj, "Dev":dev, "Exam":exam, "Mean":mean}
	
  
def get_all_students_info():
	RUN = 1
	tab = []
	while RUN :
		student = student_information(tab)	
		tab.append(student)
		run = input('If you want to stop, Click on 0: ')
		if run.isnumeric() and int(run)==0 :
			RUN = 0
	return tab
 
 		
 		
def show_info(tab):
	print('+' + '-' * 74 + '+')		
	print(f'|{"Prenom":^10}|{"Nom":^10}|{"Telephone":^11}|{"Classe":^8}|{"Dev":^5}|{"Proj":^6}|{"Examen":^8}|{"Moyenne":^9}|')
	for student in tab :
		print(f"|{student["Firstname"]:^10}|{student["Name"]:^10}|{student["Number"]:^11}|{student["Class"]:^8}|{student["Dev"]:^5}|{student["Proj"]:^6}|{student["Exam"]:^8}|{student["Mean"]:^9}|")
	print('+' + '-' * 74 + '+')

def show_menu() :
	while True :
		choice = input("\n1- Afficher tout\n2- Trier et afficher \n3- Rechercher \n4- Modification \n5- Sortir\n: ")
		if choice.isnumeric() and 1<= int(choice) <=5 :
			return int(choice)
		
def sort_mean(tab) :
	sort_tab = tab
	for i in range(len(tab)) :
		for j in range(len(tab)) :
			if sort_tab[i]["Mean"]>sort_tab[j]["Mean"] :
				sort_tab[i], sort_tab[j] = sort_tab[j], sort_tab[i]
	return sort_tab

def get_criteria() :
	while True :
		criteria = input('Choose the search criteria:\n1- Prenom \n2- Nom \n3- Telephone \n4- Classe\n: ')
		if criteria.isnumeric() and 1<= int(criteria) <=4 :
			return ["Firstname", "Name", "Number", "Class"][int(criteria)-1]
		
def search(criteria, tab):
	value = input('Enter the value of {criteria}: ')
	tab_search = []
	for student in tab :
		if student[criteria]==value :
			tab_search.append(student)
	tab_search

def search_by_criteria(tab) :
	criteria = get_criteria()
	return search(criteria, tab)

def get_student(tab, phone):
		for index, student in enumerate(tab):
			if student["Number"]==phone :
				return index
		return -1

def get_type_note() :
	while True :
		criteria = input('Choose the note type to modify:\n1- Dev \n2- Proj \n3- Exam\n: ')
		if criteria.isnumeric() and 1<= int(criteria) <=3 :
			return ["Dev","Proj" ,"Exam"][int(criteria)-1]
		

def change_note(tab):
	number = get_number()
	index = get_student(tab, number)
	if index+1 :
		note_type = get_type_note()
		note = get_note()
		tab[index][note_type] = note
		tab[index]["Mean"] = calcul_mean(tab[index]["Dev"], tab[index]["Proj"], tab[index]["Exam"])


def execute_menu(tab) :
	while True :
		choice = show_menu()
		match choice :
			case 1:
				os.system("clear")
				show_info(tab)
			case 2:
				os.system("clear")
				show_info(sort_mean(tab))
			case 3:
				os.system("clear")
				show_info(search_by_criteria(tab))
			case 4:
				os.system("clear")
				change_note(tab)
			case 5:
				break

def main():
	students = get_all_students_info()
	os.system("clear")
	show_info(students)
	execute_menu(students)

		
main()