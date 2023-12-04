from function import *
directory = "./speeches"
if __name__ == '__main__':
    files_names = list_of_files(directory, "txt")
    print(files_names)

lastname_clean = extractions_name(files_names)
print(lastname_clean)

print(association_lastname_firstname(lastname_clean))
dictionary_president = association_lastname_firstname(lastname_clean)

display_list_president(dictionary_president)

convert_file_lower_case(files_names, directory)

replacement_punctuation_(files_names)

for file_name in files_names:
    fichier_entrer = "./cleaned" + '/' + file_name + "copie.txt"
    with open(fichier_entrer, 'r') as f:
        contenu = f.read()
        print(word_occurrences_tf(contenu))

print(idf(files_names))

matrice = TD_IDF(files_names)
for item in matrice:
    print(item)
