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


    # Fonctionalité 1 permettant de trouver les mots les moins importants
def score_tdf_idf_nulle(tf_idf_transposed, words_list):
    mots_non_importants = []

    for i in range(len(words_list)):
        # Vérifie si le TD-IDF est égal à 0 pour tous les fichiers
        td_idf_zero = True
        j = 0
        while j < len(tf_idf_transposed[i]) and td_idf_zero:
            if tf_idf_transposed[i][j] != 0:
                td_idf_zero = False
            j += 1

        if td_idf_zero:
            mots_non_importants.append(words_list[i])

    return mots_non_importants

#Foonctionalité 2 permettant d'obtenir les mots avec le score + eleve

"""def most_important_word(files_names, tf_idf_matrix, words_list):
    unique_words_set = set()

    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()
            words = content.split()
            unique_words_set.update(words)

    unique_words_list = list(unique_words_set)
    most_important_words = []

    for i in range(len(tf_idf_matrix[0])):
        max_score = 0
        most_important_word = None
        for j in range(len(tf_idf_matrix)):
            if tf_idf_matrix[j][i] > max_score:
                max_score = tf_idf_matrix[j][i]
                most_important_word = unique_words_list[j]

        if most_important_word is not None:
            most_important_words.append(most_important_word)

    return most_important_words """




#Fonctionalité 3

def word_occurrences_tf_per_president(files_names, president_last_name):
    word_count = {}

    for file_name in files_names:
        if president_last_name.lower() in file_name.lower():
            input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
            with open(input_file_path, 'r') as f:
                content = f.read()
                tf_scores = word_occurrences_tf(content)

                for word, count in tf_scores.items():
                    if word in word_count:
                        word_count[word] += count
                    else:
                        word_count[word] = count

    return word_count

def list_trié(president_word_occurrences):
    most_repeated_words = []
    sorted_president_word_occurrences = list(president_word_occurrences.items())


    for i in range(len(sorted_president_word_occurrences)):
        for j in range(i + 1, len(sorted_president_word_occurrences)):
            if sorted_president_word_occurrences[j][1] > sorted_president_word_occurrences[i][1]:
                sorted_president_word_occurrences[i], sorted_president_word_occurrences[j] = \
                sorted_president_word_occurrences[j], sorted_president_word_occurrences[i]

    for i in range(len(sorted_president_word_occurrences)):
        most_repeated_words.append(sorted_president_word_occurrences[i][0])

    return most_repeated_words



def first_president_to_mention_topic(files_names, target_words):
    first_mention = {}

    for president_last_name in ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']:
        for file_name in files_names:
            if president_last_name.lower() in file_name.lower():
                input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
                with open(input_file_path, 'r') as f:
                    content = f.read().lower()

                    # Vérifier si le discours mentionne le thème
                    for word in target_words:
                        if word in content:
                            if president_last_name not in first_mention:
                                first_mention[president_last_name] = file_name

    return first_mention # Retourne un dictionnaire qui a pour clé le nom de famille de president et comme valeur son nom de fichier

def common_important_words_across_presidents(files_names, non_important_words):
    president_words_dict = {}


    presidents_to_consider = ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']


    for president_last_name in presidents_to_consider:
        president_words_dict[president_last_name] = []


    for president_last_name in presidents_to_consider:
        for file_name in files_names:

            if president_last_name.lower() in file_name.lower():

                input_file_path = "./cleaned" + '/' + file_name + "copie.txt"

                with open(input_file_path, 'r') as f:
                    content = f.read()

                    words = content.split()
                    filtered_words = []
                    for word in words:
                        if word not in non_important_words:
                            filtered_words.append(word)
                    for word in filtered_words:
                            president_words_dict[president_last_name].append(word)

    common_important_words = set()
    for word in president_words_dict[presidents_to_consider[0]]:
        common_important_words = set(list(common_important_words) + [word])  # Utiliser une liste puis convertir en ensemble

    # Filtrer les mots communs avec les ensembles de mots des présidents suivants avec une boucle explicite
    for president_last_name in presidents_to_consider[1:]:
        current_president_words = set()
        for word in president_words_dict[president_last_name]:
            current_president_words = set(
                list(current_president_words) + [word])  # Utiliser une liste puis convertir en ensemble

        # Garder uniquement les mots communs avec une boucle explicite
        common_important_words_temp = set()
        for word in common_important_words:
            if word in current_president_words:
                common_important_words_temp = set(list(common_important_words_temp) + [word])  # Utiliser une liste puis convertir en ensemble

        common_important_words = common_important_words_temp

    return common_important_words
