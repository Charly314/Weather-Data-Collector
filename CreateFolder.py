# This code is written by Senadhi
def createfolder():
    import os
    import os.path

# define the path to the required zip files
    path = r'D:'
# check whether folder already exists
    file_path = os.path.isdir(r'D:\Weather Data Collector')

# If foldr doesn't exist create the new folder
    if not file_path:
        os.chdir(path)
        newfolder = "Weather Data Collector"
        os.mkdir(newfolder)
