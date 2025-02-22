import pytest
import selenium.webdriver
import json
from pages.test_home import OpenCartHomePage
from pages.test_search import OpenCartSearchPage



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
    # Initialize the WebDriver instance
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


    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()

@pytest.fixture
def home_page(browser):
    #fixture to initialize and return the opencart home page
    page = OpenCartHomePage(browser)
    page.load()  
    return page

@pytest.fixture
def search_page(browser):
    #fixture to initialize and return the opencart search page
    return OpenCartSearchPage(browser)

