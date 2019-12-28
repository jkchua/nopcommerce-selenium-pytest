from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

MENU_LOGIN_LINK = (By.CLASS_NAME, "ico-login")
LOGIN_EMAIL_TEXTBOX = (By.ID, "Email")
LOGIN_PASSWORD_TEXTBOX = (By.ID, "Password")
LOGIN_LOGIN_BUTTON = (By.XPATH, "//*[@type='submit' and @value='Log in']")

class FrontEndLoginPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        
    def login(email, password):
        
        loginPage = FrontEndLoginPage()

        loginPage.visit(loginPage.base_url)
        loginPage.find_element(MENU_LOGIN_LINK).click()

        loginPage.find_element(LOGIN_EMAIL_TEXTBOX).click()
        loginPage.find_element(LOGIN_EMAIL_TEXTBOX).send_keys(email)

        loginPage.find_element(LOGIN_PASSWORD_TEXTBOX).click()
        loginPage.find_element(LOGIN_PASSWORD_TEXTBOX).send_keys(password)

        loginPage.find_element(LOGIN_LOGIN_BUTTON).click()
   
        assert "nopCommerce demo store" in loginPage.browser.title