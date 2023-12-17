# Fichier contenant toutes les fonctions de la partie 1 et 2
# Auteurs : Blanchard Amandine / Morrety Paul
import math
import os


# List_of_files : fonction permettant de créer une liste de fichier avec leur chemin d'accès complet.
# Directory : dossier ou le fichier se trouve , Extension : .txt car texte
def list_of_files(directory, extension):
    files_names=[]
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            files_names.append(file_name)
    return files_names  # Retourne une liste des fichiers avec leur chemin d'acces complet


# Extraction_name : fonction qui permet de nettoyer le chemin d'accès afin de récuperer uniquement les noms de famille des présidents
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
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


# Association_last_name : permet d'associer un prénom au bon de famille
# lastnames_clean : est une liste contenant uniquement les noms de familles des présidents
def association_lastname_firstname(lastnames_clean):
    dictionary_president = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François',
                            'Macron': 'Emmanuel', 'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    for name in lastnames_clean:
        name = dictionary_president[name] + ' ' + name
    return dictionary_president  # Retourne un dictionnaire associant la clé (nom de famille du président ) a son prénom


# display_lit_president : Afficher chaque prénom avec son bon nom de famille
def display_list_president(dictionary_president):
    for name in dictionary_president.keys():  # Permet d'accèder uniquement aux clé du dictionnaire
        print(name)


# convert_file_lower : fonction permettant de prendre les discours dans le dossier speeches est convertir les discours en minuscules puis de le réécrir dans une copie
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents, Directory : dossier ou le fichier se trouve
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


# replacement_punctuation : permet de prendre un texte est d'enlever tous les punctuations
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
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


# word_occurences-tf : fonction qui permet de compter le nombre de fois qu'un mot apparait dans un unique discours
# text : discours
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


# idf : calcule le score idf de chaque mot du corpus
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
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


    # Calculer l'IDF pour chaque mot
    idf_scores = {}
    for word, doc_count in documents_containing_word.items():
        idf_scores[word] = math.log10(total_documents / (doc_count))
    return idf_scores


# TD_IDF_transposed : fonction qui permet de créeer la matrice tf_idf du corpus de documents
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
def TD_IDF_transposed(files_names: str) -> list[list]:
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
    tf_idf_transposed = matrix_tranposee(tf_idf)

    return tf_idf_transposed


# matrix_transposé : inverser les lignes et les colonnes
def matrix_tranposee(matrix):
    transposed_matrix = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix


# Fonctionalité 1 : non_important_words : fonction permettant de trouver les mots les moins importants du corpus ceux qui ont un score tf_idf < 0.
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
def non_important_words(files_names):
    tf_idf_matrix = TD_IDF_transposed(files_names)

    non_important = []
    for row in tf_idf_matrix:
        i = 1
        while i < len(row) and row[i] <= 0:
            i += 1

        if i == len(row):
            non_important.append(row[0])

    return non_important


# Foonctionalité 2 : most_important_word : fonction permettant d'obtenir les mots avec le score + eleve parmis le corpus de document
def most_important_word(tf_idf_matrix):
    sum_scores = {}
    most_important_word = []

    # Calcul le td-idf total du mot
    # On initialise pour chaque ligne la somme a 0 + mot concerné
    for lines in tf_idf_matrix:
        word = lines[0]
        sum_score = 0

        # Permet de parcourir la ligne sans le mot
        for score in lines[1:]:
            sum_score += score
        # Si le mot est déja dans le dictionnaire on ajoute la nouvelle somme de la ligne
        if word in sum_scores:
            sum_scores[word] += sum_score
        # Sinon on ajoute le mot au dictionnaire
        else:
            sum_scores[word] = sum_score

    # Compare les scores td-idf afin de savoir lequel est le plus grand
    score_maximun = 0
    for sum_score in sum_scores.values():
        if sum_score > score_maximun:
            score_maximun = sum_score
    # Tout ce qui sont égal au maximun sont ajoutés à la liste
    for (mot, sum_score) in sum_scores.items():
        if sum_score == score_maximun:
            most_important_word.append(mot)

    return most_important_word  # Retourne une liste contenant le mot le plus important


