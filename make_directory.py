import os
import shutil
import sys
import subprocess

data_set = sys.argv[1]
round = sys.argv[2]

directory = f"{data_set}_round_{round}"

parent_dir = "."

path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '%s' created" %directory)

create_dirs = []
for i in range(3, 9):
    path1 = os.path.join(path + "/", f"model_0{i}_{data_set}_r{round}")
    os.mkdir(path1)
    print("Directory '%s' created" % f"model_0{i}_{data_set}_r{round}")
    create_dirs.append(f"model_0{i}_{data_set}_r{round}")


i = int(sys.argv[3])
for model in create_dirs:
    p = subprocess.Popen(f"mv ../flair/gazetteer_embeddings_scripts/resources/taggers/model_0{i}* "
                         f"{os.getcwd()}/{directory}/{model}/", stdout=subprocess.PIPE, shell=True)

    print(p.communicate())

    p = subprocess.Popen(f"rm {os.getcwd()}/{directory}/{model}/model_*/*.pt",
                         stdout=subprocess.PIPE, shell=True)
    print(p.communicate())
    i += 1