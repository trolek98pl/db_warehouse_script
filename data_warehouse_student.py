# generate student data
import random

nazwisko = ["Nowak", "Kowalski", "Wisniewski", "Wojcik", "Kowalczyk", "Kaminski", "Lewandowski"]        #   surnames
nazwisko.extend(["Zielinski", "Szymanski", "Wozniak", "Dabrowski", "Kozlowski", "Mazur", "Jankowski"])
nazwisko.extend(["Kwiatkowski", "Wojciechowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski"])

imie = ["Mateusz", "Marek", "Lukasz", "Jan", "Wojtek", "Pawel", "Jozef", "Wieslaw", "Stanislaw"]    #   names
imie.extend(["Mariusz", "Waldemar", "Stanislaw", "Marian", "Jakub", "Maciej", "Krzysztof", "Bogdan"]);

path = '/home/student/Documents/python_program/student.csv' #   path to directory

f = open(path, 'w') #   open a file

for i in range(1, 1501):    #   random data and write to file (1500 records)
    print(str(i) + "\n")    #   print value the current iteration
    f.write(str(i) + "," + random.choice(nazwisko) + "," + random.choice(imie) + "," + str(random.randrange(19, 26)) + "\n")    # write data in file

f.close() #close file
