from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import pandas as pd
import time
from io import StringIO

load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

def getScheduledClasses(config):
    topwayCloudLogin(config)
    driver.get("https://cloud.topwayschool.com/home/agenda")
    time.sleep(2)
    driver.find_element('xpath', "//i[contains(text(), 'keyboard_arrow_right')]").click()
    getAgendaTable()
    return [{"name":"Free. II", "date":"test"}]

def topwayCloudLogin(config):
    driver.get(str(config["links"]["topwayCloudLogin"]))
    driver.find_element('xpath', "//input[@id='email']").send_keys(str(config["usernames"]["topway"]))
    driver.find_element('xpath', "//input[@id='password']").send_keys(str(os.getenv('PASSWORD_TOPWAY')))
    driver.find_element('xpath', "//button[contains(text(), 'Entrar')]").click()

def getAgendaTable():
    time.sleep(5)
    html_page=driver.page_source
    soup = BeautifulSoup(html_page, 'html.parser')
    html_table = soup.find('table')
    html_content = StringIO(str(html_table))
    dfAgenda = pd.read_html(html_content)[0]
    print(dfAgenda)
    return dfAgenda
    