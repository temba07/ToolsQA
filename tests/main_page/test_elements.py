import time


def test_elements_text_box(elements):
    elements.elements.test_elements_text_box()
    #elements.elements.enter_button_elements_exit()
    time.sleep(2)


def test_elements_check_box(elements):
    elements.elements.test_elements_check_box()
    time.sleep(2)


def test_elements_radio_button(elements):
    elements.elements.test_elements_radio_button()
    time.sleep(2)
