import csv
import datetime
from toy import Toy

# reads in the toy orders from a file
def readToys(toyfile):
    with open(toy_file, 'rb') as f:
        toysfile = csv.reader(f)
        # skipping the first line which describes the data
        toysfile.next()
        toys = list()
        for row in toysfile:
            id = int(row[0])
            arrivaltime = row[1]
            at = arrivaltime.split(' ')
            time = datetime.datetime(int(at[0]),int(at[1]),int(at[2]),int(at[3]),int(at[4]))
            duration = float(row[2])
            toys.append(Toy(id,time,duration))

    return toys
