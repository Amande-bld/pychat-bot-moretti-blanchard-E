import os
def list_of_files(directory, extension):
    files_names=[]
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            files_names.append(file_name)
    return files_names  # Retourne une liste des fichiers avec leur chemin d'acces complet

def extractions_name (files_names):
    lastnames_clean = []
    for name in files_names :
        name = name.split("_")[-1]  # Récupère uniquement la partie après Nomination_
        name = name[:-4]  # Enleve l'extension (.txt)
       name_mod =""
       for car in name :
           if car != '1' and car != '2':  # Vérifie que chaque carctère restant est diffèrent de 1 ou 2  pour obtenir le noms sans carctère superflu
                name_mod += car
       lastnames_clean.append(name_mod)
    return lastnames_clean  #Retourne une liste comportant uniquement les noms de familles des Présidents de la République


def association_lastname_firstname(lastnames_clean):
    dictionary_president = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François',
                            'Macron': 'Emmanuel',
               'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    for name in lastnames_clean:
        name = dictionary_president[name] + ' ' + name
    return dictionary_president  # retourne un dictionnaire associant la clé (nom de famille du président ) a son prénom


def display_list_president(dictionary_president):
    for name in dictionary_president.keys():  # Permet d'accèder uniquement aux clé du dictionnaire
        print(name)

def convert_file_lower_case(files_names,directory):
    for file_name in files_names :
        # Création chemin d'acces du fichier 
        input_file_path = directory + '/' + file_name
        # Ouverture fichier 
        with open(input_file_path,'r') as content:
            #Création chemin ou sera rangé le fichier modifier 
            output_file_path = "./cleaned" + '/' + file_name + "copie.txt"
            #Ouverture fichie copie
            with open(output_file_path, 'a') as copy:
                # modification des majusucles en miniscule 
                line = content.readline()
                while line != '':
                    line_mod =''
                    for car in line :
                        if car >= 'A' and car <= 'Z':
                            car = chr(ord(car)+ 32 )
                        line_mod += car
                    # Ligne transformer en minuscule réecrite dans la copie 
                    copy.write(line_mod)
                    line = content.readline()


def replacement_punctuation_(files_names):
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f1:
            content = f1.read()
            # définition des caractères de ponctuations
            punctuation_character = ',;:.?!""()[]*/'
            text_clean = ''
            for car in content:
                if car in punctuation_character:
                    text_clean += ' '
                elif car == "'" or car == "-":
                    text_clean += ' '
                else:
                    text_clean += car
        with open(input_file_path, "w") as file_clean:
            file_clean.write(text_clean)  # Réecriture du texte sans ponctuaction dans le même fichier


#Le mot text est à remplacer par le nom du fichier
def word_occurrences_tf(text):
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


import math


def idf(files_names):
    nb_files = 0
    occurence_word_all_files = {}
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()

            # Obtention du dictionnaire associant un mot au nombre de fois ou il apparait dans le fichier
            occurence_files = word_occurrences_tf(content)
            nb_files = nb_files + 1

            # Nous parcourons ensuite ce dictionnaire obtenus pour un fichier
            for (word, occurence) in occurence_files.items():
                if word in occurence_word_all_files:
                    # Si le mot existe deja dans le dictionnaire regroupant tous les mots des fichiers on rajoute +1 a son compteur
                    occurence_word_all_files[word] += 1
                    # Sinon le mots n'existe pas déjà dans le dictionnaire alors on l'ajoute et on initialise son compteur a 1
                else:
                    occurence_word_all_files[word] = 1

            # Apres avoir parcourus tous les fichier occurence totale représente un dictionnaire contenant tous les mots possible dans les fichiers avec le nombre de fois qu'il apparraissent dans ces documents
    occurrence_idf = {}
    for (word, occurence) in occurence_word_all_files.items():
        # Associe pour chaque mot son score IDF en faisant le logarithme du nombre de fichier / le nombre de fois qu'il apparait dans un fichier
        occurrence_idf[word] = math.log((nb_files / (occurence)) + 1)
    return occurrence_idf  # retourne un dictionnaire qui a chaque mots associe son score idf.
