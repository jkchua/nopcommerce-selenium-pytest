from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time

class BasePage(object):

    # Initialize WebDriver.
    def __init__(self, base_url="https://demo.nopcommerce.com/"):

        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.maximize_window()
        
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    # Generic method to find an element, given a tuple.
    # Example of tuple: (By.ID, "idName")
    def find_element(self, location):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(location))

    # Generic method for visiting a website.
    def visit(self, url):
        self.browser.get(url)

    # Generic method for executing hover from one element to another. 
    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        time.sleep(5)
  
    # Generic method that displays a message that a method doesn't exist. 
    def method_missing(self, what):
        print("No %s here!"%what)