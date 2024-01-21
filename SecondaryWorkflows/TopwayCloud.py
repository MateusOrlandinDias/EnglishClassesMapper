def getScheduledClasses(config):
    topwayCloudLogin(config)
    return 'a'

def topwayCloudLogin(config):
    driver = driver.get('https://cloud.topwayschool.com/login')


def navigateMain(driver):
    driver = driver.get("https://cloud.topwayschool.com/home/cliente")