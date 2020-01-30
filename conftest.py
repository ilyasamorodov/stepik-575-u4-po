import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Select user browser language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is not None:
        # init browser instance with user language
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        print("\nstart browser...")
    else:
        raise pytest.UsageError("--language should be set. Examples: ru, en, fr, es")
    yield browser
    print("\nquit browser..")
    browser.quit()
