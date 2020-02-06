import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
      help="Choose user browser language: en, ru, fr, etc...")
    parser.addoption('--browser_name', action='store', default='chrome',
      help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    # init browser instance with user language, default=en
    language = request.config.getoption("language")
    # init browser instance with chosen driver
    browser_name = request.config.getoption("browser_name")
    
    if browser_name == 'firefox':
      firefox_profile = webdriver.FirefoxProfile()
      firefox_profile.set_preference("intl.accept_languages", language)
      browser = webdriver.Firefox(firefox_profile=firefox_profile)
      print("\nstarting firefox browser...")
    else:
      chrome_options = Options()
      chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
      browser = webdriver.Chrome(options=chrome_options)
      print("\nstarting chrome browser...")

    # setting implicit wait
    browser.implicitly_wait(5)
    
    yield browser
    print("\nquit browser..")
    browser.quit()
