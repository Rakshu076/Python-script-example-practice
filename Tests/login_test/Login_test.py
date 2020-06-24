from Pages.LoginPage.LoginPage import LoginPage
import pytest
import time
import unittest

@pytest.mark.usefixtures("setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, setup):
        self.lp = LoginPage(self.driver)


    def test_login(self):
        self.lp.ecommercepractice()
        time.sleep(10)

