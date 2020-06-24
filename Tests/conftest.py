import pytest
from Base.WebDriverFactory import WebDriverFactory


@pytest.fixture(scope="class")
def setup(request, browser):

    wdf = WebDriverFactory(browser)
    driver = wdf.getwebdriverinstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")




