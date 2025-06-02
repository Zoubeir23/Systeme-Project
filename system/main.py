from system.file_operations import *

def valider_choix_menu(choix):
    try:
        choix_int = int(choix)
        if 1 <= choix_int <= 7:
            return True
        return False
    except ValueError:
        return False

def menu():
    while True:
        print("\n  Menu de Gestion des Fichiers et Dossiers")
        print("1. Créer un dossier")
        print("2. Lister les fichiers dans un dossier")
        print("3. Supprimer un fichier")
        print("4. Supprimer un dossier")
        print("5. Copier un fichier")
        print("6. Déplacer un fichier")
        print("7. Quitter")
        
        while True:
            choix = input("Choisissez une option (1-7): ")
            if valider_choix_menu(choix):
                break
            print("  Erreur : Veuillez entrer un nombre entre 1 et 7.")
        
        if choix == "1":
            creer_dossier()
        elif choix == "2":
            lister_fichiers()
        elif choix == "3":
            supprimer_fichier()
        elif choix == "4":
            supprimer_dossier()
        elif choix == "5":
            copier_fichier()
        elif choix == "6":
            deplacer_fichier()
        elif choix == "7":
            print("  À la prochaine!")
            break 