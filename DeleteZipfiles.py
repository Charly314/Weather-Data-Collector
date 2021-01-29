# This code is written by Senadhi

def deletezipfiles():
    import os
    import glob

    # define the path to the required pdf files
    path = "C:/Users/Public/Weather Data Collector"

    # select all csv files and assign into filename variables
    zipfiles = glob.glob(path + "/*.zip")

    for file in zipfiles:
        os.remove(file)
