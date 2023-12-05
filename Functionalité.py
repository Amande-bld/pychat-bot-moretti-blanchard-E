from function import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
tf_idf_matrix = TD_IDF(files_names)

if __name__ == '__main__':
    # Fonctionalité 1

    print("Les mots les moins importants sont :", mots_non_importants(files_names))
    # Fonctionalité 2

    print("Le(s) mots les plus importants sont :", most_important_word(tf_idf_matrix))

    # Fonctionalité 3

    print("Veuillez saisir un nom de président parmi : {}".format(
        association_lastname_firstname(extractions_name(files_names), )))
    president_last_name = input()
    president_word_occurrences = word_occurrences_tf_per_president(files_names, president_last_name,
                                                                   mots_non_importants(files_names))
    most_repeat_tri = list_trié(president_word_occurrences)
    print("Le(s) mot(s) le(s) plus répété(s) par le président", president_last_name, "sont:", most_repeat_tri)

    # Fonctionalité 4

    target_word = "nation"
    nation_word_occurrences = {}
    president_last_name = extractions_name(files_names)

    # Récupère le fichier ou pour la première fois le mot apparait ça crée un dico.
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

    # Fonctionalité 5

    target_words = ['climat', 'écologie']

    # Trouver le premier président à mentionner le climat et/ou l'écologie
    first_mention = first_president_to_mention_topic(files_names, target_words)

    if first_mention:
        president, first_discours = list(first_mention.items())[0]
        print(
            f"Le premier président à parler du climat et/ou de l'écologie est {association_lastname_firstname({president})[president]}, dans son discours intitulé {first_discours}.")
    else:
        print("Aucun président n'a mentionné le climat et/ou l'écologie dans ses discours.")

    # Fonctionlaité 6

    non_important_words = mots_non_importants(files_names)
    common_words = common_important_words_across_presidents(files_names, non_important_words)

    print("Mots évoqués par tous les présidents (hormis les mots non importants) :", common_words)
