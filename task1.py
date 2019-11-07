import os
import nltk
import re

class sentence:
    def __init__(self):
        sentence = ""
        subject_name = ""
        subject_mid = ""
        object_name = ""
        object_mid = ""

def infor_extra(file, sentences):
    while True:
        line = file.readline()
        if line == "[":
            continue
        elif line =="]":
            break

        brackets_stack = []





if __name__ == '__main__':
    directory = "a4_data"
    files = os.listdir(directory)

    sentences = []
    for file in files:
        f = open(directory+"/"+file)
        relation = file.split(".json")[0]
        infor_extra(f, sentences)
        f.close()
