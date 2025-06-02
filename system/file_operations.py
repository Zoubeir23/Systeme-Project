import os
import shutil
from pathlib import Path
import re

def valider_chemin(chemin):
    try:
        if not chemin or chemin.isspace():
            print("  Erreur : Le chemin ne peut pas être vide.")
            return None
            
        # Vérification des caractères interdits dans les noms de fichiers Windows
        caracteres_interdits = r'[<>:"/\\|?*]'
        if re.search(caracteres_interdits, chemin):
            print("  Erreur : Le chemin contient des caractères interdits (< > : \" / \\ | ? *)")
            return None
            
        # Vérification de la longueur maximale du chemin
        if len(chemin) > 260:  # Limite Windows
            print("  Erreur : Le chemin est trop long (maximum 260 caractères)")
            return None
            
        return os.path.abspath(chemin)
    except Exception as e:
        print(f"  Erreur : Format de chemin invalide - {str(e)}")
        return None

def valider_confirmation(reponse):
    while True:
        if reponse.lower() in ['o', 'n', 'oui', 'non']:
            return reponse.lower() in ['o', 'oui']
        print("  Erreur : Veuillez répondre par 'o' ou 'oui' pour oui, 'n' ou 'non' pour non.")
        reponse = input("Votre réponse (o/n) : ").strip()

def valider_chemin_source(chemin):
    if not os.path.exists(chemin):
        print(f"  Erreur : Le chemin '{chemin}' n'existe pas.")
        return False
    return True

def valider_chemin_destination(chemin):
    if os.path.exists(chemin):
        print(f"  Attention : Le chemin '{chemin}' existe déjà.")
        if os.path.isfile(chemin):
            print(f"  Type : Fichier")
        elif os.path.isdir(chemin):
            print(f"  Type : Dossier")
        return valider_confirmation(input("Voulez-vous écraser l'élément existant ? (o/n) : "))
    return True

def valider_espace_disque(chemin_source, chemin_dest):
    try:
        if os.path.isfile(chemin_source):
            taille_source = os.path.getsize(chemin_source)
            espace_dispo = shutil.disk_usage(os.path.dirname(chemin_dest)).free
            if taille_source > espace_dispo:
                print(f"  Erreur : Espace disque insuffisant.")
                print(f"  Taille du fichier : {taille_source / (1024*1024):.2f} MB")
                print(f"  Espace disponible : {espace_dispo / (1024*1024):.2f} MB")
                return False
    except Exception as e:
        print(f"  Erreur lors de la vérification de l'espace disque : {str(e)}")
        return False
    return True

def formater_taille(taille_octets):
    for unite in ['B', 'KB', 'MB', 'GB']:
        if taille_octets < 1024:
            return f"{taille_octets:.2f} {unite}"
        taille_octets /= 1024
    return f"{taille_octets:.2f} TB"

def afficher_info_fichier(chemin):
    try:
        stats = os.stat(chemin)
        print(f"\n  Informations sur le fichier :")
        print(f"  Taille : {formater_taille(stats.st_size)}")
        print(f"  Dernière modification : {stats.st_mtime}")
        print(f"  Permissions : {oct(stats.st_mode)[-3:]}")
    except Exception as e:
        print(f"  Erreur lors de l'affichage des informations : {str(e)}")

def creer_dossier():
    while True:
        nom = input("Nom du dossier à créer : ").strip()
        chemin = valider_chemin(nom)
        if not chemin:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue
        
        if not os.path.exists(chemin):
            try:
                os.makedirs(chemin)
                print(f"  Le dossier '{nom}' a été créé avec succès.")
                break
            except PermissionError:
                print("  Erreur : Permission refusée pour créer le dossier.")
                print("  Vérifiez vos droits d'accès au dossier parent.")
            except Exception as e:
                print(f"  Erreur lors de la création du dossier : {str(e)}")
        else:
            print(f"  Le dossier '{nom}' existe déjà.")
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre nom ? (o/n) : ")):
                break

def lister_fichiers():
    while True:
        dossier = input("Entrez le nom du dossier pour lister les fichiers : ").strip()
        chemin = valider_chemin(dossier)
        if not chemin:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if os.path.exists(chemin):
            try:
                fichiers = os.listdir(chemin)
                if fichiers:
                    print(f"\n  Contenu du dossier '{dossier}':")
                    total_taille = 0
                    for f in fichiers:
                        chemin_complet = os.path.join(chemin, f)
                        type_fichier = "📁" if os.path.isdir(chemin_complet) else "📄"
                        taille = os.path.getsize(chemin_complet) if os.path.isfile(chemin_complet) else 0
                        total_taille += taille
                        print(f"{type_fichier} {f} ({formater_taille(taille)})")
                    print(f"\n  Taille totale : {formater_taille(total_taille)}")
                else:
                    print("  Le dossier est vide.")
                break
            except PermissionError:
                print("  Erreur : Permission refusée pour accéder au dossier.")
                print("  Vérifiez vos droits d'accès.")
            except Exception as e:
                print(f"  Erreur lors de la lecture du dossier : {str(e)}")
        else:
            print(f"  Le dossier '{dossier}' n'existe pas.")
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin ? (o/n) : ")):
                break

