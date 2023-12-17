# Fichier ou se droule les tests des fonctions
# Auteurs : Blanchard Amandine / Morrety Paul




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

# Affiche matrice-tf_idf du corpus
matrix = TD_IDF_transposed(files_names)
for item in matrix:
    print(item)

# tokenisation question
question = input("Veuillez saisir une question")
word_question = tokenization_question(question)
print("Les mots de la question sont:", word_question)

# Mots en commun entre les documents et
commun_word = word_presence(files_names, word_question)
print("Les mots en communs entre la question et les documents sont", commun_word)

# Calcul tf de chaque mot dans la questions
tf_score_question = tf_score_question(word_question, files_names)
print("Le score tf de la question est :", tf_score_question)

# Calcul tf-idf_questions
vector_tf_idf_question = calculation_vector_question(word_question, files_names)
print("le vecteur tf-idf de la question est", vector_tf_idf_question)

# Calcul produit scalaire vecteur
matrix_non_transposed = tf_idf_non_transposed(files_names)

res_produit_scalaire_doc = []

for i in range(1, len(matrix_non_transposed)):
    vector_b = matrix_non_transposed[i]
    scalar_product_docs = scalar_product_calculation(vector_tf_idf_question, vector_b)
    res_produit_scalaire_doc.append(scalar_product_docs)
print("Le produit scalaire de chaque document avec la question est :", res_produit_scalaire_doc)

# Calcul norme vecteur
norm_vector = calculation_norm_vector(vector_tf_idf_question)
print("La norme du vecteur question est :", norm_vector)

# Calcul de smilarité
smilarity_doc = calculus_smiliratité(vector_tf_idf_question, matrix_non_transposed, files_names)
print(smilarity_doc)

# Calcul document le plus pertient
document_more_relevant, document_more_relevant_original = document_more_relevant(matrix_non_transposed,
                                                                                 vector_tf_idf_question, files_names)
print("Le document le plus pertient est :", document_more_relevant, "et le document original est :",
      document_more_relevant_original)

# Génération d'une question
list_mot = idf(files_names)
list_mot = list(list_mot.keys())
print(list_mot)
word_more_important = most_important_words_in_question(vector_tf_idf_question, list_mot)
print(word_more_important)

sentence = generation_question(document_more_relevant_original, word_more_important, question)
print("la reponse est :", sentence)
