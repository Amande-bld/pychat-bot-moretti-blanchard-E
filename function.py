import os

def list_of_files(directory, extension):
    files_names=[]
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            files_names.append(file_name)
    return files_names


def extractions_name (files_names):
    names_good = []
    for name in files_names :
       name = name.split("_")[-1]
       name = name[:-4]
       name_mod =""
       for car in name :
            if car != '1' and car != '2' :
                name_mod += car
       names_good.append(name_mod)
    return names_good


def association_prénom(names_good):
    prénoms = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel',
               'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    for name in names_good:
        name = prénoms[name] + ' ' + name
        print(name)
    return prénoms

#Le mot text est à remplacer par le nom du fichier

def word_occurrences(text):
    # Initialiser un dictionnaire pour stocker les occurrences de mots
    word_count = {}

    # Diviser le discours en série de mots
    words = text.split()

    # Compter la fréquence de chaque mot
    for word in words:
        # Mettre à jour le dictionnaire à chaque fréquence.
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count
