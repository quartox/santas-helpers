import csv
import datetime
import numpy as np
import matplotlib.pyplot as plot

if __name__ == "__main__":
    # Read file from data directory
    toy_file = "toys_rev2.csv"
    with open(toy_file, 'rb') as f:
        toysfile = csv.reader(f)
        toysfile.next()
        # initializing the start time and lists containing toy info
        starttime = datetime.datetime(2014,1,1,0,0)
        toyid = []
        time = []
        toytime = []
        for row in toysfile:
            arrival = row[1]
            at = arrival.split(' ')
            dt = datetime.datetime(int(at[0]),int(at[1]),int(at[2]),int(at[3]),int(at[4]))
            tt = dt-starttime
            time.append(tt.total_seconds()/3600.)
            toytime.append(float(row[2])/60.)
            toyid.append(int(row[0]))
    # saving number of toys with specific range of work times
    # work times are less than 2.5 hours (for elves with low rating)
    # between 2.5 and 32.8 hours (to improve elves rating to 4.0)
    # between 32.8 and 47.6 hours (which can be done without reducing rating)
    # between 47.6 and 248 hours (which reduces rating)
    # and greater than 248 hours (which reduces 4.0 elf to 0.25 elf)
    nums=[0,0,0,0,0]
    # number of hours for jobs in the above ranges
    hours=[0,0,0,0,0]
    # total number of hours to do all toys
    totalhours = 0.

    for ii in toytime:
        totalhours += ii
        if ii <=2.5:
            nums[0] += 1
            hours[0] += ii
        else:
            if ii<=32.8:
                nums[1] += 1
                hours[1] += ii
            else:
                if ii<=47.6:
                    nums[2] += 1
                    hours[2] += ii
                else:
                    if ii<=248:
                        nums[3] += 1
                        hours[3] += ii
                    else:
                        nums[4] += 1
                        hours[4] += ii

    print nums
    print hours
    print totalhours

    # finding the first toy in the list of toys that take much longer
    count = 0
    for x in range(1,9999998):
        if toytime[x] >=47.6:
            count += 1
        if toytime[x] >=248 and toytime[x+1]>=248:
            print time[x]
            print count
            print x
            quit()
