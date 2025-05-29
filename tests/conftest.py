import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 900
    browser.config.window_height = 600
    # вводим дпнные не посимвольно а строками с помощью JS
    # browser.config.type_by_js = True

    driver_options = webdriver.ChromeOptions()
    # не выводим на экран браузер
    # driver_options.add_argument('--headless=new')
    # закрываем сообщение что браузер запущен в отладочном режиме
    driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    browser.config.driver_options = driver_options

    yield

    browser.quit()
