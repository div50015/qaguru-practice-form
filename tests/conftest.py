import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1900
    browser.config.window_height = 1080

    # browser.config.type_by_js = True
    #
    # driver_options = webdriver.ChromeOptions()
    # # driver_options.add_argument('--headless=new')
    # driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # browser.config.driver_options = driver_options

    # уменьшение масштаба страницы до 65%
    # browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")
    # закрываем сообщение что браузер запущен в отладочном режиме
    # browser.execute_script('document.querySelector("#fixedban").remove()')
    # browser.element('footer').execute_script('element.remove()')

    yield

    browser.quit()
