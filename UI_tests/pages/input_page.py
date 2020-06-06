from UI_tests.pages.admin_product_page import AdminProductPage
from UI_tests.pages.selectors import MozillaPageSelectors


class InputPage(AdminProductPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser
        self.base_url = 'https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file'

    def load_file(self, path):
        iframe = self.find_element(MozillaPageSelectors.IFRAME)
        self.driver.switch_to_frame(iframe)
        input_element = self.find_dom_element(MozillaPageSelectors.INPUT_ELEMENT)
        input_element.send_keys(path)
