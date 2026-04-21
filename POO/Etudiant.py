class Etudiant:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.notes = []

    
    def afficher_info(self):
        print(f"L'etudiant {self.prenom} {self.nom} a {self.age} ans")

    def ajouter_note(self, notes):
        try:
            for note in notes:
                if 0<=float(note)<=20:
                    self.notes.append(float(note))
        except:
            print('Error: Wrong value entered!!!')
    
    def calculer_moyenne(self):
        if self.notes:
            return sum(self.notes)/len(self.notes)



