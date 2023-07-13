# generate student data

subject = ["Matematyka", "Fizyka", "Mikrokontrolery", "Sterowniki PLC", "Programowanie w jezyku Python", "Metody numeryczne"]   # names of subject
subject.extend(["Maszyny elektryczne", "Naped elektryczny", "Programowanie obiektowe", "Podstawy elektroniki", "Urzadzenia elektryczne"])
subject.extend(["Przetwarzanie obrazow", "Sztuczna inteligencja", "Teoria sterowania", "Bazy danych", "System operacyjny Linux"])

types = ["wyk", "cw", "lab"] # types of classes


path = '/home/student/Documents/python_program/subject.csv' #   path to directory

f = open(path, 'w') #   open a file

index = 1   # variable needed to add 2 record with the same subject but different time
for i in range(len(subject)):    #   random data and write to file (32 records)
    print(str(i) + "\n")    #   print value the current iteration
    for j in range(2):
        if (j == 0):    #   wyk record
            f.write(str(index) + "," + subject[i] + "," + types[0] + "\n")  # write data in file
        else:   #   cw/lab record
            if (i < 2): #   cw
                f.write(str(index) + "," + subject[i] + "," + types[1] + "\n")
            else:   #   lab
                f.write(str(index) + "," + subject[i] + "," + types[2] + "\n")
        index = index + 1

f.close() #close file
