## THIS PY FILE IS CREATED BY HARRY QI STUDNT ID 13287683 ##

def downloadfiles():

    print("Welcome to weather data collector!")
    print("PLEASE DO NOT CLOSE THE BROWSER OR CLOSE THE PROGRAM! ")
    # use 'python -m pip install ******' to install necessary package.
    # use 'python -m pip install requests' command to install requests.
    # use 'python -m pip install panda' command to install panda.
    # use 'python -m pip install selenium' & 'python -m pip install webdriver-manger' run ' from selenium import webdriver
    # from webdriver_manager.chrome import ChromeDriverManager
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from GetLinks import Link_List
    #from CheckDownloads import latest_file,FileList
    #from CreateFile import CreateTempFile
    import importlib
    from importlib import reload

    import time


    for links in Link_List:

        options = webdriver.ChromeOptions()
        options.add_argument("--enable-javascript") # enable javascript
        options.add_experimental_option("prefs",{ "download.default_directory": r"C:\Users\Public\Weather Data Collector"})
        driver = webdriver.Chrome(options=options)


        driver.get(links)
        driver.implicitly_wait(10)  #wait 10s for web loading
    # print(driver.page_source) # exam code
        driver.switch_to.frame('webhyd')        #locate id in ifream
        driver.switch_to.frame('plpllf_org')    #unpack plpllf_org ifream under webhyd
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"titlelinkplplcf_org"))).click()
    #Click Custom OutPut, wait 5s till custom output avalible


        driver.switch_to.default_content()
        driver.switch_to.frame('webhyd') #back to main content
        driver.switch_to.frame('plplcf_org') #unfold webhyd and plplcf_org
        Period_select = Select(driver.find_element_by_id('pl_period'))
        Period_select.select_by_visible_text('All data')
        Output_select = Select(driver.find_element_by_id('output'))
        Output_select.select_by_visible_text('Download')
        driver.implicitly_wait(0.5) #wait 0.5s till interval selection avalible
        Interval_select = Select(driver.find_element_by_id('interval'))
        Interval_select.select_by_visible_text('Daily')


        Download_Button = driver.find_element_by_id('submit')
        Download_Button.click()


        confirm = driver.find_element_by_xpath("//div[@class='msgbox msgbox_cf']//button[1]")
        confirm.click() # start download
        time.sleep(10)

        #if latest_file.endswith('.zip.crdownload'):

        #time.sleep(5)



        #else:
        driver.close()








    print("Your data is ready to use!")