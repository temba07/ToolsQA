from ..locators import ElementsLocators
from ..support_ui import SupportUI


class Elements:
    def __init__(self, webdriver):
        self.locators = ElementsLocators
        self.webdriver = webdriver
        self.support_ui = SupportUI(self.webdriver)

    # [Действия]
    def enter_button_elements(self):
        self.support_ui.find_element(*self.locators.button_elements).click()

    def enter_button_elements_exit(self):
        self.support_ui.find_element(*self.locators.button_elements_exit).click()

    def text_elements(self):
        return self.support_ui.find_element(*self.locators.text_elements).text

    def enter_text_box(self):
        self.support_ui.find_element(*self.locators.button_text_box).click()

    def text_text_box(self):
        return self.support_ui.find_element(*self.locators.button_text_box).text

    def enter_full_name(self, text):
        self.support_ui.enter_text(text, *self.locators.field_full_name)

    def enter_email(self, text):
        self.support_ui.enter_text(text, *self.locators.field_email)

    def enter_current_address(self, text):
        self.support_ui.enter_text(text, *self.locators.field_current_address)

    def enter_permanent_address(self, text):
        self.support_ui.enter_text(text, *self.locators.field_permanent_address)

    def press_button_submit(self):
        self.support_ui.scroll()
        self.support_ui.find_element(*self.locators.button_submit).click()

    def enter_check_box(self):
        self.support_ui.find_element(*self.locators.button_check_box).click()

    def text_check_box(self):
        return self.support_ui.find_element(*self.locators.text_check_box).text

    def enter_plus(self):
        self.support_ui.find_element(*self.locators.button_plus).click()

    def enter_minus(self):
        self.support_ui.find_element(*self.locators.button_minus).click()

    def select_notes(self):
        self.support_ui.find_element(*self.locators.button_notes).click()

    def select_commands(self):
        self.support_ui.find_element(*self.locators.button_commands).click()

    def enter_radio_button(self):
        self.support_ui.find_element(*self.locators.button_radio_button).click()

    def text_radio_button(self):
        return self.support_ui.find_element(*self.locators.text_radio_button).text

    def enter_yes(self):
        self.support_ui.find_element(*self.locators.button_yes).click()

    def enter_web_tables(self):
        self.support_ui.find_element(*self.locators.button_web_tables).click()

    def text_web_tables(self):
        return self.support_ui.find_element(*self.locators.text_web_tables).text

    def enter_add(self):
        self.support_ui.find_element(*self.locators.button_add).click()

    def enter_firs_name(self, text):
        self.support_ui.enter_text(text, *self.locators.field_first_name)

    def enter_last_name(self, text):
        self.support_ui.enter_text(text, *self.locators.field_last_name)

    def enter_email_wt(self, text):
        self.support_ui.enter_text(text, *self.locators.field_email_wt)

    def enter_age(self, text):
        self.support_ui.enter_text(text, *self.locators.field_age)

    def enter_salary(self, text):
        self.support_ui.enter_text(text, *self.locators.field_salary)

    def enter_department(self, text):
        self.support_ui.enter_text(text, *self.locators.field_department)

    def enter_button_submit(self):
        self.support_ui.find_element(*self.locators.button_submit_wt).click()

    def enter_search_box(self,text):
        self.support_ui.enter_text(text, *self.locators.field_searchBox)

    def enter_delete(self):
        self.support_ui.find_element(*self.locators.button_delete).click()

    # [Сценарии]
    def test_elements_text_box(self):
        text_elements = "Elements"
        text_text_box = "Text Box"
        self.enter_button_elements()
        assert self.text_elements() == text_elements, "Ошибка входа. Страница 'Elements'"
        self.enter_text_box()
        assert self.text_text_box() == text_text_box, "Не удалось открыть вкладку 'Text Box'"
        self.enter_full_name("Tembulat")
        self.enter_email("ktv@list.ru")
        self.enter_current_address("KBR, Nalchik, Lenina 1")
        self.enter_permanent_address("KBR, Nalchik, Lenina 1")
        self.press_button_submit()

    def test_elements_check_box(self):
        text_elements = "Elements"
        text_check_box = "Check Box"
        self.enter_button_elements()
        assert self.text_elements() == text_elements, "Ошибка входа. Страница 'Elements'"
        self.enter_check_box()
        assert self.text_check_box() == text_check_box, "Не удалось открыть вкладку 'Check Box'"
        self.enter_plus()
        self.select_notes()
        self.select_commands()
        self.enter_minus()

    def test_elements_radio_button(self):
        text_elements = "Elements"
        text_radio_button = "Radio Button"
        self.enter_button_elements()
        assert self.text_elements() == text_elements, "Ошибка входа. Страница 'Elements'"
        self.enter_radio_button()
        assert self.text_radio_button() == text_radio_button, "Не удалось открыть вкладку 'Radio Button'"
        self.enter_yes()

    def test_elements_web_tables(self):
        text_elements = "Elements"
        text_web_tables = "Web Tables"
        self.enter_button_elements()
        assert self.text_elements() == text_elements, "Ошибка входа. Страница 'Elements'"
        self.enter_web_tables()
        assert self.text_web_tables() == text_web_tables, "Не удалось открыть вкладку 'Web Tables'"
        self.enter_add()
        self.enter_firs_name("Tembulat")
        self.enter_last_name("Ketov")
        self.enter_email_wt("ketv@list.ru")
        self.enter_age("21")
        self.enter_salary("70000")
        self.enter_department("QA Automation Engineer")
        self.enter_button_submit()
        self.enter_search_box("Ketov")
        self.enter_delete()
