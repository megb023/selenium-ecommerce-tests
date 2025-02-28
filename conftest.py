import os

import pytest
import selenium.webdriver
import json
from pages.test_home import OpenCartHomePage
from pages.test_search import OpenCartSearchPage
from pages.test_cart import OpenCartCartPage

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):
    """ Initialize the webdriver instance"""
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    b.maximize_window()
    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()

@pytest.fixture
def home_page(browser):
    """fixture to initialize and return the opencart home page"""
    page = OpenCartHomePage(browser)
    page.load()  
    return page

@pytest.fixture
def search_page(browser):
    """Fixture to initialize and return the OpenCart cart page"""
    page = OpenCartSearchPage(browser)
    return page

@pytest.fixture
def cart_page(browser):
    """Fixture to initialize and return the OpenCart cart page"""
    page = OpenCartCartPage(browser)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to take actions after a test runs."""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Get the browser instance from fixtures
            browser = item.funcargs.get("browser")  
            if browser:
                reports_dir = os.path.join(os.path.dirname(__file__), "reports", "tests")
                os.makedirs(reports_dir, exist_ok=True)  # Ensure the directory exists
                
                relative_path = os.path.join("reports", report.nodeid.replace("::", "_") + ".png")
                absolute_path = os.path.join(os.path.dirname(__file__), relative_path)
                print(f"Saving screenshot to: {absolute_path}")
                _capture_screenshot(browser, absolute_path)  # Pass browser to function

                html = (
                    f'<div><img src="{relative_path}" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extras = extra
                                     
def _capture_screenshot(browser, file_name):
    browser.get_screenshot_as_file(file_name)

