from base.Base import Base
from page.page_elements import PageElements


class PersonPage(Base):
    """个人中心页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_setting_btn(self):
        """点击设置"""
        self.click_element(PageElements.person_setting_btn_id)

    def get_text_my_shopping_cart(self):
        """返回我的收藏文本信息"""
        return self.get_element(PageElements.person_my_shopping_cart_id).text
