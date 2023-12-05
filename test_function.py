from function import *
directory = "./speeches"
if __name__ == '__main__':
    files_names = list_of_files(directory, "txt")
    print(files_names)

# Lastname clean
lastname_clean = extractions_name(files_names)
print(lastname_clean)

# Association lastname => name
print(association_lastname_firstname(lastname_clean))
dictionary_president = association_lastname_firstname(lastname_clean)

# Affiche liste des présidents
display_list_president(dictionary_president)

# Convertit texte en minuscule
convert_file_lower_case(files_names, directory)

# Convertit la ponctuation
replacement_punctuation_(files_names)

# Compte occurence des mots
for file_name in files_names:
    fichier_entrer = "./cleaned" + '/' + file_name + "copie.txt"
    with open(fichier_entrer, 'r') as f:
        contenu = f.read()
        print(word_occurrences_tf(contenu))
# idf
print(idf(files_names))

# Affiche matrice
matrice = TD_IDF(files_names)
for item in matrice:
    print(item)

# tokenisation question
question = input("Veuillez saisir une question")
word_question = tokenisation_question(question)
print(word_question)

# document dans lequel mot apparait

res = search_wordsquestion_in_files(word_question, files_names)
print(res)
