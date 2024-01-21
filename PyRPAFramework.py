import json
from dotenv import dotenv_values
import os

def InitAllSettings():
    with open('Config.json', 'r') as configFile:
        config = json.load(configFile)

    config = EnvToConfig(config)
    
    print('> Init All Settings done. Config Available.')
    return config

def EnvToConfig(config, envPath=".env"):
    variablesEnv = dotenv_values(envPath)
    
    for key, value in variablesEnv.items():
        config[key] = value

    return config
