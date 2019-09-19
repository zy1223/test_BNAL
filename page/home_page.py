"""首页"""
from base.Base import Base
from page.page_elements import PageElements


class HomePage(Base):
    """首页"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_me_btn(self):
        """点击我"""
        self.click_element(PageElements.home_me_btn_id)
