from selene import browser, have, command
from selene.support.conditions.have import values_containing
from selenium.webdriver import Keys
import tests
import os


class RegistrationPanel:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.user_email = browser.element("#userEmail")
        self.user_number = browser.element("#userNumber")
        self.user_subjects = browser.element("#subjectsInput")
        self.user_hobbies = browser.all('[for^=hobbies-checkbox]')
        self.user_picture = browser.element("#uploadPicture")
        self.user_address = browser.element("#currentAddress")

        self.user_address = browser.element("#currentAddress")

        self.user_state = browser.element("#state")
        self.choose_state = browser.all("[id^=react-select]")
        self.user_city = browser.element("#city")
        self.choose_city = browser.all("[id^=react-select]")
        self.user_submit = browser.element("#submit")

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_user_email(self, value):
        self.user_email.type(value)

    def choose_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()

    def fill_user_namber(self, value):
        self.user_number.type("9185024041")

    def fill_user_date_of_birth(self, value):
        browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL, "a").type(
            value
        ).press_enter()

    def choose_subjects(self, value):
        self.user_subjects.type(value).press_enter()

    def choose_user_hobbies(self, value):
        self.user_hobbies.element_by(have.text(value)).perform(
            command.js.scroll_into_view
        ).click()

    def chose_user_picrure(self, value):
        self.user_picture.send_keys(os.path.dirname(tests.__file__), value)

    def fill_user_address(self, value):
        self.user_address.type(value)

    def choose_user_state(self, value):
        self.user_state.click()
        self.choose_state.element_by(have.text(value)).click()
        # browser.element("#state").click()
        # browser.all("[id^=react-select]").element_by(have.text("Rajasthan")).click()

    def choose_user_city(self, value):
        self.user_city.click()
        self.choose_city.element_by(have.text(value)).click()
        # browser.element("#city").click()
        # browser.all("[id^=react-select]").element_by(have.text("Jaipur")).click()

    def click_buttom(self):
        self.user_submit.click()

    def should_registration(self):
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
