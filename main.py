from file_manager import FileManager

def main():
    file_path = 'log.txt'  # Chemin vers le fichier log.txt
    file_manager = FileManager(file_path)

    while True:
        print("\n=== Menu ===")
        print("1 - Lecture de fichiers")
        print("2 - Écriture dans des fichiers")
        print("3 - Ajout de contenu à des fichiers")
        print("4 - Recherche de mots-clés")
        print("5 - Informations sur le fichier")
        print("0 - Quitter")

        choice = input("Veuillez sélectionner une option (0-5): ")

        if choice == '1':
            print("\n=== Contenu du fichier ===")
            print(file_manager.read_file())

        elif choice == '2':
            content = input("Entrez le contenu à écrire dans le fichier : ")
            file_manager.write_file(content)
            print("Contenu écrit dans le fichier.")

        elif choice == '3':
            content = input("Entrez le contenu à ajouter au fichier : ")
            file_manager.append_to_file(content)
            print("Contenu ajouté au fichier.")

        elif choice == '4':
            keyword = input("Entrez le mot-clé à rechercher : ")
            results = file_manager.search_keyword(keyword)
            print("\n=== Lignes contenant '{}' ===".format(keyword))
            if isinstance(results, list):
                for line in results:
                    print(line.strip())
            else:
                print(results)

        elif choice == '5':
            print("\n=== Informations sur le fichier ===")
            print(file_manager.file_info())

        elif choice == '0':
            print("Au revoir!")
            break

        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
