class Etudiant:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.notes = []

    
    def afficher_info(self):
        print(f"L'etudiant {self.prenom} {self.nom} a {self.age} ans")

    def ajouter_note(self, *notes):
        try:
            for note in notes:
                if 0<=note<=20:
                    self.notes.append(note)
        except:
            print('Error: Wrong value entered!!!')
    
    def calculer_moyenne(self):
        if self.notes:
            return sum(self.notes)/len(self.notes)



class GestionEtudiant:
    def __init__(self):
        self.liste_etudiants = []

    def ajouter_etudiant(self, etudiant):
        try:
            if isinstance(etudiant, Etudiant):
                self.liste_etudiants.append(etudiant)
        except:
            print("Error: The argument isn't a Etudiant object")

    def afficher_etudiant(self):
        for student in self.liste_etudiants:
            student.afficher_info()

    def meilleur_etudiant(self):
        try:
            the_best = self.liste_etudiants[0]
            for student in self.liste_etudiants[1:]:
                if student.calculer_moyenne()>the_best.calculer_moyenne():
                    the_best = student
            return the_best
        except:
            return None


    def moyenne_class(self):
        return sum([student.calculer_moyenne() for student in self.liste_etudiants])/len(self.liste_etudiants)





yero = Etudiant('BA', 'Yero', 26)
abdou = Etudiant('Tiaw', 'Abdou', 23)

yero.afficher_info()
abdou.afficher_info()
yero.ajouter_note(12)
yero.ajouter_note(15)
print(yero.calculer_moyenne())



# g = GestionEtudiant()
# g.ajouter_etudiant('a')
# g.ajouter_etudiant(yero)
# g.ajouter_etudiant(abdou)
# g.afficher_etudiant()