import time

from base.Base import Base
from page.page_elements import PageElements


class LoginPage(Base):
    """登录页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, username, password):
        time.sleep(3)
        """
        登录
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.send_element(PageElements.login_username_id, username)  # 输入账号
        time.sleep(2)
        self.send_element(PageElements.login_password_id, password)  # 输入密码
        self.click_element(PageElements.login_login_btn_id)  # 点击登录

    def get_login_btn_text(self):
        """返回登录按钮的文本信息"""
        return self.get_element(PageElements.login_login_btn_id).text

    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(PageElements.login_close_login_page_btn_id)
