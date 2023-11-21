import os

def list_of_files(directory, extension):
    files_names=[]
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            files_names.append(file_name)
    return files_names


def extractions_name (files_names):
    names_good = []
    for name in files_names :
       name = name.split("_")[-1]
       name = name[:-4]
       name_mod =""
       for car in name :
            if car != '1' and car != '2' :
                name_mod += car
       names_good.append(name_mod)
    return names_good
