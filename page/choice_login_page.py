from base.Base import Base
from page.page_elements import PageElements


class ChoiceLoginPage(Base):
    """选择登录页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exists_account_login(self):
        """点击已有账号去登录"""
        self.click_element(PageElements.choice_login_exist_account_login_btn_id)
