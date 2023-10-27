from framework.pages.base_page import BasePage
from framework.locators.locator_help_page import LocatorMainPage as LocatorMP
from framework.locators.locator_help_page import LocatorKICSNetworkPage as LocatorKICS
from config.urls import HELP_PAGE_URL


class HelpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = HELP_PAGE_URL

    def open_industrial_cybersecurity_networks(self):
        element = self.find_element(LocatorMP.INDUSTRIAL_CUBER_SECURITY_NETWORKS)
        element.click()

    def choose_4_0_version(self):
        self.__open_span_version()

        element = self.find_element(LocatorKICS.VERSION_4_0)
        element.click()

    def choose_3_0_version(self):
        self.__open_span_version()

        element = self.find_element(LocatorKICS.VERSION_3_0)
        element.click()

    def choose_rus_language(self):
        self.__open_span_language()

        element = self.find_element(LocatorKICS.LANGUAGE_RUS)
        element.click()

    def open_tab_hardware_software_requirements(self):
        element = self.find_element(LocatorKICS.CHAPTER_HARDWARE_SOFTWARE_REQUIREMENTS)
        element.click()

    def search_text(self):
        element = self.find_element(LocatorKICS.VERIFICATION_TEXT)

        return element.text

    def __open_span_version(self):
        element = self.find_element(LocatorKICS.SPAN_VERSION)
        element.click()

    def __open_span_language(self):
        element = self.find_element(LocatorKICS.SPAN_LANGUAGE)
        element.click()
