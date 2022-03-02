from selenium import webdriver
from helpers.pages.elements import Elements
from helpers.pages.forms import Forms
from helpers.pages.alerts_frame_and_windows import AlertsFrameAndWindows


class Application:
    def __init__(self):
        self.link = "https://demoqa.com/"
        self.webdriver = webdriver.Chrome()
        self.webdriver.get(self.link)
        self.webdriver.implicitly_wait(5)

        self.elements = Elements(self.webdriver)
        self.forms = Forms(self.webdriver)
        self.alerts_frame_and_windows = AlertsFrameAndWindows(self.webdriver)

