# This code is written by Senadhi

import schedule
import time
from UnzipFiles import unzipfiles
from DeleteUnwantedFiles import deleteunwantedfiles
from DeleteZipfiles import deletezipfiles
from RemoveColumn import removeColumn


def updatefiles():
    # downloadfiles()
    unzipfiles()
    deletezipfiles()
    deleteunwantedfiles()
    removeColumn()


# updatefiles() will run every Monday at 6.00 am
schedule.every().monday.at('06:00').do(updatefiles)

while 1:
    schedule.run_pending()
    time.sleep(1)
