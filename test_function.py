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
