import PyRPAFramework as PyRPA
from SecondaryWorkflows import TopwayCloud, TopwayEdu, Asana
import GlobalEmail as ge
from dotenv import load_dotenv
import os

load_dotenv()

config = PyRPA.InitAllSettings()

try:
    TopwayCloud.getScheduledClasses(config)
except Exception as e:
    print(f"General Exception Handling error detected: {str(e.args)}")
    ge.send_email(
        str(config["email"]["emailSustainSubject"]),
        f"Error found while running the automation:<br>{str(e.args)}",
        str(config["email"]["emailSustainRecipients"]),
        str(config["email"]["robotEmail"]),
        str(os.getenv('EMAIL_ROBOT_APP_PASSWORD'))
    )