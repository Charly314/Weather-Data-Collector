# This code is written by Senadhi
# def mergefiles():
import pandas as pd
import glob
import os

# define the path to the required CSV files
path = r'C:\Users\udari\PycharmProjects\pythonProject1\data_files'

# select all csv files and assign into filename variables
filenames = glob.glob(path + "/*.csv")

colnames = ["Date & time", "Total", "Quality", "Comment"]
# combine all csv files into one using for loop
master_file = pd.concat((pd.read_csv(file, skiprows=4, header=None) for file in filenames))
master_file.columns = colnames

# Create the master CSV file
master_file.to_csv("output.csv")
