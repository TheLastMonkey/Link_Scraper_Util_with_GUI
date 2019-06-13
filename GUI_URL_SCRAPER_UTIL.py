from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import PySimpleGUI as sg
import re,time
######################################## GUI setup
sg.ChangeLookAndFeel('Black') # ez black
layout=[[sg.Text('Input File Path or Url')],
        [sg.Text("File:                    "),sg.Input("",key="_FILE_"), sg.FileBrowse()],
        [sg.Text("URL:                   "),sg.Input("",key="_URL_")],
        [sg.Text("Add regex:           "),sg.Input("",key="_RX_")],
        [sg.Text("Output File Name:"),sg.Input("",key="_OUTputFILE_")],
        [sg.Checkbox("Headless",key="_HEAD_",default=True),sg.Checkbox("Keep User Data - Logins, Cookies, Etc ",key="_USER_Data_"),sg.Text("Wait in Secs: "),sg.Input("0",key="_WAIT_",size=[5,1])],
        [sg.OK("OK"), sg.Cancel(),sg.Text(" "*60),sg.Text("All fields are optional.")] ]

window = sg.Window('Scraper Setup').Layout(layout)
event, values = sg.Window.Read(window)
window.Close()
######################################### Var setup
file_url=values["_FILE_"]
url_url=values["_URL_"]
regex=values["_RX_"]
outPUTfile=values["_OUTputFILE_"]
head=values["_HEAD_"]
furl="file://"
previous_link = ""
current_link=""
######################################### wait setup

wait_time=values["_WAIT_"]
try:
    wait_time=int(wait_time)
except Exception as e:
    print(e)
    wait_time=0
#########################################
user_DATA=values["_USER_Data_"]


######################################### file or url
if file_url=="":
    url_proper=url_url
elif url_url=="":
    url_proper = furl + file_url.replace(" ", "%20")
print(url_proper)

def PRINT_AND_LOG():
    # printing and logging
    global current_link,previous_link
    print(current_link)
    previous_link = current_link
    if outPUTfile =="":
        pass
    else:
        print(current_link,file=open(outPUTfile,"a"))
#######################################
try:
    # options for webdriver
    options = Options()
    if head==False:
        pass
    else:
        options.add_argument("--headless")
    options.add_argument("--window-size=192x108")
    if user_DATA == False:
        pass
    else:
        options.add_argument("user-data-dir=selenium")
    ###################################
    # driver setup
    driver = webdriver.Chrome(options=options, executable_path="./sel_driver/chromedriver")
    driver.set_page_load_timeout(60)
    print("Loading...")
    # main get URL
    driver.get(url_proper)

    time.sleep(wait_time)

    # main scrape for links
    for meta in driver.find_elements_by_xpath("//a[@href]"):
        current_link=meta.get_attribute("href")
        if current_link == previous_link:
            pass
        else:
            if regex is not "":
                for current_link in re.findall(regex,current_link):
                    if current_link == "":
                        pass
                    else:
                        PRINT_AND_LOG()
            else:
                PRINT_AND_LOG()
    driver.close()
except Exception as e:
    print(e)
    driver.close()