# This code is written by Senadhi
def deleteunwantedfiles():

    import os
    import glob

# define the path to the required pdf files
    path = r'D:\Weather Data Collector'

# select all csv files and assign into filename variables
    pdffiles = glob.glob(path + "/*.pdf")

    for file in pdffiles:
        os.remove(file)
