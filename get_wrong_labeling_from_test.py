import sys
import os.path

file_list_1 = []
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in [f for f in filenames if f.endswith(".tsv")]:
        if filename == "test.tsv":
            file_list_1.append(os.path.join(dirpath, filename))

false_labels_1 = {}
for file in file_list_1:
    with open(file, 'r') as src:
        for line in src:
            line = line.strip("\n")
            if line != "":
                values = line.split(" ")
                if values[1] != values[2]:
                    try:
                        false_labels_1[f'{values[0]} {values[1]}'] = false_labels_1[f'{values[0]} {values[1]}'] + 1
                    except KeyError:
                        false_labels_1[f'{values[0]} {values[1]}'] = 1

file_list_2 = []
for dirpath, dirnames, filenames in os.walk(sys.argv[2]):
    for filename in [f for f in filenames if f.endswith(".tsv")]:
        if filename == "test.tsv":
            file_list_2.append(os.path.join(dirpath, filename))

false_labels_2 = {}
for file in file_list_2:
    with open(file, 'r') as src:
        for line in src:
            line = line.strip("\n")
            if line != "":
                values = line.split(" ")
                if values[1] != values[2]:
                    try:
                        false_labels_2[f'{values[0]} {values[1]}'] = false_labels_2[f'{values[0]} {values[1]}'] + 1
                    except KeyError:
                        false_labels_2[f'{values[0]} {values[1]}'] = 1


for wrong_label in false_labels_1.keys():
    try:
        if false_labels_1[wrong_label] > false_labels_2[wrong_label]:
            print(f'{wrong_label}: m1-({false_labels_1[wrong_label]}) m2-({false_labels_2[wrong_label]}) #############')
        else:
            print(f'{wrong_label}: m1-({false_labels_1[wrong_label]}) m2-({false_labels_2[wrong_label]})')
    except KeyError:
        print(f'{wrong_label}: m1-({false_labels_1[wrong_label]})')
