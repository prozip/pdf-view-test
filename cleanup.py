import duplicates as dup
import os, csv


path = "out"
accepted_ext = ["html","js","css","page"]
remove_data = {}


def remove_log_file():
    if os.path.exists("log"):
        os.remove("log")
    if os.path.exists("duplicates.csv"):
        os.remove("duplicates.csv")


def find_remove_duplicates_image():
    current_file = ""
    os.system("cd " + path + ";image-cleaner -v .; mv log ../")
    for line in open("log", "r").readlines():
        type, file = line.strip().split(": ./")
        if type == "leaving best":
            current_file = file
            remove_data[current_file] = []
        elif type == "Removing":
            list = remove_data[current_file]
            list.append(file)

    print("remove same images done")


def find_remove_duplicates_files():
    dup.list_all_duplicates(path, to_csv=True, csv_path=".")
    current_hash = ""
    current_file = ""

    with open("duplicates.csv") as csv_file:
        reader = csv.reader(csv_file)
        for (file, hash) in reader:
            if hash != "hash":
                file = file.split("/")[-1]
                if hash != current_hash:
                    current_hash = hash
                    current_file = file
                    remove_data[file] = []
                else:
                    list = remove_data[current_file]
                    list.append(file)
                    os.system("rm '" + path + "/" + file + "'")


def clean(line):
    for file in remove_data:
        list = remove_data[file]
        for replace_file in list:
            line = line.replace(replace_file, file)
    return line

def replace_page():
    dir = os.listdir(path)
    for file in dir:
        ext = file.split(".")[-1]

        if ext in accepted_ext:
            f = open(path + "/" + file, "r")
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = clean(lines[i])
            f.close()
            f = open(path + "/" + file, "w")
            f.writelines(lines)
            f.close()
        if ext == "html":
            os.rename(path + "/" + file, path + "/index.html")
    print('Replace page done')


remove_log_file()
find_remove_duplicates_image()
find_remove_duplicates_files()
replace_page()

