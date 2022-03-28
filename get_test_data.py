import sys
import re
import os.path
from statistics import mean, stdev

file_list = []
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in [f for f in filenames if f.endswith(".log")]:
        file_list.append(os.path.join(dirpath, filename))

micro_pattern = '- F-score \(micro\)'
macro_pattern = '- F-score \(macro\)'
accuracy_pattern = '- Accuracy'

micro_f1 = []
macro_f1 = []
accuracy = []

for file in file_list:
    with open(file, 'r') as src:
        for line in src:
            if re.search(micro_pattern, line):
                micro_f1.append(float(re.findall("\d+\.\d+", line)[0]))
            if re.search(macro_pattern, line):
                macro_f1.append(float(re.findall("\d+\.\d+", line)[0]))
            if re.search(accuracy_pattern, line):
                accuracy.append(float(re.findall("\d+\.\d+", line)[0]))

print("Average Micro F1 =", round(mean(micro_f1), 4))
print("Standard Deviation Micro F1 =", round(stdev(micro_f1), 5))

print("Average Macro F1 =", round(mean(macro_f1), 4))
print("Standard Deviation Macro F1 =", round(stdev(macro_f1), 5))

print("Average Accuracy F1 =", round(mean(accuracy), 4))
print("Standard Deviation Accuracy F1 =", round(stdev(accuracy), 5))
