import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Lit le contenu du fichier et le retourne."""
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "Fichier non trouvé."

    def write_file(self, content):
        """Écrit du contenu dans le fichier. Si le fichier n'existe pas, il est créé."""
        with open(self.file_path, 'w') as file:
            file.write(content)

    def append_to_file(self, content):
        """Ajoute du contenu à la fin du fichier."""
        with open(self.file_path, 'a') as file:
            file.write(content)

    def search_keyword(self, keyword):
        """Recherche un mot-clé dans le fichier et retourne les lignes qui le contiennent."""
        if not os.path.exists(self.file_path):
            return "Fichier non trouvé."

        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        matched_lines = [line for line in lines if keyword in line]
        return matched_lines if matched_lines else f"'{keyword}' non trouvé dans le fichier."

    def file_info(self):
        """Retourne des informations sur le fichier comme sa taille et s'il existe."""
        if not os.path.exists(self.file_path):
            return "Fichier non trouvé."
        
        file_size = os.path.getsize(self.file_path)
        return f"Le fichier {self.file_path} existe et a une taille de {file_size} octets."
