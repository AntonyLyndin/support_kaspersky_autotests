from framework.pages.help_page import HelpPage


class TestHelpPage:
    def test_check_sensor_ram_v40(self, driver):
        page = HelpPage(driver)
        page.load_page()

        page.open_industrial_cybersecurity_networks()
        page.choose_4_0_version()
        page.open_tab_hardware_software_requirements()

        text = page.search_text()

        assert text == 'RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer', \
            'This text was not found'

    def test_check_sensor_ram_v30(self, driver):
        page = HelpPage(driver)
        page.load_page()

        page.open_industrial_cybersecurity_networks()
        page.choose_3_0_version()
        page.open_tab_hardware_software_requirements()

        text = page.search_text()

        assert text == 'RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer.', \
            'This text was not found'

    def test_check_sensor_ram_v40_rus(self, driver):
        page = HelpPage(driver)
        page.load_page()

        page.open_industrial_cybersecurity_networks()
        page.choose_4_0_version()
        page.choose_rus_language()
        page.open_tab_hardware_software_requirements()

        text = page.search_text()

        assert text == 'объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;', \
            'This text was not found'
