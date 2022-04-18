import sys
import os.path

file_list = []
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in [f for f in filenames if f.endswith(".tsv")]:
        if filename == "test.tsv":
            file_list.append(os.path.join(dirpath, filename))

false_labels = set()
for file in file_list:
    with open(file, 'r') as src:
        for line in src:
            line = line.strip("\n")
            if line != "":
                values = line.split(" ")
                if values[1] != values[2]:
                    false_labels.add(line)

for wrong_label in false_labels:
    print(wrong_label)
