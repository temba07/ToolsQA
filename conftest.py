import pytest
from application import Application

application = Application()


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    application.webdriver.maximize_window()
    yield
    application.webdriver.quit()
    return application


@pytest.fixture()
def elements():
    return application


@pytest.fixture()
def forms():
    return application
