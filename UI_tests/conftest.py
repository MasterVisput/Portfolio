import logging

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver

from UI_tests.pages.admin_categories_page import AdminCategoriesPage
from UI_tests.pages.admin_product_page import AdminProductPage
from UI_tests.pages.input_page import InputPage
from UI_tests.pages.listener import MyListener

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='This is browser for testing'
    )


@pytest.fixture
def browser_opt(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def browser(browser_opt):
    if browser_opt == 'Chrome':
        caps = DesiredCapabilities.CHROME
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        browser = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=caps), MyListener())
    elif browser_opt == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--kiosk')
        browser = EventFiringWebDriver(webdriver.Firefox(), MyListener())
        profile.accept_untrusted_certs = True
    elif browser_opt == 'IE':
        browser = EventFiringWebDriver(webdriver.Ie(), MyListener())
    yield browser
    browser.quit()


@pytest.fixture()
def admin_product_page(browser):
    logger.info('====================Start Setup Activity====================')
    page = AdminProductPage(browser)
    page.open()
    page.login_admin()
    page.go_to_product_tab()
    logger.info('====================End Setup Activity====================')
    return page


@pytest.fixture()
def setup_product_page(admin_product_page):
    if not admin_product_page.is_product_in_tab(p_name='Mouse'):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')


@pytest.fixture()
def admin_categories_page(browser):
    logger.info('====================Start Setup Activity====================')
    page = AdminCategoriesPage(browser)
    page.open()
    page.login_admin()
    page.go_to_categories()
    logger.info('====================End Setup Activity====================')
    return page


@pytest.fixture()
def input_page(browser):
    page = InputPage(browser)
    page.open()
    return page
