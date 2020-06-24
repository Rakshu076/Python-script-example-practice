from Base.SeleniumDriver import SeleniumDriver
from Utilities.CustomLogger import CustomLogger as cl
import logging


class LoginPage():
    log =cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.sd = SeleniumDriver(driver)


    #locators
    practicelink = "//li[@id='menu-item-1450']/a/span[1]"
    ecommercelink = "menu-item-1700"


    def ecommercepractice(self):
        self.sd.movetoelement("xpath", self.practicelink)

        self.sd.getelement("id", self.ecommercelink).click()




