from ..locators import AlertsFrameAndWindowsLocators
from ..support_ui import SupportUI


class AlertsFrameAndWindows:
    def __init__(self, webdriver):
        self.locators_alerts_frame_and_windows = AlertsFrameAndWindowsLocators
        self.webdriver = webdriver
        self.support_ui = SupportUI(self.webdriver)

    # [Действия]
    def enter_button_alerts_frame_and_windows(self):
        self.support_ui.find_element(*self.locators_alerts_frame_and_windows.button_alerts_frame_and_windows).click()

    def text_alerts_frame_and_windows(self):
        return self.support_ui.find_element(*self.locators_alerts_frame_and_windows.text_alerts_frame_and_windows).text

    # [Сценарий]
    def test_alerts_frame_and_windows(self):
        text_alerts_frame_and_windows = "Alerts, Frame & Windows"
        self.enter_button_alerts_frame_and_windows()
        assert self.text_alerts_frame_and_windows() == text_alerts_frame_and_windows, "Не удалось открыть вкладку " \
                                                                                      "'Alerts, Frame & Windows'"
