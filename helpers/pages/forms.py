from ..locators import FormsLocators
from ..locators import ElementsLocators
from ..support_ui import SupportUI


class Forms:
    def __init__(self, webdriver):
        self.locators = ElementsLocators
        self.locators_forms = FormsLocators
        self.webdriver = webdriver
        self.support_ui = SupportUI(self.webdriver)

    #[Действия]
    def enter_button_forms(self):
        self.support_ui.find_element(*self.locators_forms.button_forms).click()

    def enter_button_practice_form(self):
        self.support_ui.find_element(*self.locators_forms.button_practice_form).click()

    def text_practice_form(self):
        return self.support_ui.find_element(*self.locators_forms.text_practice_form).text

    #[Сценарий]
    def test_forms_practice_form(self):
        text_practice_form = "Practice Form"
        self.enter_button_forms()
        self.enter_button_practice_form()
        assert self.text_practice_form() == text_practice_form, "Не удалось открыть вкладку 'Practice Form'"
