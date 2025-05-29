import pytest
from selene import browser, have
import time

def test_registration_form():
    # Given
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()') # delete element fixedban
    browser.element('footer').execute_script('element.remove()') # delete element footer

    # When
    browser.element('#firstName').type('Igor')
    browser.element('#lastName').type('Degt')
    browser.element('#userEmail').type('div@novoch.ru')
    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('9185024041')

    time.sleep(3)

    #Then