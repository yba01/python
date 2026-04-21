from prettytable import PrettyTable
from utils.data_reader import FileReader
import os
class GestionDonnees:
    file_reader = FileReader()
    file_reader.readfile("/home/yba/Downloads/Personal Exercices/python-exercices/POO/student_management/data/Donnees_Projet_Python_Dev_Data.csv")
    file_reader.create_students(';')
    liste_etudiants = file_reader.students
    valides = []
    
    def valid_students(self):
        for etudiant in self.liste_etudiants:
            if etudiant.valid:
                self.valides.append(etudiant)

    def affichage_valid(self):
        self.valid_students()
        table = PrettyTable(['code', 'prenom', 'nom', 'date', 'classe', 'ang', 'fr', 'hg', 'math', 'pc', 'svt'])
        for etudiant in self.valides:
            etudiant.afficher_valid(table)
        os.system('clear')    
        print(table)

    def affichage_invalid(self):
        table = PrettyTable(['numero', 'prenom', 'nom', 'erreurs'])
        for etudiant in self.liste_etudiants:
            if not etudiant.valid:
                etudiant.afficher_invalid_error(table)
        os.system('clear')
        print(table)

    def affichage_cinq(self):
        table = PrettyTable(['numero', 'prenom', 'nom', 'date', 'classe', 'valid', 'erreurs'])
        for etudiant in self.liste_etudiants[:5]:
            if not etudiant.valid:
                etudiant.afficher_info(table)
        os.system('clear')
        print(table)

    def recherche_par_numero(self, numero):
        table = PrettyTable(['numero', 'prenom', 'nom', 'date', 'classe', 'valid', 'erreurs'])
        for student in self.liste_etudiants:
            if student.numero == numero:
                student.afficher_info(table)
                os.system('clear')
                print(table)
                break
        else:
            print('Ce numero ne correspond à aucun etudiant.')

    def recherche_par_code(self, code):
        table = PrettyTable(['numero', 'prenom', 'nom', 'date', 'classe', 'valid', 'erreurs'])
        valid = 0
        invalid = 0
        for student in self.liste_etudiants:
            if student.code == code:
                student.afficher_info(table)
                if student.valid:
                    valid += 1
                else:
                    invalid += 1
        if valid + invalid == 0 :
            print('Ce code ne correspond à aucun etudiant')
            return
        
        percentage = (valid / (valid + invalid)) * 100

        stat = PrettyTable(['statistics', ''])
        stat.add_row(['valid', f'{percentage:.2f}%'])
        stat.add_row(['invalid', f'{(100-percentage):.2f}%'])

        os.system('clear')
        print(table)
        print()
        print(stat)




