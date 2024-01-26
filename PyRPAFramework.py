import json
import os

def InitAllSettings():
    with open('Config.json', 'r') as configFile:
        config = json.load(configFile)
    
    print('> Init All Settings done. Config Available.')
    return config