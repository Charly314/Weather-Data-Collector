
def renamefiles():
    import os
    import glob
    import datetime


# define the path to the required csv files
    path = r'C:\Users\udari\PycharmProjects\pythonProject1\data_files'

# select all csv files and assign into filename variables
    csvfiles = glob.glob(path + "/*.csv")

    for file in os.listdir(path):
        filename, extention = os.path.splitext(file)
        current_date = datetime.datetime.today().strftime('%d-%b-%Y')
        new_file_name = [filename] + ["-"] + [str(current_date)] + ['.csv']
        os.rename(os.path.join(path, file), os.path.join(path, ''.join(new_file_name)))


