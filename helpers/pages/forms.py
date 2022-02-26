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

    def enter_first_name(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_first_name)

    def enter_last_name(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_last_name)

    def enter_email(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_email)

    def enter_radio_button_male(self):
        self.support_ui.find_element(*self.locators_forms.radio_button_male).click()

    def enter_mobile_number(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_mobile_number)

    def enter_date_birth(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_date_of_birth)

    def enter_subject(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_subject)

    def enter_hobbies(self):
        self.support_ui.find_element(*self.locators_forms.check_box_sports).click()
        self.support_ui.find_element(*self.locators_forms.check_box_reading).click()

    def enter_current_address(self, text):
        self.support_ui.enter_text(text, *self.locators_forms.field_current_address)

    #[Сценарий]
    def test_forms_practice_form(self):
        text_practice_form = "Practice Form"
        self.enter_button_forms()
        self.enter_button_practice_form()
        assert self.text_practice_form() == text_practice_form, "Не удалось открыть вкладку 'Practice Form'"
        self.enter_first_name("Temba")
        self.enter_last_name("Ketov")
        self.enter_email("ktv@list.ru")
        self.enter_radio_button_male()
        self.enter_mobile_number("+79887070034")
        self.enter_date_birth("12 May 2000")
        #self.enter_subject("Maths")
        self.enter_hobbies()
        self.enter_current_address("NLK")
