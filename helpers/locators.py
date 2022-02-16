from selenium.webdriver.common.by import By


class ElementsLocators:
    button_elements = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]/div/div[1]")
    button_elements_exit = (By.XPATH, "//div[text() = 'Elements'] /span")
    text_elements = (By.CSS_SELECTOR, "[class='main-header']")

    button_text_box = (By.XPATH, "//span [text() = 'Text Box']")
    text_text_box = (By.XPATH, "//div [text() = 'Text Box']")
    field_full_name = (By.CSS_SELECTOR, "#userName")
    field_email = (By.CSS_SELECTOR, "#userEmail")
    field_current_address = (By.CSS_SELECTOR, "#currentAddress")
    field_permanent_address = (By.CSS_SELECTOR, "#permanentAddress")
    button_submit = (By.CSS_SELECTOR, "#submit")

    button_check_box = (By.XPATH, "//span [text() = 'Check Box']")
    text_check_box = (By.XPATH, "//div [text() = 'Check Box']")
    button_plus = (By.CSS_SELECTOR, "[class='rct-icon rct-icon-expand-all']")
    button_minus = (By.CSS_SELECTOR, "[class='rct-icon rct-icon-collapse-all']")
    button_notes = (By.XPATH, "//span [text() = 'Notes']")
    button_commands = (By.XPATH, "//span [text() = 'Commands']")
