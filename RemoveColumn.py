# This code is written by Senadhi
# def removeColumn():
import glob
import os
import pandas as pd
import csv

# define the path to the required zip files
path = "D:/Weather Data Collector/"

# select all csv files and assign into filename variables
csvfiles = glob.glob(path + "/*.csv")

Dcsvfiles= dict(zip(csvfiles, ""))
print(Dcsvfiles)

for file in Dcsvfiles.key():
    print(file)
    with open('1160P002.csv', 'r') as files:
        reader = csv.DictReader(files)

    with open('1160P002_1.csv', 'w', newline="") as files:
        col = ['Date and time', 'Total', 'Quality']
        writer = csv.DictWriter(files, fieldnames=col)
        writer.writeheader()

        for line in reader:
            del line['Comments']
            writer.writerow(line)
    files.close()

#for file in os.listdir(path):
    #csvfile = pd.read_csv((path+file), skiprows=3, skipfooter=2, engine='python')
    #csvfile.drop('Comments', axis=1, inplace=True)
    #csvfile.head()
    #print(csvfile)



