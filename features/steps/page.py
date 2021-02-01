
class BasePage:

    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    pass

class SearchResultsPage(BasePage):
    pass

class ContentPage(BasePage):
    pass

class LoginPage(BasePage):
    pass