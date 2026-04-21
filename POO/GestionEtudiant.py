import Etudiant
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
            # the_best = self.liste_etudiants[0]
            # for student in self.liste_etudiants[1:]:
            #     if student.calculer_moyenne()>the_best.calculer_moyenne():
            #         the_best = student
            # return the_best
            return max([(std.calculer_moyenne(), std) for std in self.liste_etudiants  ])
        except:
            return None


    def moyenne_class(self):
        return sum([student.calculer_moyenne() for student in self.liste_etudiants])/len(self.liste_etudiants)


