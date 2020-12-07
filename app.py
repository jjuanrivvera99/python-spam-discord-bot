from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from datetime import datetime
import time, os, random, string
load_dotenv()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def login():
    time.sleep(2)
    username = driver.find_element_by_name('email')
    password = driver.find_element_by_name('password')
    username.send_keys(os.getenv("EMAIL"))
    password.send_keys(os.getenv("PASSWORD"))
    password.send_keys(Keys.ENTER)

def takeScreenshot():
    now = datetime.now()
    dateTimeStampString = now.strftime("%Y-%d-%m-%H-%M-%S")
    print(dateTimeStampString)
    driver.get_screenshot_as_file('./Screenshots/' + dateTimeStampString + '.png')

def checkCaptcha():
    try:
        captcha = driver.find_element_by_id('recaptcha-anchor')
        captcha.click()
        time.sleep(5)
        takeScreenshot()
    except:
        print('No se pudo resolver el captcha')

def getIntoServer(guild):
    try:
        server = driver.find_element_by_xpath('//div[contains(@href,"' + guild + '")]')
        server.click()
    except:
        checkCaptcha()

def getIntoChannel(channel):
    channel = driver.find_element_by_xpath('//a[contains(@href,"' + channel + '")]')
    channel.click()

if __name__ == "__main__":
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.get('https://discord.com/login')
    login()
    time.sleep(5)
    takeScreenshot()
    getIntoServer(os.getenv("SERVER"))
    time.sleep(2)
    getIntoChannel(os.getenv("CHANNEL"))
    time.sleep(3)
    pretextArea = driver.find_element_by_xpath('//div[contains(@class,"textArea")]')
    textArea = pretextArea.find_element_by_xpath('//div[contains(@class,"slateTextArea")]')
    
    while True:
        actions = ActionChains(driver)
        element = actions.move_to_element(textArea)
        text = get_random_string(8)
        print(text)
        element.send_keys(text)
        element.send_keys(Keys.ENTER).perform()
        time.sleep(int(os.getenv("FREQUENCY")))