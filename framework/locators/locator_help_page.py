from selenium.webdriver.common.by import By


class LocatorMainPage:
    INDUSTRIAL_CUBER_SECURITY_NETWORKS = (By.CSS_SELECTOR, '[data-url="/KICSforNetworks/4.0/en-US"]')


class LocatorKICSNetworkPage:

    SPAN_VERSION = (By.CSS_SELECTOR, '.top-bar__versions.js_header_versions_list div')
    SPAN_LANGUAGE = (By.CSS_SELECTOR, '.js_header_lang_list div')

    VERSION_4_0 = (By.XPATH, '//div[@class="top-bar__langs"]//a[text()=4.0]')
    VERSION_3_0 = (By.XPATH, '//div[@class="top-bar__langs"]//a[text()=3.0]')

    LANGUAGE_RUS = (By.CSS_SELECTOR, '.header-wrapper.js_header_placeholder [data-lang-id="ru-RU"]')

    CHAPTER_HARDWARE_SOFTWARE_REQUIREMENTS = (By.CSS_SELECTOR, '.contents__item.js_menu_item [href="102347.htm"]')

    VERIFICATION_TEXT = (By.CSS_SELECTOR, 'ul:nth-child(7) > li:nth-child(2) > ul > li:nth-child(2)')
