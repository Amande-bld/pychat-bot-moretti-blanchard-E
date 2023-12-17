import math
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
        # Enleve l'extension (.txt)
        name = name[:-4]
        name_mod = ""
        for car in name:
           if car != '1' and car != '2':  # Vérifie que chaque carctère restant est diffèrent de 1 ou 2  pour obtenir le noms sans carctère superflu
                name_mod += car
        lastnames_clean.append(name_mod)
    return lastnames_clean  #Retourne une liste comportant uniquement les noms de familles des Présidents de la République


def association_lastname_firstname(lastnames_clean):
    dictionary_president = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François',
                            'Macron': 'Emmanuel', 'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    for name in lastnames_clean:
        name = dictionary_president[name] + ' ' + name
    return dictionary_president  # Retourne un dictionnaire associant la clé (nom de famille du président ) a son prénom


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
            with open(output_file_path, 'w') as copy:
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
            # Verification des caractères un par un
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
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def idf(files_names):

    # Dictionnaire pour stocker le nombre de documents contenant chaque mot
    documents_containing_word = {}

    # Nombre total de documents
    total_documents = len(files_names)

    # Compter le nombre de documents contenant chaque mot
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()

            occurrence_files = word_occurrences_tf(content)

            for word in occurrence_files.keys():
                if word in documents_containing_word:
                    documents_containing_word[word] += 1
                else:
                    documents_containing_word[word] = 1
        print(documents_containing_word)

    # Calculer l'IDF pour chaque mot
    idf_scores = {}
    for word, doc_count in documents_containing_word.items():
        idf_scores[word] = math.log10(total_documents / (doc_count))
    return idf_scores


def TD_IDF(files_names: str) -> list[list]:
    tf_idf = []
    idf_scores = idf(files_names)

    tf_idf_row = []
    for word in idf_scores.keys():
        tf_idf_row.append(word)
    tf_idf.append(tf_idf_row)

    for file_name in files_names:
        input_files_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_files_path, 'r') as f:
            content = f.read()

            # récupère dico tf associant a chaque mot du fichier le nombre de fois qu'il apparait

            tf_scores = word_occurrences_tf(content)

            tf_idf_row = []
            for word in idf_scores.keys():

                if word in tf_scores:
                    tf_score = tf_scores[word]
                else:
                    tf_score = 0
                idf_score = idf_scores[word]
                tf_idf_row.append(round(idf_score * tf_score, 2))
            tf_idf.append(tf_idf_row)

    # Transpositionde la matrice
    tf_idf_transposed = matrice_tranposee(tf_idf)

    return tf_idf_transposed


def matrice_tranposee(matrix):
    transposed_matrix = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix


# Fonctionalité 1 permettant de trouver les mots les moins importants
def mots_non_importants(files_names):
    tf_idf_matrix = TD_IDF(files_names)

    non_important = []
    for row in tf_idf_matrix:
        i = 1
        while i < len(row) and row[i] <= 0:
            i += 1

        if i == len(row):
            non_important.append(row[0])

    return non_important


# Foonctionalité 2 permettant d'obtenir les mots avec le score + eleve
def most_important_word(tf_idf_matrix):
    somme_scores = {}
    most_important_word = []

    # Calcul le td-idf total du mot
    # On initialise pour chaque ligne la somme a 0 + mot concerné
    for lines in tf_idf_matrix:
        word = lines[0]
        somme_score = 0

        # Permet de parcourir la ligne sans le mot
        for score in lines[1:]:
            somme_score += score
        # Si le mot est déja dans le dictionnaire on ajoute la nouvelle somme de la ligne
        if word in somme_scores:
            somme_scores[word] += somme_score
        # Sinon on ajoute le mot au dictionnaire
        else:
            somme_scores[word] = somme_score

    # Compare les scores td-idf afin de savoir lequel est le plus grand
    score_maximun = 0
    for somme_score in somme_scores.values():
        if somme_score > score_maximun:
            score_maximun = somme_score
    # Tout ce qui sont égal au maximun sont ajoutés à la liste
    for (mot, somme_score) in somme_scores.items():
        if somme_score == score_maximun:
            most_important_word.append(mot)

    return most_important_word  # Retourne une liste contenant le mot le plus important


# Fonctionalité 3

def word_per_president(files_names, president_last_name):
    word_count = {}

    for file_name in files_names:
        if president_last_name.lower() in file_name.lower():
            # Créer le chemin d'accès
            input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
            # Ouvre un fichier
            with open(input_file_path, 'r') as f:
                content = f.read()
                # Permet de récupèrer le nombre de fois que les mots apparraissent dans le discours
                tf_scores = word_occurrences_tf(content)
                # obtiens un dico contenant le nombre de fois que chaque mot apprait dans les deux dico
                for (word, count) in tf_scores.items():
                    if word in word_count:
                        word_count[word] += count
                    else:
                        word_count[word] = count
    return word_count


