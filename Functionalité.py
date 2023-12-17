from function import *

# définition des variables de bases
directory = "./speeches"
files_names = list_of_files(directory, "txt")
tf_idf_matrix = TD_IDF_transposed(files_names)

if __name__ == '__main__':
    # Fonctionalité 1

    print("Les mots les moins importants sont :", non_important_words(files_names))

    # Fonctionalité 2

    print("Le(s) mot(s) le(s) plus important(s) sont :", most_important_word(tf_idf_matrix))

    # Fonctionalité 3

    president = ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']
    correct = False
    while not correct:
        president_last_name = input(
            "Veuillez choisir un nom de président parmis cette liste : Chirac, Giscard dEstaing, Hollande, Macron, Mitterrand, Sarkozy : ")

        if president_last_name in president:
            correct = True
        else:
            print(
                "Le président que vous avez choisis ne fait pas partie de la liste. Veuillez en choisir un faisant partie de la liste")
    print("Le président choisis est :", president_last_name)

    word_count = word_per_president(files_names, president_last_name)
    sort_word_count = sort_words(word_count, files_names)
    most_repetated = words_more_repeat(sort_word_count)
    print("Le(s) mot(s) le(s) plus répété(s) par le président", president_last_name,
          " hormis les mots non importants sont : ", most_repetated)

    # Fonctionalité 4

    target_word = input("Veuillez saisir le mot que vous souhaitez chercher : ")
    target_word = target_word.lower()
    # si on met un espace en plus lors de la saisie du mot recherché out of range
    mention = president_to_mention_topic(files_names, target_word)
    print("Les présidents qui ont parlé de nation sont :", list(mention.keys()))

    for president_last_name in mention:
        word_count[president_last_name] = word_per_president(files_names, president_last_name)
    most_repeated_president = list(president_speak_about_the_most_topic(files_names, target_word, mention))

    print("Le président qui a répéter le plus de fois le mot", target_word, 'est le président',
          most_repeated_president[0])

    # Fonctionalité 5

    target_words = ['climat', 'écologie']
    first_mention = first_president_to_mention_topic(files_names, target_words)
    first_mention = list(first_mention.keys())
    print("Le premier président a parler de climat ou/et d'écologie est le président ", first_mention[0])
