from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)