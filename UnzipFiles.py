# This code is written by Senadhi
def unzipfiles():
    import zipfile
    import glob

# define the path to the required zip files
    path = r'D:\Weather Data Collector'

# select all zip files and assign into filename variables
    zipfiles = glob.glob(path + "/*.zip")

    for file in zipfiles:
        target = file
        handle = zipfile.ZipFile(target)
        handle.extractall(r'D:\Weather Data Collector')
        handle.close()
