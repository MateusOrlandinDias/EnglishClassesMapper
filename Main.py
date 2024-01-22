import PyRPAFramework as PyRPA
from SecondaryWorkflows import TopwayCloud, TopwayEdu, Asana
import GlobalEmail as ge

config = PyRPA.InitAllSettings()

try:
    TopwayCloud.topwayCloudLogin(config)
except Exception as e:
    print(f"General Exception Handling error detected: {str(e)}")
    ge.send_email(
        '[R01 Personal - EnglishClassesMapper] Process Error',
        f"Error found while running the automation:<br>{str(e)}",
        str(config["EMAIL_SUSTAIN"]),
        str(config["ROBOT_EMAIL_SENDER"]),
        str(config["EMAIL_ROBOT_PASSWORD"]),
    )