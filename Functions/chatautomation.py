from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pathlib

ScriptDir = pathlib.Path().absolute()

url = 'https://chat.openai.com/'

chrome_option = Options()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument(f"--profile-directory=Default")
chrome_option.add_argument(f"user-data-dir={ScriptDir}\\chromedata")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_option)

driver.maximize_window()
driver.get(url=url)
sleep(500)


def websiteopener():
    while True:
        try:
            xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH, value=xPATH)
            break
        except:
            pass


def sendmessage(Query):
    xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea'
    driver.find_element(by=By.XPATH, value=xPATH).send_keys(Query)
    sleep(0.5)
    Xpath2 = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button'
    driver.find_element(by=By.XPATH, value=Xpath2).click()


# def Popupremoval():
#     Xpath = '/html/body/div[3]/div[3]/div/section/button'
#     driver.find_element(by=By.Xpath,value=Xpath).click()
# Popupremoval()


websiteopener()
sendmessage("who is the owner of tata")
