# This code is written by Senadhi

def createfolder():
    import os.path

    # defining the file path and name
    path = "C:/Users/Public"

    # check whether folder already exists
    file_path = os.path.isdir("C:/Users/Public/Weather Data Collector")

    # If foldr doesn't exist create the new folder
    if not file_path:
        os.chdir(path)
        newfolder = "Weather Data Collector"
        os.mkdir(newfolder)

