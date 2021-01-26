import schedule
import time
from UnzipFiles import unzipfiles
from DeleteUnwantedFiles import deleteunwantedfiles
from main import mergefiles


def updatefiles():
    unzipfiles()
    deleteunwantedfiles()
    mergefiles()


# updatefiles() will run every Monday at 6.00 am
schedule.every().monday.at('06:00').do(updatefiles)

while 1:
    schedule.run_pending()
    time.sleep(1)
