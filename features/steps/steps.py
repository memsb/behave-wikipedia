import time
import os
from hamcrest import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def am_logged_in(context):
    try:
        return context.driver.find_element_by_id("pt-logout").text == "Log out" \
               and context.driver.find_element_by_id("pt-userpage")
    except NoSuchElementException:
        return False


def am_logged_out(context):
    try:
        return context.driver.find_element_by_id("pt-login").text == "Log in"
    except NoSuchElementException:
        return False


def log_in(context):
    context.driver.save_screenshot(f"output/before_login_link.png")
    login_link = context.driver.find_element_by_id("pt-login")
    login_link.click()

    context.driver.save_screenshot(f"output/before_login_form.png")
    login_form = context.driver.find_element_by_name("userlogin")
    username_field = context.driver.find_element_by_id("wpName1")
    password_field = context.driver.find_element_by_id("wpPassword1")

    username_field.send_keys(os.environ.get('WIKIPEDIA_USERNAME'))
    password_field.send_keys(os.environ.get('WIKIPEDIA_PASSWORD'))

    context.driver.save_screenshot(f"output/before_login_form_submit.png")
    login_form.submit()

    context.driver.save_screenshot(f"output/after_login_form_submit.png")


def log_out(context):
    logout_link = context.driver.find_element_by_id("pt-logout")
    logout_link.click()


@given('I am on the Wikipedia homepage')
def visit_wikipedia(context):
    context.driver.get("https://en.wikipedia.org")


@given('I am not logged in')
def step_impl(context):
    if am_logged_in(context):
        log_out(context)


@given('I am logged in')
def step_impl(context):
    if am_logged_out(context):
        log_in(context)


@given('I visit via the url "{url}"')
def step_impl(context, url):
    context.driver.get(f"https://{url}")


@when('I search for "{text}"')
def step_impl(context, text):
    search_field = context.driver.find_element_by_id("searchInput")
    search_field.send_keys(text)
    time.sleep(2)
    search_field.send_keys(Keys.ENTER)

    # time.sleep(2)


@when('I log in')
def step_impl(context):
    log_in(context)


@when('I click the log out link')
def step_impl(context):
    context.driver.save_screenshot(f"output/before_logout.png")
    logout_link = context.driver.find_element_by_id("pt-logout")
    logout_link.click()

    context.driver.save_screenshot(f"output/clicked_logout.png")


@then('I should see a search result for "{text}"')
def step_impl(context, text):
    context.driver.find_element_by_link_text(text)


@then('I should be sent to the page for "{text}"')
def step_impl(context, text):
    heading = context.driver.find_element_by_id("firstHeading").text
    page_title = context.driver.title

    try:
        assert_that(page_title, contains_string(text))
        assert_that(heading, equal_to(text))
    except:
        context.driver.save_screenshot(f"output/{text}.png")
        raise


@then('I should see a welcome message')
def step_impl(context):
    context.driver.find_element_by_id("mp-welcome")


@then('I should see a section titled "{title}"')
def step_impl(context, title):
    section_titles = context.driver.find_elements_by_class_name("mw-headline")
    titles = [t.text for t in section_titles]

    assert title in titles


@then('I should be logged in')
def step_impl(context):
    assert am_logged_in(context)


@then('I should see a link to log in')
def step_impl(context):
    context.driver.save_screenshot(f"output/see_login_link.png")
    assert context.driver.find_element_by_id("pt-login").text == "Log in"


@then('I should see a link to log out')
def step_impl(context):
    context.driver.save_screenshot(f"output/see_logout_link.png")
    assert context.driver.find_element_by_id("pt-logout").text == "Log out"


@then('I will be logged out')
def step_impl(context):
    context.driver.save_screenshot(f"output/logged_out.png")
    assert am_logged_out(context)
