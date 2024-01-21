from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

def getScheduledClasses(config):
    topwayCloudLogin(config)
    return [{"name":"Free. II", "date":"test"}]

def topwayCloudLogin(config):
    driver.get(str(config["links"]["topwayCloudLogin"]))
    driver.find_element('xpath', "//input[@id='email']").send_keys(str(config["USER_TOPWAY"]))
    driver.find_element('xpath', "//input[@id='password']").send_keys(str(config["PASSWORD_TOPWAY"]))
    driver.find_element('xpath', "//button[contains(text(), 'Entrar')]").click()

def navigateMain(driver):
    driver.get("https://cloud.topwayschool.com/home/cliente")