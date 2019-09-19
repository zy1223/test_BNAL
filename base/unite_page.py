from page.home_page import HomePage
from page.login_page import LoginPage
from page.setting_page import SettingPage
from page.choice_login_page import ChoiceLoginPage
from page.person_page import PersonPage


class UnitePage(object):
    """统一页面入口类"""

    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        """首页"""
        return HomePage(self.driver)

    def choice_login(self):
        """登录选择页"""
        return ChoiceLoginPage(self.driver)

    def login_page(self):
        """登录页"""
        return LoginPage(self.driver)

    def person_page(self):
        """个人中心页"""
        return PersonPage(self.driver)

    def setting_page(self):
        """设置页"""
        return SettingPage(self.driver)
