class Etudiant:
    def __init__(self, code, numero, nom, prenom, date, classe, note):
        self.code = code
        self.numero = numero
        self.prenom = prenom
        self.nom = nom
        self.date = date
        self.classe = classe
        self.note = note
        self.valid = True
        self.erreurs = []

    def __str__(self):
        return f"prenom: {self.prenom} nom: {self.nom} notes: "


    def afficher_info(self, table):
        table.add_row([self.numero, self.prenom, self.nom, self.date, self.classe, self.valid])

    def afficher_invalid_error(self, table):
        table.add_row([self.numero, self.prenom, self.nom, '-'.join(self.erreurs)])

    def afficher_valid(self, table):
        self.note.sort(key=lambda note: note.matiere)
        row = [self.code, self.prenom, self.nom, self.date, self.classe]
        row.extend([note.mean() for note in self.note])
        table.add_row(row)




    