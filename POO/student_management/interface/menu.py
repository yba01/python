from services.gestion_donnees import GestionDonnees
import os
class Menu:
    gest = GestionDonnees()

    def afficher_menu(self):
        print(f"1-  Afficher\n2-  Ajouter\n3-  Modifier\n4-  Rechercher\n5-  Quitter")
        choix = input(':')
        match choix:
            case '1':
                self.affichage()
            case '2':
                self.ajouter()
            case '3':
                self.modifier()
            case '4':
                self.rechercher()
            case '5':
                os.system('clear')
                return
            case _:
                os.system('clear')
                self.afficher_menu()


    def affichage(self):
        os.system('clear')
        print(f"1-  Afficher donnees valides\n2-  Afficher donnees invalides\n3-  Afficher un etudiant\n4-  Afficher 5 premiers donnees\n5-  Quitter")
        choix = input(':')
        match choix:
            case '1':
                self.gest.affichage_valid()
            case '2':
                self.gest.affichage_invalid()
            case '3':
                numero = input("Entrer le numero de l'etudiant: ")
                self.gest.recherche_par_numero(numero)
            case '4':
                self.gest.affichage_cinq()
            case '5':
                os.system('clear')
                return
            case _:
                os.system('clear')
                self.affichage()

            
    def rechercher(self):
        os.system('clear')
        print(f"1-  Numero\n2-  Code\n3-  Quitter")
        choix = input(':')
        match choix:
            case '1':
                numero = input("Entrer le numero de l'etudiant: ")
                self.gest.recherche_par_numero(numero)
            case '2':
                code = input("Entrer le code des etudiants: ")
                self.gest.recherche_par_code(code)
            case '3':
                os.system('clear')
                return
            case _:
                os.system('clear')
                self.rechercher()

    def ajouter(self):
        pass

    def modifier(self):
        pass

