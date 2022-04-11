from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException


CHROME_DRIVER_PATH = "/usr/bin/chromedriver"
SIMILAR_ACCOUNT = "SomethingFancy"
USERNAME = ""
PASSWORD = ""

s = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=s)

class InstaFollower:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(driver_path)
    def login(self):
        pass
    def find_followers(self):
        pass
    def follow(self):
        pass

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    username = self.driver.find_element_by_name("username")
    password = self.driver.find_element_by_name("password")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    time.sleep(2)
    password.send_keys(Keys.ENTER)
def find_followers(self):
    time.sleep(5)
    self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

    time.sleep(2)
    followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers.click()

    time.sleep(2)
    modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    for i in range(10):
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
def follow(self):
    all_buttons = self.driver.find_elements_by_css_selector("li button")
    for button in all_buttons:
        try:
            button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()
