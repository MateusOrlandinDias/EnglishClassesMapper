import PyRPAFramework as PyRPA
from SecondaryWorkflows import TopwayCloud, TopwayEdu, Asana

config = PyRPA.InitAllSettings()

TopwayCloud.topwayCloudLogin(config)