def supprimer_fichier():
    while True:
        fichier = input("Entrez le nom du fichier à supprimer : ").strip()
        chemin = valider_chemin(fichier)
        if not chemin:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if os.path.exists(chemin):
            if os.path.isfile(chemin):
                afficher_info_fichier(chemin)
                if valider_confirmation(input(f"Êtes-vous sûr de vouloir supprimer '{fichier}' ? (o/n) : ")):
                    try:
                        os.remove(chemin)
                        print(f"  Le fichier '{fichier}' a été supprimé.")
                        break
                    except PermissionError:
                        print("  Erreur : Permission refusée pour supprimer le fichier.")
                        print("  Vérifiez si le fichier n'est pas utilisé par un autre programme.")
                    except Exception as e:
                        print(f"  Erreur lors de la suppression du fichier : {str(e)}")
                else:
                    print("  Suppression annulée.")
                    break
            else:
                print(f"  '{fichier}' n'est pas un fichier.")
                if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin ? (o/n) : ")):
                    break
        else:
            print(f"  Le fichier '{fichier}' n'existe pas.")
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin ? (o/n) : ")):
                break

def supprimer_dossier():
    while True:
        dossier = input("Entrez le nom du dossier à supprimer : ").strip()
        chemin = valider_chemin(dossier)
        if not chemin:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if os.path.exists(chemin):
            if os.path.isdir(chemin):
                try:
                    taille_totale = 0
                    nb_fichiers = 0
                    for root, dirs, files in os.walk(chemin):
                        for file in files:
                            taille_totale += os.path.getsize(os.path.join(root, file))
                            nb_fichiers += 1
                    
                    print(f"\n  Informations sur le dossier :")
                    print(f"  Nombre de fichiers : {nb_fichiers}")
                    print(f"  Taille totale : {formater_taille(taille_totale)}")
                    
                    if valider_confirmation(input(f"Êtes-vous sûr de vouloir supprimer le dossier '{dossier}' et tout son contenu ? (o/n) : ")):
                        shutil.rmtree(chemin)
                        print(f"  Le dossier '{dossier}' et son contenu ont été supprimés.")
                        break
                    else:
                        print("  Suppression annulée.")
                        break
                except PermissionError:
                    print("  Erreur : Permission refusée pour supprimer le dossier.")
                    print("  Vérifiez vos droits d'accès et si aucun fichier n'est utilisé.")
                except Exception as e:
                    print(f"  Erreur lors de la suppression du dossier : {str(e)}")
            else:
                print(f"  '{dossier}' n'est pas un dossier.")
                if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin ? (o/n) : ")):
                    break
        else:
            print(f"  Le dossier '{dossier}' n'existe pas.")
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin ? (o/n) : ")):
                break

def copier_fichier():
    while True:
        source = input("Entrez le chemin du fichier source à copier : ").strip()
        chemin_source = valider_chemin(source)
        if not chemin_source:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if not valider_chemin_source(chemin_source):
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin source ? (o/n) : ")):
                break
            continue

        if not os.path.isfile(chemin_source):
            print(f"  '{source}' n'est pas un fichier.")
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin source ? (o/n) : ")):
                break
            continue

        destination = input("Entrez le chemin de destination : ").strip()
        chemin_dest = valider_chemin(destination)
        if not chemin_dest:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if not valider_chemin_destination(chemin_dest):
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin de destination ? (o/n) : ")):
                break
            continue

        if not valider_espace_disque(chemin_source, chemin_dest):
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin de destination ? (o/n) : ")):
                break
            continue

        try:
            shutil.copy(chemin_source, chemin_dest)
            print(f"  Fichier copié de '{source}' à '{destination}'.")
            break
        except PermissionError:
            print("  Erreur : Permission refusée pour copier le fichier.")
            print("  Vérifiez vos droits d'accès et si le fichier n'est pas utilisé.")
        except Exception as e:
            print(f"  Erreur lors de la copie du fichier : {str(e)}")

def deplacer_fichier():
    while True:
        source = input("Entrez le chemin du fichier à déplacer : ").strip()
        chemin_source = valider_chemin(source)
        if not chemin_source:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if not valider_chemin_source(chemin_source):
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin source ? (o/n) : ")):
                break
            continue

        if not os.path.isfile(chemin_source):
            print(f"  '{source}' n'est pas un fichier.")
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin source ? (o/n) : ")):
                break
            continue

        destination = input("Entrez le chemin de destination : ").strip()
        chemin_dest = valider_chemin(destination)
        if not chemin_dest:
            if not valider_confirmation(input("Voulez-vous réessayer ? (o/n) : ")):
                break
            continue

        if not valider_chemin_destination(chemin_dest):
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin de destination ? (o/n) : ")):
                break
            continue

        if not valider_espace_disque(chemin_source, chemin_dest):
            if not valider_confirmation(input("Voulez-vous réessayer avec un autre chemin de destination ? (o/n) : ")):
                break
            continue

        try:
            shutil.move(chemin_source, chemin_dest)
            print(f"  Fichier déplacé de '{source}' à '{destination}'.")
            break
        except PermissionError:
            print("  Erreur : Permission refusée pour déplacer le fichier.")
            print("  Vérifiez vos droits d'accès et si le fichier n'est pas utilisé.")
        except Exception as e:
            print(f"  Erreur lors du déplacement du fichier : {str(e)}") 