from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import PyRPAFramework as PyRPA
from SecondaryWorkflows import TopwayCloud, TopwayEdu, Asana

config = PyRPA.InitAllSettings()

# chrome_options = Options()
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(options=chrome_options)