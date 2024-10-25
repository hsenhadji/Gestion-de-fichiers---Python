
# Gestionnaire de Fichiers en Python

Ce projet est une application en Python permettant de gérer un fichier de logs, incluant la lecture, l'écriture, la recherche de mots-clés et la suppression d'entrées. Elle permet d'ajouter des lignes au fichier, de rechercher des mots-clés, et d'afficher des informations sur le fichier.

## Auteur

- HAMZA SENHADJI

---

## Table des Matières
1. [Fonctionnalités](#fonctionnalités)
2. [Structure du Projet](#structure-du-projet)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Prérequis](#prérequis)

---

## Fonctionnalités

- **Lecture de fichiers** : Affiche le contenu complet du fichier de logs.
- **Écriture et ajout d'entrées** : Ajoute de nouvelles lignes au fichier.
- **Recherche de mots-clés** : Recherche les lignes contenant un mot-clé spécifique.
- **Suppression d'entrées** : Supprime toutes les lignes contenant un mot-clé donné.
- **Comptage de lignes** : Affiche le nombre total de lignes du fichier.
- **Affichage d'informations sur le fichier**.

---

## Structure du Projet

### 1. `file_manager.py`
Ce fichier contient la classe `FileManager`, qui gère toutes les interactions avec le fichier de logs (`log.txt`).

#### Méthodes de `FileManager`
- `__init__(self, file_path)` : Initialise le gestionnaire avec le chemin du fichier.
- `read_file()` : Lit et retourne le contenu du fichier sous forme de liste.
- `write_to_file(data)` : Ajoute une nouvelle entrée dans le fichier de logs.
- `count_lines()` : Retourne le nombre total de lignes.
- `search_keyword(keyword)` : Retourne les lignes contenant le mot-clé spécifié.
- `delete_entries(keyword)` : Supprime les lignes contenant le mot-clé spécifié.

### 2. `main.py`
Un fichier de script pour tester directement les fonctionnalités de `FileManager`.

### 3. `log.txt`
Le fichier de logs où toutes les entrées sont enregistrées. Ce fichier doit être dans le même répertoire que le projet.

---

## Installation

1. Clonez ce dépôt ou téléchargez-le sur votre machine :
   ```bash
   git clone https://github.com/hsenhadji/Gestion-de-fichiers---Python.git
   ```
2. Créez un environnement virtuel :
   ```bash
   python3 -m venv Projet
   ```
3. Activez l'environnement virtuel :
   ```bash
   Projet\Scripts\activate  # Sous Windows
   source Projet/bin/activate  # Sous macOS/Linux
   ```
4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

1. Modifiez le fichier `log.txt` pour ajouter ou visualiser des entrées.
2. Exécutez le script principal pour accéder aux fonctionnalités :
   ```bash
   python main.py
   ```

---

## Prérequis

- Python 3.x
