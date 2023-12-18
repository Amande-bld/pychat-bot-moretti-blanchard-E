# Pychat-bot-moretti-blanchard-E

* Moretti Paul
* Blanchard Amandine

https://github.com/Cathaleya-10/pychat-bot-moretti-blanchard-E/blob/master

Fonctionnement du Programme :

main.py
- Fichier permettant d'appeler les fonctions de notre fichier function.py
- Sert d'interface au projet

function.py

-> Regroupe l'ensemble des fonctions permettant le fonctionnement du projet : 

Partie 1 :

Fonctions de base :
- list_of_files permet de faire une liste avec le chemin d'accès de chaque fichiers du dossier speeches
- extractions_name est utilisé pour extraire le nom de famille du président contenu dans le nom du fichier text
- association_lastname_firstname associe chaque nom de président à son prénom
- convert_file_lower_case réécrit tous les textes en minuscules, et replacement_punctuation_ enlève toute la ponctuation. 

Fonction TF-IDF :
- word_occurrences_tf calcule le score TF de chaque mots unique dans un texte donné
- idf calcule l'IDF de chaque mots unique de l'ensemble des textes
- tf_idf calcule le score TF-IDF de chaque mots par rapport à l'ensemble des fichiers
- score_tdf_idf_nulle sert à retourner les mots sans importances dans l'ensemble des discours (TF-IDF = 0)
- most_important_word retourne la liste des mots les plus importants (TF-IDF le plus élevé)
- word_occurrences_tf_per_president nous donne les mots les plus utilisés pour un président donné
- first_president_to_mention_topic nous renseigne sur le premier président à mentionner un thème spécifique
- common_important_words_across_presidents crée la liste de l'ensemble des mots les plus importants utilisés par tous les présidents 

Partie 2 :

- tokenisation_question permet de sectionner la question en mot et de les ajouter à une liste
- word_presence permet de détecter les mots en commun entre le corpus et la liste
- tf_score_question calcule le score TF des mots qui composent la question
- calculation_vector_question est une fonction qui permet de calculer le vecteur TF-IDF des mots de la question
- tf_idf_non_transposed retourne la même matrice sans la transposition
- scalar_product_calculation calcule le produit scalaire de deux vecteurs
- calculation_norm_vector nous permet d'obtenir la norme d'un vecteur

Fonction ajoutés :

- another_question : permet de poser une autre question sans a avoir à retourner au programme principal

Les dossiers speeches & cleaned
- Le premier stock tous les fichiers que nous utilisons dans notre programme
- Le deuxième stock ces mêmes fichiers, mais sans ponctuations et majuscules.

