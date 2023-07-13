# generate student data

path = '/home/student/Documents/python_program/time.csv' #   path to directory

f = open(path, 'w') #   open a file

for i in range(1, 32):    #   random data and write to file (31 records)
    print(str(i) + "\n")    #   print value the current iteration
    
    if (i < 10):
        f.write(str(i) + "," + "2023-07-0" + str(i) + "\n") # write data in file
    else:
        f.write(str(i) + "," + "2023-07-" + str(i) + "\n")
      
f.close() #close file