# Fonctionalité 3 : word_per_president : fonction qui permet de savoir le nombre de fois qu'un president à dit les mots
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents , president_last_name : nom de président choisis par l'utilisateur

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


# sort_words : permet d'enlever tous les mots non importants dans la liste des mots dits par le président choisis
# word_count : dictionnaire associant le mot et le nombre de fois que le président le dit dans son ou ses discours , # files_names : obtenus de la fonction list_of_files liste qui contient
def sort_words(word_count, files_names):
    no_import_word = non_important_words(files_names)
    for word in list(word_count.keys()):
        if word in no_import_word:
            del word_count[word]
    return word_count


# words_more_repeat : fonction qui permet de chercher le mot le plus repeter en trouvant le plus grands score tf
# word_count : dictionnaire associant le mot et le nombre de fois que le président le dit dans son ou ses discours
def words_more_repeat(word_count):
    president_most_important = []
    tf_max = 0
    for value in word_count.values():
        if value > tf_max:
            tf_max = value
    for (word, count) in word_count.items():
        if count >= tf_max:
            president_most_important.append(word)

    return president_most_important


# Fonctionalité 4 : president_to_mention : fonction qui permet de savoir si un discour contient le mot recherché
# targets_words : mots a rechercher indiquer par l'utilisateur , files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents

def president_to_mention_topic(files_names, target_words):
    mention = {}
    for president_last_name in ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']:
        for file_name in files_names:
            if president_last_name.lower() in file_name.lower():
                input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
                with open(input_file_path, 'r') as f:
                    content = f.read()
                    word = content.split()

                    # Vérifier si le discours mentionne le thème
                    if target_words in word:
                        if president_last_name not in mention:
                            mention[president_last_name] = file_name

    return mention  # Retourne un dictionnaire qui a pour clé le nom de famille de president et comme valeur son nom de fichier


# president_speak_about_the_most_topic : fonction qui permet d'obtenir le president qui a le plus repeter le mot recherché
# files_names: obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents, target_words : mots a rechercher indiquer par l'utilisateur , mention : list des président qui ont parlé du mot rechercher
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


# Fonctionalité 5 : first_president_to_mention_topic : fonction qui s'arrète des que le mot recherche est trouve dans un discours
# files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents, target_words : mots a rechercher indiquer par l'utilisateur
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
                        for name in ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']:
                            if name.lower() in file_name.lower():
                                last_name = name
                        first_mention[last_name] = file_name

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
            non_import_words = non_important_words(files_names)
            print("Les mots avec un score idf nulles sont :", non_import_words)

        elif choix == "2":
            td_idf_matrix = _matrix = TD_IDF_transposed(files_names)
            important_words = most_important_word(td_idf_matrix)
            print("Les mots les plus importants sont :", important_words)

        elif choix == "3":

            president_last_name = "Chirac"
            word_count = word_per_president(files_names, president_last_name)
            word_count_trie = sort_words(word_count, files_names)
            most_repetated = most_repetated(word_count_trie)
            print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac hormis les mots non importants sont",
                  most_repetated)

        elif choix == "4":
            president_last_name = "Chirac"
            word_count = word_per_president(files_names, president_last_name)
            word_count_trie = sort_words(word_count, files_names)
            most_repetated = most_repetated(word_count_trie)
            print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac hormis les mots non importants sont",
                  most_repetated)

        elif choix == "5":
            target_words = ['climat', 'écologie']
            first_mention = first_president_to_mention_topic(files_names, target_words)
            first_mention = list(first_mention.keys())
            print("Le premier président a parler de climat ou/et d'écologie est", first_mention[0])

        elif choix == "6":
            print("Fonction qui permet de savoir tous les mots que les préidents ont dit .")
            non_important_words = non_important_words(files_names)
            common_words = common_important_words_across_presidents(files_names, non_important_words)
            print("Mots évoqués par tous les présidents (hormis les mots non importants) :", common_words)

        elif choix == "7":
            print("Au revoir")
    else:
        print("Veuillez choisir un chiffre entre 1-7")


