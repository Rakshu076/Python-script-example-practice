from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from Utilities.CustomLogger import CustomLogger as cl
from selenium.webdriver.common.action_chains import ActionChains
import logging.config


class SeleniumDriver:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def gettype(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "class":
            return By.CLASS_NAME
        else:
            self.log.error("locatortype= " + locatortype + " not found")
            print("locator type not valid")


    def getelement(self, locatortype, locator):
        locatortype = locatortype.lower()
        getype = self.gettype(locatortype)
        element = self.driver.find_element(getype, locator)
        self.log.info("element found ")
        return element

    def elementclick(self, locatortype, locator):
        element = self.getelement(locatortype, locator)
        element.click()
        self.log.info("clicked on element")
        self.log.error("not clicked")

    def sendkeys(self, data, locatortype, locator):
        element = self.getelement(locatortype, locator)
        element.send_keys(data)
        self.log.warning("data is loaded")

    def webdriverwait(self, locatortype, locator, timeout=25, poll_frequency=1 ):
        bytype = self.gettype(locatortype)
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions={NoSuchElementException})
            wait.until(EC.element_to_be_clickable((bytype, locator)))
        except:
            self.log.error("webdriverwait for element" + locatortype + "element not found")
            print("Element not found")

    def movetoelement(self, locatortype, locator):
        element = self.getelement(locatortype, locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()