def mots_trie(word_count, files_names):
    no_import_word = mots_non_importants(files_names)
    for word in list(word_count.keys()):
        if word in no_import_word:
            del word_count[word]
    return word_count


def mots_plus_repeter(word_count):
    president_most_important = []
    tf_plus_grand = 0
    for value in word_count.values():
        if value > tf_plus_grand:
            tf_plus_grand = value
    for (word, count) in word_count.items():
        if count >= tf_plus_grand:
            president_most_important.append(word)

    return president_most_important


# Fonctionalité 4

def president_to_mention_topic(files_names, target_words):
    mention = {}

    for president_last_name in extractions_name(files_names):
        for file_name in files_names:
            input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
            with open(input_file_path, 'r') as f:
                content = f.read()

                # Vérifier si le discours mentionne le thème
                for word in target_words:
                    if word in content:
                        if president_last_name not in mention:
                            mention[president_last_name] = file_name

    return mention  # Retourne un dictionnaire qui a pour clé le nom de famille de president et comme valeur son nom de fichier


def president_speak_about_the_most_topic(files_names, target_word, mention):
    nation_word_occurrences = {}
    president_word_occurrences = {}

    for president_last_name in mention:
        president_word_occurrences[president_last_name] = word_per_president(files_names, president_last_name)

    nation_word_president = []

    for president_last_name, occurrences in president_word_occurrences.items():
        if target_word in occurrences:
            nation_word_president.append(president_last_name)

    return nation_word_president


# Fonctionalité 5
def first_president_to_mention_topic(files_names, target_words):
    first_mention = {}

    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()

            # Vérifier si le discours mentionne le thème
            for word in target_words:
                if word in content:
                    if file_name not in first_mention:
                        first_mention[file_name] = file_name

    return first_mention


# Fonctionalité 6
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
        common_important_words = set(list(common_important_words) + [word])

    # Filtrer les mots communs avec les ensembles de mots des présidents suivants avec une boucle explicite
    for president_last_name in presidents_to_consider[1:]:
        current_president_words = set()
        for word in president_words_dict[president_last_name]:
            current_president_words = set(list(current_president_words) + [word])

        # Garde  les mots communs
        common_important_words_temp = set()
        for word in common_important_words:
            if word in current_president_words:
                common_important_words_temp = set(list(common_important_words_temp) + [word])

        common_important_words = common_important_words_temp

    return common_important_words


def afficher_menu():
    print("Menu Principal:")
    print("1. Trouver les mots les moins importants")
    print("2. Obtenir les mots avec le score le plus élevé")
    print("3. Indiquer le(s) mot(s)  le(s) plus répété(s) par un président")
    print("4. Indiquer quel est le president a voir parler de la Nation ")
    print("5. Indiquer le premier président à parler du climat et/ou de l’écologie ")
    print("6. Indique  le(s) mot(s) que tous les présidents ont évoqués hormis les moins importants")
    print("7. Quitter")


def main(directory, extension):
    files_names = list_of_files(directory, extension)

    while True:
        afficher_menu()
        choix = input("Choisissez une option du menu (1-6): ")

        if choix == "1":
            non_import_words = mots_non_importants(files_names)
            print("Les mots avec un score idf nulles sont :", non_import_words)

        elif choix == "2":
            td_idf_matrix = _matrix = TD_IDF(files_names)
            important_words = most_important_word(td_idf_matrix)
            print("Les mots les plus importants sont :", important_words)

        elif choix == "3":

            print("Veuillez saisir un nom de président parmi : {}".format(
                association_lastname_firstname(extractions_name(files_names), )))
            president_last_name = input()
            president_word_occurrences = word_occurrences_tf_per_president(files_names, president_last_name)
            most_repeat_trié = list_trié(president_word_occurrences)
            print("Le(s) mot(s) le(s) plus répété(s) par le président", president_last_name, "sont:", most_repeat_trié)

        elif choix == "4":
            target_word = "nation"
            nation_word_occurrences = {}
            president_last_name = extractions_name(files_names)

            first_mention = first_president_to_mention_topic(files_names, target_word)
            president_word_occurrences = {}

            for president_last_name in first_mention.keys():
                president_word_occurrences[president_last_name] = word_occurrences_tf_per_president(files_names,
                                                                                                    president_last_name)

            nation_word_occurrences = {}

            for president_last_name, file_name in first_mention.items():
                if president_last_name in president_word_occurrences:
                    nation_word_occurrences[president_last_name] = president_word_occurrences[president_last_name]
            print("Le(s) président(s) qui a(ont) parlé de la Nation :", list(nation_word_occurrences.keys()))

            most_mentions_president = None
            max_mentions = 0

            for president_last_name, occurrences in nation_word_occurrences.items():
                current_mentions = 0

                for count in occurrences.values():
                    if count > current_mentions:
                        current_mentions = count

                if current_mentions > max_mentions:
                    max_mentions = current_mentions
                    most_mentions_president = president_last_name

            print("Le président qui a répété le plus souvent le mot 'nation' :", most_mentions_president)


        elif choix == "5":
            target_words = ['climat', 'écologie']

            # Trouver le premier président à mentionner le climat et/ou l'écologie
            first_mention = first_president_to_mention_topic(files_names, target_words)

            if first_mention:
                president, first_discours = list(first_mention.items())[0]
                print(
                    f"Le premier président à parler du climat et/ou de l'écologie est {association_lastname_firstname({president})[president]}, dans son discours intitulé {first_discours}.")
            else:
                print("Aucun président n'a mentionné le climat et/ou l'écologie dans ses discours.")

        elif choix == "6":
            print("Fonction qui permet de savoir tous les mots que les préidents ont dit .")
            non_important_words = mots_non_importants(files_names)
            common_words = common_important_words_across_presidents(files_names, non_important_words)
            print("Mots évoqués par tous les présidents (hormis les mots non importants) :", common_words)

        elif choix == "7":
            print("Au revoir")
    else:
        print("Veuillez choisir un chiffre entre 1-7")


