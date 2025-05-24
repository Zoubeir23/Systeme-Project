# Système de Gestion de Fichiers et Dossiers

## Auteur
Développé par [Zoubeir23](https://github.com/Zoubeir23)  
Contact : Zoubeiribrahima@gmail.com

## Description
Ce projet est un système de gestion de fichiers et dossiers en ligne de commande, développé en Python. Il permet la création, la suppression, la copie, le déplacement et le listage de fichiers et dossiers avec gestion des erreurs.

## Fonctionnalités

1. **Création de dossiers**
   - Création de nouveaux dossiers avec validation des chemins
   - Gestion des erreurs de permissions

2. **Listage des fichiers**
   - Affichage du contenu des dossiers
   - Distinction visuelle entre fichiers (📄) et dossiers (📁)

3. **Suppression de fichiers**
   - Suppression sécurisée avec confirmation
   - Validation du type de fichier

4. **Suppression de dossiers**
   - Suppression récursive avec confirmation
   - Gestion des erreurs de permissions

5. **Copie de fichiers**
   - Copie de fichiers vers une destination
   - Validation des chemins source et destination

6. **Déplacement de fichiers**
   - Déplacement de fichiers vers une nouvelle location
   - Gestion des erreurs de permissions

## Structure du Projet

```
Systeme-Project/
├── main.py               # Point d'entrée du programme
├── system/               # Package principal
│   ├── __init__.py       # Fichier d'initialisation du package
│   ├── main.py           # Logique du menu principal
│   └── file_operations.py # Fonctions de gestion des fichiers
└── README.md             # Documentation du projet
```

## Installation

1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Clonez ce dépôt ou téléchargez les fichiers.
3. Aucune dépendance externe n'est requise.

## Utilisation

Pour lancer le programme :

```bash
python main.py
```

Suivez les instructions du menu pour :
- Créer des dossiers
- Lister le contenu des dossiers
- Supprimer des fichiers ou dossiers
- Copier des fichiers
- Déplacer des fichiers

## Gestion des Erreurs

Le système gère plusieurs types d'erreurs :
- Chemins invalides
- Permissions insuffisantes
- Fichiers/dossiers inexistants
- Opérations annulées par l'utilisateur

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT.

### Qu'est-ce que la licence MIT ?

La licence MIT est une licence de logiciel libre très permissive qui permet :

- ✅ Utilisation commerciale
- ✅ Modification
- ✅ Distribution
- ✅ Utilisation privée

Avec les conditions suivantes :
- La licence et le copyright doivent être inclus dans toutes les copies ou parties substantielles du logiciel
- Le logiciel est fourni "tel quel", sans garantie d'aucune sorte

En termes simples, vous pouvez :
- Utiliser ce code dans vos projets personnels ou commerciaux
- Modifier le code comme vous le souhaitez
- Distribuer des copies modifiées
- L'utiliser dans des projets privés

La seule exigence est de conserver la notice de copyright et la licence MIT dans votre code.

Pour plus d'informations, consultez le texte complet de la [licence MIT](https://opensource.org/licenses/MIT).
