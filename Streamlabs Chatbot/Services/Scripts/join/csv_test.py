import csv

file = open("test.csv", "a")
writer = csv.writer(file)
writer.writerow(["Dude", 0])
writer.writerow(["Another Guy",0])
writer.writerow(["Person 3",0])
file.close()

file = open("test.csv", "r")

for row in file.readlines():
    row = row.split(",")
    if row[0] == "Another Guy":
        num = int(row[1])
        file.write(row[0] + "," + str(num+1))