# Partie projet 2 :

def tokenisation_question(question):
    word_question = []
    # Coupe la question en mots
    contenu = question.split()
    for word in contenu:
        # Ajoute chaque mots dans une liste
        word_question.append(word)
    return word_question


def word_presence (files_names, word_question):
    key_words = [] #liste des mots qui sont présent dans le corpus de mots des textes
    #Parcours de l'ensemble des fichiers à la recherche des mots de la question
    for file_name in files_names:
        for word in file_name:
            for word in word_question:
                if word in file_name:
                    word.append(key_words) #Ajout du mot à la liste des mots clés
    return key_words

def tf_score_question(word_question,files_names): 
#tf_sccore_question : fonction qui permet de calculer le tf de chaque mot de la question, met un zero quand le mot n'est pas dans le corpus de document
    word_count_question = {}
    all_word = idf(files_names)
    for word in word_question :
    #word_question : list contenant les mots de la question =, files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
            if word in word_count_question:
                word_count_question[word] += 1
            else:
                word_count_question[word] = 1

    word_question_tf = {} 
    for word in all_word:
        if word in word_count_question :
            word_question_tf[word] = word_count_question[word]
        else:
            word_question_tf[word] = 0

    return word_question_tf

def calculation_vector_question(word_question,files_names):
#calculation_vector_question : fonction qui permet de calculer le vecteur tf_idf de la question 
    idf_scores = idf(files_names)
    # Des mots de la questions
    tf_scores = tf_score_question(word_question,files_names)
    tf_idf_questions=[]


    for word in idf_scores:
        if word in word_question:
        #word_question : list contenant les mots de la question
        #files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
            tf_score = tf_scores[word]
            idf_score = idf_scores[word]
        else :
            tf_score = 0
            idf_score = 0

        tf_idf_questions.append( round(idf_score * tf_score, 2))

    return tf_idf_questions


#files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
def tf_idf_non_transposed(files_names):
#tf_idf_non_transposée : fonction qui recalcule de la matrice tf-idf-document sans qu'elle soit transposée
    tf_idf = []
    idf_scores = idf(files_names)

    tf_idf_row = []
    for word in idf_scores.keys():
        tf_idf_row.append(word)
    tf_idf.append(tf_idf_row)

    for file_name in files_names:
        input_files_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_files_path, 'r') as f:
            content = f.read()

            tf_scores = word_occurrences_tf(content)

            tf_idf_row = []
            for word in idf_scores.keys():

                if word in tf_scores:
                    tf_score = tf_scores[word]
                else:
                    tf_score = 0
                idf_score = idf_scores[word]
                tf_idf_row.append(round(idf_score * tf_score, 2))
            tf_idf.append(tf_idf_row)
    return tf_idf #retourne la même matrice td_idf sauf qu'en colonne nous avons les mots du corpus et en lignes nous avons les documents


#scalar_product_calculation : fonction qui permet de calculer le produit scalaire entre deux vecteur
def scalar_product_calculation(vector_tf_idf_question,vector_tf_idf_corpus):
    sum = 0
    #vector_tf_idf_question : liste qui contient la valeur de tous les mots avec les scores de la question
    #vector-tf_idf_corpus : correspond aux valeur de tous les lots d'un documents
    for i in range(len(vector_tf_idf_question)):
        product = vector_tf_idf_question[i] * vector_tf_idf_corpus[i]
        sum += product
    return sum

#calculation_norm_vector : permet de calculer la norme d'un vecteur
def calculation_norm_vector(vector):
    sum = 0
    for value in vector:
        sum += (value**2)
    norm_vector = math.sqrt(sum)
    return norm_vector #retourne la norme du vecteur
