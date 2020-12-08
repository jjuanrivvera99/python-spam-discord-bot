import os
import random
import string
import time
from datetime import datetime

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
    #chrome_options.add_argument("--headless")
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


def take_screenshot():
    now = datetime.now()
    date_timestamp_string = now.strftime("%Y-%d-%m-%H-%M-%S")
    print(date_timestamp_string)
    driver.get_screenshot_as_file('./Screenshots/' + date_timestamp_string + '.png')


def check_captcha():
    try:
        driver.execute_script('captcha = document.getElementById("recaptcha-anchor");captcha.click()')
        #captcha = driver.find_element_by_id('recaptcha-anchor')
        #captcha.click()
        time.sleep(5)
        take_screenshot()
    except:
        print('No se pudo resolver el captcha')


def get_into_server(guild):
    try:
        server = driver.find_element_by_xpath('//div[contains(@href,"' + guild + '")]')
        server.click()
    except:
        check_captcha()


def get_into_channel(channel):
    channel = driver.find_element_by_xpath('//a[contains(@href,"' + channel + '")]')
    channel.click()


if __name__ == "__main__":
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.get('https://discord.com/login')
    login()
    time.sleep(5)
    take_screenshot()
    get_into_server(os.getenv("SERVER"))
    time.sleep(2)
    get_into_channel(os.getenv("CHANNEL"))
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
