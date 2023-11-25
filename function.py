import os
def list_of_files(directory, extension):
    files_names=[]
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            files_names.append(file_name)
    return files_names

def extractions_name (files_names):
    lastnames_clean = []
    for name in files_names :
       name = name.split("_")[-1]
       name = name[:-4]
       name_mod =""
       for car in name :
            if car != '1' and car != '2' :
                name_mod += car
       lastnames_clean.append(name_mod)
    return lastnames_clean


def association_lastname_firstname(lastnames_clean):
    dictionary_president = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François',
                            'Macron': 'Emmanuel',
               'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    for name in lastnames_clean:
        name = dictionary_president[name] + ' ' + name
    return dictionary_president


def display_list_president(dictionary_president):
    for name in dictionary_president.keys():
        print(name)


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
