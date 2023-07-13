# generate student data

group = ["1ED11A", "1ED11B", "1ED12A", "1ED12B", "2ED11A", "2ED11B", "2ED12A", "2ED12B"] # names of group
group.extend(["3ED11A", "3ED11B", "3ED12A", "3ED12B", "4ED11A", "4ED11B", "4ED12A", "4ED12B"])
group.extend(["5ED11A", "5ED11B", "5ED12A", "5ED12B"])


path = '/home/student/Documents/python_program/group.csv' # path to directory

f = open(path, 'w') # open a file

index = 1   # variable needed to add 2 record with the same subject but different time
for i in range(len(group)):    # random data and write to file (32 records)
    print(str(i + 1) + "\n")    # print value the current iteration
    f.write(str(i + 1) + "," + group[i] + "," + "75" + "\n")    # write data in file

f.close() # close file
