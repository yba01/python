def read_file(filename):   
    """ This function get the filename or a file path and return the content of file"""  

    with open(filename, 'r') as f:
        data = []
        #Lire par ligne
        for line in f:
            data.append(line.rstrip('\n'))
        return data[1:]



def change_line(line, sep):
    correct_line = line.rstrip('\n')
    return correct_line.split(sep)

def get_colonne_value(line):
    code = numero = nom = prenom = date = classe = note = ''
    if len(line)>7:
        code, numero, nom, prenom, date, classe, *note = line
    else:
        colonne = [code, numero, nom, prenom, date, classe, note]
        for i, value in enumerate(line):
            colonne[i] = value
    return colonne

# def to_date(date):
#     return datetime.strptime(date, "%d/%m/%y").date()

def append_in_dict(dict, colonne):
    dict['code'].append(colonne[0])
    dict['numero'].append(colonne[1])
    dict['nom'].append(colonne[2])
    dict['prenom'].append(colonne[3])
    dict['date'].append(colonne[4])
    dict['classe'].append(colonne[5])
    dict['note'].append(colonne[6])


def put_raw_data_in_dict(data, sep):
    """ 
    This function function accept data (list) as argument, get each element of it(str) :
        1. split each element by a known separator: (change_line)
        2. get the value of each column of them :(get_clonne_value)
        3. append each value in a list of our dictionnary stracture that represent a column: (append_in_dict)

                            {
                                'code':[....],
                                'numero':[...],
                                    ....
                                    ....
                                    ....

                            }
    """
    
    table = {'code':[], 'numero':[], 'nom':[], 'prenom':[], 'date':[], 'classe':[], 'note':[]}
    for line in data:
        corrected_line = change_line(line, sep)
        colon_value = get_colonne_value(corrected_line)
        append_in_dict(table, colon_value)

    get_complete_data(table)
    del table['note']
    return table



def get_notes(note_str):
    try:
        notes = note_str.strip(']').replace(",", ".").split('[')[1]
        notes = notes.split('|')
        notes.extend(notes[-1].split(':'))
        del notes[-3]
        # print(notes)
        return notes
    except:
        # print('None')
        return None

def get_mean(dev):
    try:
        mean_dev = sum([float(f) for f in dev[:len(dev)-1]])/(len(dev) - 1)
        mean = round(( mean_dev + ( 2 * float(dev[-1]) )) / 3, 2)
        return mean
    except:
        return None
    

def put_note(table, matiere_note, index, matiere_name):
    mean = get_mean(get_notes(matiere_note))
    if mean :
        table[matiere_name][index] =  mean

def get_complete_data(table):
    table['description'] = [None]*len(table['code'])
    table['math'] = [None]*len(table['code'])
    table['pc'] = [None]*len(table['code'])
    table['svt'] = [None]*len(table['code'])
    table['ang'] = [None]*len(table['code'])
    table['fr'] = [None]*len(table['code'])
    table['hg'] = [None]*len(table['code'])
    table['valid'] = [True]*len(table['code'])

    for index, note in enumerate(table['note']):
        for matiere in note.replace(" ", "").split('#'):
            if 'math' in matiere.lower():
                put_note(table, matiere, index, 'math') 
            elif 'pc' in matiere.lower() or 'science' in matiere.lower():
                put_note(table, matiere, index, 'pc')
            elif 'svt' in matiere.lower():
                put_note(table, matiere, index, 'svt') 
            elif 'fran' in matiere.lower():
                put_note(table, matiere, index, 'fr') 
            elif 'anglais' in matiere.lower():
                put_note(table, matiere, index, 'ang')
            elif 'hg' in matiere.lower():
                put_note(table, matiere, index, 'hg')
