from src import data_reader as dr
from src import data_validator as dv
from prettytable import PrettyTable

data = dr.read_file("/home/yba/Downloads/Personal Exercices/python-exercices/mini_projects/new_project/data/Donnees_Projet_Python_Dev_Data.csv")
table = dr.put_raw_data_in_dict(data, ';')
dv.validate_table(table)
valid_data, invalid_data  = dv.get_valid_or_invalid(table)

# print(table)
tabval = PrettyTable()
tabinv = PrettyTable()

column = ['code', 'numero', 'prenom', 'nom', 'date', 'classe', 'math', 'pc', 'svt', 'ang', 'fr', 'hg', 'description']
for col in  column[:12]:
    tabval.add_column(col, valid_data[col])

for col in  column:
    tabinv.add_column(col, invalid_data[col])

tabnum = PrettyTable()
number = '20LH7BG'
for i, val in enumerate(valid_data['numero']):
    if val == number:
        for col in  column[:12]:
            tabnum.add_column(col, [valid_data[col][i]])





    

# print(tabval)
# print()
# print(invalid_data)
print(tabnum)