# Partie projet 2 :
# tokenization_question : fonction qui permet de decouper la question en mot et on applique les mêmes modiffaction que pour les textes
# question : chaîne de carcatères entrer par l'utilisateur
def tokenization_question(question):
    word_question = []
    # Application des mêmes modifiaction du texte sur la question

    content_lowercase = question.lower()
    punctuation_character = ',;:.?!""()[]*/'
    question_clean = ''

    for car in content_lowercase:
        if car in punctuation_character:
            question_clean += ' '
        elif car == "'" or car == "-":
            question_clean += ' '
        else:
            question_clean += car

    # Divise la question en mot
    content = question_clean.split()
    for word in content:
        word_question.append(word)
    return word_question


# word_presence : fonction qui permet de detecter les mots en commun dans la question et dans le corpus
# word_question : list contenant les mots de la question =, files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
def word_presence(files_names, word_question):
    word_file = set()
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()
            speech = content.split()
            for word in speech:
                word_file.add(word)
    commun_terms = set(word_question) & word_file
    return commun_terms


# Calcul du vecteur TD-IDF pour les termes de la questions


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


# calculus_smiliratité : fonction qui permet de calculer la smiliratité du vecteur_tf_idf_question avec chaque document du corpus
# vector_tf_idf_question : liste qui contient la valeur de tous les mots avec les scores de la question, files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
def calculus_smiliratité(vector_tf_idf_question, matrix_non_transposed, files_names):
    smilarities = {}
    for i in range(1, len(matrix_non_transposed)):
        vector_b = matrix_non_transposed[i]
        dot_product_doc = scalar_product_calculation(vector_tf_idf_question, vector_b)
        smilarity = dot_product_doc / (
                    calculation_norm_vector(vector_tf_idf_question) * calculation_norm_vector(vector_b))
        document_name = files_names[i - 1] + "copie.txt"
        smilarities[document_name] = smilarity

    return smilarities


# document_mmore_relevant : fonction qui permet de trouver le document avec le plus grands score de smiliraité avec le vecteur tf_idf de la question
# vector_tf_idf_question : liste qui contient la valeur de tous les mots avec les scores de la question, files_names : obtenus de la fonction list_of_files liste qui contient tous les chemins d'accès de tous les documents
def document_more_relevant(matrix_non_tranposed, vector_tf_idf_question, files_names):
    similarities = calculus_smiliratité(vector_tf_idf_question, matrix_non_tranposed, files_names)
    max = 0
    for (files_names, values) in similarities.items():
        if values > max:
            max = values
            document_more_relevant = files_names
            document_more_relevant_original = files_names.split("copie.txt")

    return document_more_relevant, document_more_relevant_original[0]


# most_important_words_in_question : fonction qui permet de trouver le mot avec le plus grand score tf_idf de la question
# list_word = liste qui contient tous les mots du corpus, # vector_tf_idf_question : liste qui contient la valeur de tous les mots avec les scores de la question
def most_important_words_in_question(vector_tf_idf_question, list_word):
    max_tf_idf = 0

    for i in range(len(vector_tf_idf_question)):
        tf_idf_score = vector_tf_idf_question[i]

        if tf_idf_score > max_tf_idf:
            max_tf_idf = tf_idf_score
            max_word = list_word[i]
    return max_word


def generation_question(document_more_relevant_original, most_important_word):
    input_files_path = "./speeches" + '/' + document_more_relevant_original
    with open(input_files_path, "r", encoding='utf-8') as f1:
        speech = f1.read()
        # Divise le texte en une liste de pharse
        content = speech.split(".")

        position_word = -1
        index = 0
        while index < len(content) and position_word == -1:
            # On trouve la position du mot dans la liste
            if most_important_word in content[index]:
                position_word = index
            index += 1

        if position_word == -1:
            return None
        # On retourne la phrase entière de l'indice
        sentence = content[position_word]

    return sentence
