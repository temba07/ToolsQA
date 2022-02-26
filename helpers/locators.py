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

    button_radio_button = (By.XPATH, "//span [text() = 'Radio Button']")
    text_radio_button = (By.XPATH, "//div [text() = 'Radio Button']")
    button_yes = (By.XPATH, "//label [text() = 'Yes']")

    button_web_tables = (By.XPATH, "//span [text() = 'Web Tables']")
    text_web_tables = (By.XPATH, "//div [text() = 'Web Tables']")
    button_add = (By.CSS_SELECTOR, "#addNewRecordButton")
    field_first_name = (By.CSS_SELECTOR, "#firstName")
    field_last_name = (By.CSS_SELECTOR, "#lastName")
    field_email_wt = (By.CSS_SELECTOR, "#userEmail")
    field_age = (By.CSS_SELECTOR, "#age")
    field_salary = (By.CSS_SELECTOR, "#salary")
    field_department = (By.CSS_SELECTOR, "#department")
    button_submit_wt = (By.CSS_SELECTOR, "#submit")
    field_searchBox = (By.CSS_SELECTOR, "#searchBox")
    button_delete = (By.CSS_SELECTOR, "#delete-record-4")


class FormsLocators:
    button_forms = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]")
    button_practice_form = (By.XPATH, "//span [text() = 'Practice Form']")
    text_practice_form = (By.XPATH, "//div [text() = 'Practice Form']")

    field_first_name = (By.CSS_SELECTOR, "#firstName")
    field_last_name = (By.CSS_SELECTOR, "#lastName")
    field_email = (By.CSS_SELECTOR, "#userEmail")
    radio_button_male = (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label")
    field_mobile_number = (By.CSS_SELECTOR, "#userNumber")
    field_date_of_birth = (By.CSS_SELECTOR, "#dateOfBirthInput")
    field_subject = (By.XPATH, "//*[@id='subjectsContainer']/div/div[1]")
    check_box_sports = (By.XPATH, "//label [text() = 'Sports']")
    check_box_reading = (By.XPATH, "//label [text() = 'Reading']")
    field_current_address = (By.CSS_SELECTOR, "#currentAddress")
