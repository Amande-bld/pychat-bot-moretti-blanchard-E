from function import *
directory = "./speeches"
if __name__ == '__main__':
    files_names = list_of_files(directory, "txt")
    print(files_names)

if __name__ == '__main__':
    lastname_clean = extractions_name(files_names)
    print(lastname_clean)

if __name__ == '__main__':
    print(association_lastname_firstname(lastname_clean))
    dictionary_president = association_lastname_firstname(lastname_clean)

if __name__ == '__main__':
    display_list_president(dictionary_president)

if __name__ == '__main__':
    convert_file_lower_case(files_names, directory)

if __name__ == '__main__':
    replacement_punctuation_(files_names)

if __name__ == '__main__':
    for file_name in files_names:
        fichier_entrer = "./cleaned" + '/' + file_name + "copie.txt"
        with open(fichier_entrer, 'r') as f:
            contenu = f.read()
            print(word_occurrences_tf(contenu))

if __name__ == '__main__':
    print(idf(files_names))

if __name__ == '__main__':

    matrice = TD_IDF(files_names)
    for item in matrice:
        print(item)
