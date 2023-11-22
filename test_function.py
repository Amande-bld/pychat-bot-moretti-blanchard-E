from function import *
directory = "./speeches"
if __name__ == '__main__':
    files_names = list_of_files(directory, "txt")
    print(files_names)

if __name__ == '__main__':
    good_names = extractions_name(files_names)
    print(good_names)

if __name__ == '__main__':
    print(association_prénom(good_names))
    dico_prenoms = association_prénom(good_names)
