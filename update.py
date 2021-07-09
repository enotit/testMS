import csv
import os


# this function reads all the files in \res\*.csv and returns a list
def upd():
    a = []
    for file in os.listdir("res"):
        if len(file) > 4 and file[-4:] == ".csv":
            with open("res/" + file, encoding='utf-8') as target:
                reader_object = csv.reader(target, delimiter=",")
                for row in reader_object:
                    a.append(row)
    return a
