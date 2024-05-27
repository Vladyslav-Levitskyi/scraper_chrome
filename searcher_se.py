#   This is the first part of code. You need to run THIS code fisrt!
import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, dotenv_values
import os


#   To ensure safety for all sensitive data we will use "dotenv" module.
load_dotenv()
config = dotenv_values(".env")
URL = os.getenv("URL")
USERNAME = config["USERNAME"]   #   This is the solution for .env conflict with a symbol "@".
PASSWORD = os.getenv("PASSWORD")
options = Options()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

service = Service(executable_path=r"C:\Users\Admin\Desktop\Cursorprojcts\web-scraper-chrome\chromedriver.exe")


#   Class LogInGetPages has a few functions. Start_driver() to get settings and start chromedriver.exe
#   login function is for authentication on website, and get_html_source() function to get skeleton of all the pages
#   that we need. And certainly stop_driver() function for completion of work.
class LogInGetPages:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome(options, service=service)

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def login_func(self):
        self.start_driver()
        self.driver.get(url = self.url)
        self.driver.find_element(By.XPATH, "//a[@href='#']").click()
        time.sleep(2)
        field_username = self.driver.find_element(By.ID, "login_name")
        time.sleep(3.2)
        field_username.send_keys(self.username)
        field_password = self.driver.find_element(By.ID, "login_password")
        time.sleep(3)
        field_password.send_keys(self.password)
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "fbutton2"))
            )
            login_button.click()
            time.sleep(5)
            self.get_html_source()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.stop_driver()
        
    def get_html_source(self):
        for page in range(1, 20 + 1):
            try:
                self.driver.get(url=self.url + f"top-filmy/page/{page}/")
                time.sleep(2.3)
                source = self.driver.page_source
                with codecs.open("source_file", "a", encoding="utf-8") as file:
                    file.write(source)
                time.sleep(2.7)
            except Exception as e:
                print(f"An error occurred on page {page}: {e}")


if __name__ == "__main__":
    get_pages = LogInGetPages(URL, USERNAME, PASSWORD)        
    get_pages.login_func()

