import pytest
from selene import browser, have, command
from selenium.webdriver import Keys
import time
import os.path


def test_registration_form():
    # Given
    browser.open("/automation-practice-form")
    # delete element fixedban
    browser.execute_script('document.querySelector("#fixedban").remove()')
    # delete element footer
    browser.element("footer").execute_script("element.remove()")
    # уменьшение масштаба страницы до 65%
    # browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")

    # When
    browser.element("#firstName").type("Igor")
    browser.element("#lastName").type("Degt")
    browser.element("#userEmail").type("div@novoch.ru")
    # bad selector (find for text)
    # browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    # good selector (find for value)
    browser.all("[name=gender]").element_by(have.value("Male")).element("..").click()
    browser.element("#userNumber").type("9185024041")
    browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL, "a").type(
        "04 august 1967"
    ).press_enter()
    browser.element("#subjectsInput").type("History").press_enter()
    # browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click() # клик на элементе без прокрутви
    # поиск элемента, прокрутка скрола и клик
    browser.all("[for^=hobbies-checkbox]").element_by(have.text("Sports")).perform(
        command.js.scroll_into_view
    ).click()
    import tests

    browser.element("#uploadPicture").send_keys(
        os.path.dirname(tests.__file__), "/files/ball.jpg"
    )
    browser.element("#currentAddress").type("Russian Novocherkassk")
    browser.element("#state").click()
    browser.all("[id^=react-select]").element_by(have.text("Rajasthan")).click()
    browser.element("#city").click()
    browser.all("[id^=react-select]").element_by(have.text("Jaipur")).click()
    browser.element("#submit").click()
    # time.sleep(3)

    # Then
    browser.element(".table").all("td").should(
        have.texts(
            ('Student Name', 'Igor Degt'),
            ('Student Email', 'div@novoch.ru'),
            ('Gender', 'Male'),
            ('Mobile', '9185024041'),
            ('Date of Birth', '04 August,1967'),
            ('Subjects', 'History'),
            ('Hobbies', 'Sports'),
            ('Picture', 'ball.jpg'),
            ('Address', 'Russian Novocherkassk'),
            ('State and City', 'Rajasthan Jaipur'),
        )
    )
