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
    president_last_name = "Chirac"
    word_count = word_per_president(files_names, president_last_name)
    word_count_trié = mots_trie(word_count, files_names)
    most_repetated = mots_plus_repeter(word_count_trié)
    print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac hormis les mots non importants sont",
          most_repetated)

    # Fonctionalité 4

    target_word = "nation"

    mention = president_to_mention_topic(files_names, target_word)
    print("Les présidents qui ont parlé de nation sont :", mention)

    for president_last_name in mention:
        word_count[president_last_name] = word_per_president(files_names, president_last_name)
    most_repeated_president = list(president_speak_about_the_most_topic(files_names, target_word, mention))

    print("Le président qui a répéter le plus de fois le mot", target_word, 'est', most_repeated_president[0])

    # Fonctionalité 5

    target_words = ['climat', 'écologie']
    first_mention = first_president_to_mention_topic(files_names, target_words)
    print("le premier président a parler de climat d'écologie dans l'ordre des fichiers est", first_mention)

    # Fonctionilaté 6

    non_important_words = mots_non_importants(files_names)
    common_words = common_important_words_across_presidents(files_names, non_important_words)

    print("Mots évoqués par tous les présidents (hormis les mots non importants) :", common_words)
