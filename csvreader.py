import csv

current_hash = ""
f = open("log", "a")

with open("duplicates.csv") as csv_file:
    reader = csv.reader(csv_file)
    for (file, hash) in reader:
        if hash != "hash":
            file = file.split('/')[-1]
            if hash != current_hash:
                current_hash = hash
                f.write("leaving best: ./" + file + '\n')
            else:
                f.write("Removing: ./" + file + '\n')
