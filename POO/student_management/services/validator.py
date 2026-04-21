from model.date import Date
import re
class Validateur:

    def validate_student(self, student):
        if (not student.nom and not student.prenom and not student.numero and not student.classe):
            student.valid = False
            student.erreurs.append('cette ligne est vide')
        else:    
            self.validate_code(student)
            self.validate_numero(student)
            self.validate_prenom(student)
            self.validate_nom(student)
            self.validate_classe(student)
            self.validate_date(student)
            self.validate_note(student)

    def validate_note(self, student):
        self.validate_matiere(student)
        self.validate_exam(student)
        self.validate_devoirs(student)


    def validate_exam(self, student):
        for note in student.note:
            if note.matiere is not None:
                if note.exam is None or not 0<=note.exam<=20 :
                    note.valid = False
                    student.valid = False
                    student.erreurs.append(f'examen de {note.matiere} invalid')

    def validate_devoirs(self, student):
        for note in student.note:
            if note.matiere is not None:
                for index, dev in enumerate(note.devoirs):
                    if dev is None or not 0<=dev<=20 :
                        note.valid = False
                        student.valid = False
                        student.erreurs.append(f'devoirs {index + 1} de {note.matiere} invalid')    

    def validate_matiere(self, student):
        mat = [note.matiere for note in student.note]
        if len(student.note) < 6 :
            for note in ['math', 'pc', 'svt', 'ang', 'fr', 'hg']:
                if note not in mat:
                    student.valid = False
                    student.erreurs.append(f"note {note} vide")
        elif len(student.note) > 6:
            for note in ['math', 'pc', 'svt', 'ang', 'fr', 'hg']:
                if mat.count(note)>1:
                    student.valid = False
                    student.erreurs.append(f"{note} est dupliquée")
                
        for note in mat:
            if note is None:
                student.valid = False
                student.erreurs.append(f"matiere pas prise en compte")
                
 
           
    def validate_code(self, student):    
        if not re.search(r"^[A-Z]{3}[0-9]{3}$", student.code):
            student.valid = False
            student.erreurs.append('code incorrect')

    def validate_numero(self, student):
        if not re.search(r"^[A-Z0-9]{7}$", student.numero):
            student.valid = False
            student.erreurs.append('numero incorrect')

    def validate_prenom(self, student):
        if not re.search(r"^[A-Za-z].{2,}$", student.prenom):
            student.valid = False
            student.erreurs.append('prenom incorrect')

    def validate_nom(self, student):
        if not re.search(r"^[A-Za-z].{1,}$", student.nom):
            student.valid = False
            student.erreurs.append('nom incorrect')

    def validate_classe(self, student):
        if not re.search(r"^[3-6].*[A-Da-d]$", student.classe):
            student.valid = False
            student.erreurs.append('classe incorrect')
        else:
            student.classe=student.classe[0]+'e '+student.classe[-1].upper() 

    def validate_date(self, student):
        if len(student.date)<8:
            student.valid = False
            student.erreurs.append('date incorrect')
        else:
            date = Date(student)
            day, month, year = date.parse_date()
            if day and month and year:
                # 1er cas - dd/mm/yy
                if len(student.date)==8:
                    date.validate_dmy(day, month, year)
                else:
                    # 2e cas - dd/mm/yyyy
                    if month.isnumeric():
                        date.validate_dmyear(day, month, year)
                    #3e cas - dd/Janvier(Jan)/yyyy
                    elif month.isalpha():
                        date.validate_dMonthyear(day, month, year)
        # Si le mois n'est ni numerique, ni alphabetique: la date est invalide
                    else:
                        student.valid = False
                        student.erreurs.append('date incorrect')
        # Si on arrive pas à parser la date et avoir 3 valeur: jour, mois, annee , la date est invalide
            else:
                student.valid = False
                student.erreurs.append('date incorrect')





