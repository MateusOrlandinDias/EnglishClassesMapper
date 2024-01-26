from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

def getScheduledClasses(config):
    topwayCloudLogin(config)
    return [{"name":"Free. II", "date":"test"}]

def topwayCloudLogin(config):
    driver.get(str(config["links"]["topwayCloudLogin"]))
    driver.find_element('xpath', "//input[@id='email']").send_keys(str(config["usernames"]["topway"]))
    driver.find_element('xpath', "//input[@id='password']").send_keys(str(os.getenv('PASSWORD_TOPWAY')))
    driver.find_element('xpath', "//button[contains(text(), 'Entrar')]").click()
    raise Exception("a")

def navigateMain(driver):
    driver.get("https://cloud.topwayschool.com/home/cliente")