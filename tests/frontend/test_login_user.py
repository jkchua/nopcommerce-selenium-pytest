from pages.login_page import FrontEndLoginPage

def test_login():

    FrontEndLoginPage.login("picogenkaku@gmail.com", "@Password123")