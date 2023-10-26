from framework.pages.base_page import BasePage


class TestHelpPage:
    def test_check_sensor_ram_v40(self, driver):
        page = BasePage(driver)
        page.load_page()

    def test_check_sensor_ram_v30(self, driver):
        pass

    def test_check_sensor_ram_v40_rus(self, driver):
        pass
