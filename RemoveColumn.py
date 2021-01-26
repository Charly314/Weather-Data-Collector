# This code is written by Senadhi
# def removeColumn():
import glob
import os
import pandas as pd
import csv
import datetime

# define the path to the required zip files
path = "D:/Weather Data Collector/"

# select all csv files and assign into filename variables
csvfiles = glob.glob(os.path.join(path,'*.csv'))

cleanfiles = []
filenames = os.listdir(path)
for filename in filenames:
    for file in csvfiles:
    # Assign column headers
        colnames = ["Date & time", "Total", "Quality", "Comment"]
        df = pd.read_csv(file, skiprows=4, skipfooter=2, header=None, engine='python')
        df.columns = colnames
    # Delete Comment column
        del df['Comment']
    # filling  missing values with 0
        df.fillna(0)
    # extract file name
        filename, extention = os.path.splitext(filename)
    # Add new column (Location) and add filename as the station code
        df['Location'] = df.shape[0]*[filename]
        cleanfiles.append(df)
        masterfile = pd.concat(cleanfiles)
        masterfile.to_csv('RainfallData.csv', index=False)
print(filename)





