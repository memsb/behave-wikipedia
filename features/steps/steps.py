import os

from selenium.common.exceptions import NoSuchElementException

from page import HomePage, LoginPage, ContentPage, SearchResultsPage
from hamcrest import *


@given('I am on the Wikipedia homepage')
def visit_wikipedia(context):
    context.driver.get("https://en.wikipedia.org")


@given('I am not logged in')
def step_impl(context):
    home_page = HomePage(context.driver)
    if home_page.is_logged_in():
        home_page.click_logout()


@given('I am logged in')
def step_impl(context):
    username = os.environ.get('WIKIPEDIA_USERNAME')
    password = os.environ.get('WIKIPEDIA_PASSWORD')

    home_page = HomePage(context.driver)
    if home_page.is_logged_out():
        home_page.click_login()
        login_page = LoginPage(context.driver)
        login_page.login_with_credentials(username, password)


@when('I search for "{text}"')
def step_impl(context, text):
    home_page = HomePage(context.driver)
    home_page.search(text)


@when('I log in')
def step_impl(context):
    username = os.environ.get('WIKIPEDIA_USERNAME')
    password = os.environ.get('WIKIPEDIA_PASSWORD')

    home_page = HomePage(context.driver)
    home_page.click_login()
    login_page = LoginPage(context.driver)
    login_page.login_with_credentials(username, password)


@when('I click the log out link')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_logout()


@when('I attempt to log in with invalid credentials')
def step_impl(context):
    username = os.environ.get('WIKIPEDIA_USERNAME')
    password = 'INVALID_PASSWORD'

    home_page = HomePage(context.driver)
    home_page.click_login()
    login_page = LoginPage(context.driver)
    login_page.login_with_credentials(username, password)


@then('I should see a search result for "{text}"')
def step_impl(context, text):
    results_page = SearchResultsPage(context.driver)
    assert_that(results_page.has_search_result(text))


@then('I should be sent to the page for "{text}"')
def step_impl(context, text):
    content_page = ContentPage(context.driver)
    assert_that(content_page.get_browser_title(), contains_string(text))
    assert_that(content_page.get_heading(), equal_to(text))


@then('I should see a welcome message')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert_that(home_page.get_welcome_message(), contains_string("Welcome to Wikipedia"))


@then('I should see a section titled "{title}"')
def step_impl(context, title):
    home_page = HomePage(context.driver)
    assert_that(home_page.has_section_titled(title))


@then('I should be logged in')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert_that(home_page.is_logged_in())


@then('I should see a link to log in')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert_that(home_page.has_login_link())


@then('I should see a link to log out')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert_that(home_page.has_logout_link())


@then('I will be logged out')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert_that(home_page.is_logged_out())


@then('I will not be logged in')
def step_impl(context):
    login_page = LoginPage(context.driver)
    assert_that(login_page.is_logged_out())


@then('I should see a login error message')
def step_impl(context):
    login_page = LoginPage(context.driver)
    assert_that(login_page.get_login_error(), any_of(
        contains_string("Incorrect username or password entered."),
        contains_string("There are problems with some of your input.")
    ))
