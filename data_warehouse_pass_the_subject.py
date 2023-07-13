# generate student data
import random
import math

path = '/home/student/Documents/python_program/pass_the_subject.csv' # path to directory

f = open(path, 'w') # open a file

for i in range(1, 100001):    # random data and write to file (100 000 records)
    print(str(i) + "\n")    # print value the current iteration
    
    nr_albumu = random.randrange(1, 1501)   #random studenet index
    nr_gr = int(math.ceil(nr_albumu / 75))  # calculate number of group based on student index
    
    f.write(str(random.randrange(1, 21)) +"," + str(nr_albumu) + "," + str(nr_gr) + "," + str(random.randrange(1, 81)) + "," + str(random.randrange(1, 32)) + "," + str(random.randrange(2, 6)) + "\n") # write data in file
      
f.close() # close file
