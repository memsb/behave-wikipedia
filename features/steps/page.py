import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_browser_title(self):
        return self.driver.title

    def is_logged_in(self):
        try:
            self.driver.find_element_by_id("pt-userpage")
            return True
        except NoSuchElementException:
            return False

    def is_logged_out(self):
        try:
            self.driver.find_element_by_id("pt-anonuserpage")
            return True
        except NoSuchElementException:
            return False

    def has_login_link(self):
        return self.driver.find_element_by_id("pt-login").text == "Log in"

    def has_logout_link(self):
        return self.driver.find_element_by_id("pt-logout").text == "Log out"

    def click_login(self):
        login_link = self.driver.find_element_by_id("pt-login")
        login_link.click()

    def click_logout(self):
        logout_link = self.driver.find_element_by_id("pt-logout")
        logout_link.click()
        time.sleep(0.5)

    def search(self, text):
        search_field = self.driver.find_element_by_id("searchInput")
        search_field.send_keys(text)
        time.sleep(0.5)
        search_field.send_keys(Keys.ENTER)


class HomePage(BasePage):

    def get_section_titles(self):
        section_titles = self.driver.find_elements_by_class_name("mw-headline")
        return [t.text for t in section_titles]

    def has_section_titled(self, title):
        return title in self.get_section_titles()

    def get_welcome_message(self):
        return self.driver.find_element_by_id("mp-welcome").text



class SearchResultsPage(BasePage):
    def has_search_result(self, text):
        try:
            self.driver.find_element_by_link_text(text)
            return True
        except NoSuchElementException:
            return False


class ContentPage(BasePage):
    def get_heading(self):
        return self.driver.find_element_by_id("firstHeading").text


class LoginPage(BasePage):

    def login_with_credentials(self, username, password):
        login_form = self.driver.find_element_by_name("userlogin")
        username_field = self.driver.find_element_by_id("wpName1")
        password_field = self.driver.find_element_by_id("wpPassword1")

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_form.submit()

    def get_login_error(self):
        return self.driver.find_element_by_class_name('errorbox').text
