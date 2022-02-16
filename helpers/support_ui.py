

class SupportUI:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def find_element(self, how, locator):
        return self.webdriver.find_element(how, locator)

    def enter_text(self, text, how, locator):
        self.webdriver.find_element(how, locator).send_keys(text)

    def scroll(self):
        self.webdriver.execute_script("window.scrollTo(0, 500)")
