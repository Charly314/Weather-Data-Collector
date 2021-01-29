# This code is written by Senadhi

def deletechromefiles():
    import os
    import glob

    # define the path to the required pdf files
    path = "C:/Users/Public/Weather Data Collector"

    # select all chromefiles files and assign into filename variables
    chromefiles = glob.glob(path + "/*.crdownload")

    for file in chromefiles:
        os.remove(file)
