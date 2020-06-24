from selenium import webdriver
import os

class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser


    def getwebdriverinstance(self):
        baseurl = "https://letskodeit.com/"
        driver = None
        if self.browser == "chrome":
            chromedriver = "C:\\Selenium\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)

        elif self.browser == "firefox":
            driver = webdriver.firefox

        else:
            print("Enter valid browser")

        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver

