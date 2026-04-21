import re
from datetime import datetime

Dates = {"Janvier":"January", "Fevrier":"February", "Mars":"March", "Avril":"April", "Mai":"May", "Juin":"June", "Juillet":"July", "Aout":"August", "Septembre":"September", "Octobre":"October", "Novembre":"November", "Decembre":"December"}
dates = {"Fev":"Feb", "Avr":"Apr", "Mai":"May", "Jui":"Jun", "Jui":"Jul", "Aou":"Aug"}

def decript_error(table, index, colonne, descrip):
    table[colonne][index] = None
    table['valid'][index] = False
    if not table['description'][index] :
        table['description'][index] = [descrip]
    else:
        table['description'][index].append(descrip)


def validate_code(table):
    for index, code in enumerate(table['code']):
        if not re.search(r"^[A-Z]{3}[0-9]{3}$", code):
            decript_error(table, index, 'code', ' CI ')

def validate_numero(table):
    for index, numero in enumerate(table['numero']):
        if not re.search(r"^[A-Z0-9]{7}$", numero):
            decript_error(table, index, 'numero', ' NI ')

def validate_prenom(table):
    for index, prenom in enumerate(table['prenom']):
        if not re.search(r"^[A-Za-z].{2,}$", prenom):
            decript_error(table, index, 'prenom', ' PI ')
        

def validate_nom(table):
    for index, nom in enumerate(table['nom']):
        if not re.search(r"^[A-Za-z].{1,}$", nom):
            decript_error(table, index, 'nom', ' NOI ')

def validate_classe(table):
    for index, classe in enumerate(table['classe']):
        if not re.search(r"^[3-6].*[A-Da-d]$", classe):
            decript_error(table, index, 'classe', ' CLI ')
        else:
            table['classe'][index] =classe[0]+'e '+classe[-1].upper() 


def separator(date):
    for sep in [' ', '/', '_',  '-', ',', '|', '.', ':']:
        if sep in date:
            return sep
        
def parse_date(date):
    day, month, year = '', '', ''
    date_part = date.split(separator(date))
    if len(date_part) == 3:
        day, month, year = date_part
    return day, month, year


def str_date_dmy(day, month, year):
    date = f'{day}/{month}/{year}'
    try:
        date = datetime.strptime(date, "%d/%m/%y").date()
        date = date.strftime('%d/%m/%Y')
        return date
    except Exception as e:
        return ""
    
def validate_dmy(d, m, y, table, i):
    date = str_date_dmy(d, m, y)
    if date:
        table['date'][i] = date
    else:
            decript_error(table, i, 'date', ' DI ')


def str_date_dmyear(day, month, year):
    date = f'{day}/{month}/{year}'
    try:
        date = datetime.strptime(date, "%d/%m/%Y").date()
        date = date.strftime('%d/%m/%Y')
        return date
    except:
        return ""
    
def validate_dmyear(d, m, y, table, i):
    date = str_date_dmyear(d, m, y)
    if date:
        table['date'][i] = date
    else:
            decript_error(table, i, 'date', ' DI ')


def str_date_dMonthyear(day, month, year):
    if month.capitalize() in Dates.keys():
        month = Dates[month.capitalize()]

    if month.capitalize() in dates.keys():
        month = dates[month.capitalize()]

    date = f'{day}/{month.capitalize()}/{year}'
    if len(month)>3:
        try:
            date = datetime.strptime(date, "%d/%B/%Y").date()
            date = date.strftime("%d/%m/%Y")
            return True
        except:
            return ""
    elif len(month)==3:
        try:
            date = datetime.strptime(date, "%d/%b/%Y").date()
            date = date.strftime("%d/%m/%Y")
            return date
        except:
            return ""    
        

def validate_dMonthyear(d, m, y, table, i):
    date = str_date_dMonthyear(d, m, y)
    if date:
        table['date'][i] = date
    else:
            decript_error(table, i, 'date', ' DI ')



   

def validate_date(table):
    for index, date in enumerate(table['date']):
        # longueur de la chaine < 8: date invalide
        if len(date)<8:
            decript_error(table, index, 'date', ' DI ')
        else:
            day, month, year = parse_date(date)
            if day and month and year:
                # 1er cas - dd/mm/yy
                if len(date)==8:
                    validate_dmy(day, month, year, table, index)
                else:
                    # 2e cas - dd/mm/yyyy
                    if month.isnumeric():
                        validate_dmyear(day, month, year, table, index)
                    #3e cas - dd/Janvier(Jan)/yyyy
                    elif month.isalpha():
                        validate_dMonthyear(day, month, year, table, index)
        # Si le mois n'est ni numerique, ni alphabetique: la date est invalide
                    else:
                        decript_error(table, index, 'date', ' DI ')
        # Si on arrive pas à parser la date et avoir 3 valeur: jour, mois, annee , la date est invalide
            else:
                decript_error(table, index, 'date', ' DI ')


def validate_note(table, note_name):
    for index, note in enumerate(table[note_name]):
        if not note or (note and not (0<=note<=20)):
            # table[note_name][index] = None
            des = note_name.upper()+'I'
            decript_error(table, index, note_name, des)
        # elif not note:
        #     des = note_name.upper()+'I'
        #     decript_error(table, index, note_name, des)


def validate_all_note(table):
    matiere = ['math', 'pc', 'svt', 'ang', 'fr', 'hg']
    for name in matiere:
        validate_note(table, name)


def validate_table(table):
    validate_code(table)
    validate_numero(table)
    validate_prenom(table)
    validate_nom(table)
    validate_classe(table)
    validate_date(table)
    validate_all_note(table)


def get_valid_or_invalid(table):
    vtable = {}
    itable = {}
    column = ['code', 'numero', 'prenom', 'nom', 'date', 'classe', 'math', 'pc', 'svt', 'ang', 'fr', 'hg', 'description']
    for col in column :
        get_line_info(vtable, itable, table, col)
    return vtable, itable
    


def get_line_info(vtab, itab,table, column):
    vliste= []
    invliste = []
    for index, valid in enumerate(table['valid']):
        if valid :
            if column != 'description':
                vliste.append(table[column][index])
        else:
            invliste.append(table[column][index])
    if column != 'description':        
        vtab[column] = vliste
    itab[column] = invliste