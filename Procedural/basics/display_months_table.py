	
tab_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembrer", "Octobre","Novembre", "Décembre"]

tab_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#tab_choisen = []

while True :
	lang = input("Si vous voulez que les mois s'affiche en anglais saisir E, en français saisir F:")
	if lang=='E' or lang=='F' :
		break

if lang=='E' :
	tab_chosen = tab_en
else:
	tab_chosen = tab_fr
print('+'+'-------'*9+'+')
for i in range(3) :
	for j in range(i,12,3) :
		print('| '+tab_chosen[j].ljust(13)+' ', end='')
	print('|')
	print('+'+'-------'*9+'+')

