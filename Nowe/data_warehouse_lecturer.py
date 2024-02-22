# generate student data
import random

nazwisko = ["Nowak", "Kowalski", "Wisniewski", "Wojcik", "Kowalczyk", "Kaminski", "Lewandowski"]        # surnames
nazwisko.extend(["Zielinski", "Szymanski", "Wozniak", "Dabrowski", "Kozlowski", "Mazur", "Jankowski"])
nazwisko.extend(["Kwiatkowski", "Wojciechowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski"])

imie = ["Piotr", "Krzysztof", "Andrzej", "Tomasz", "Jan", "Paweł", "Michał", "Marcin", "Stanislaw", "Jakub"]    # names
imie.extend(["Adam", "Marek", "Lukasz", "Grzegorz", "Mateusz", "Wojciech", "Mariusz", "Dariusz", "Zbigniew", "Jerzy"]);

stopien = ["mgr.", "mgr. inz.", "dr.", "dr. inz", "dr. hab. inz.", "prof."]

# path = '/home/student/Documents/python_program/lecturer.csv' #   path to directory (Linux)
path = 'C:/Users/Joseph/Documents/db_warehouse_script/lecturer.csv' #   path to directory (Windows)

f = open(path, 'w') # open a file

for i in range(1, 81):    # random data and write to file (80 records)
    print(str(i) + "\n")    # print value the current iteration
    f.write(str(i) + "," + random.choice(nazwisko) + "," + random.choice(imie) + "," + random.choice(stopien) + "\n")   # write data in file

f.close() # close file
