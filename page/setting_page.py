from base.Base import Base
from page.page_elements import PageElements


class SettingPage(Base):
    """设置页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):
        """退出登录"""
        # 向上滑动屏幕
        self.swipe_screen()
        # 点击退出
        self.click_element(PageElements.setting_logout_btn)
        if tag == 1:
            # 点击确认退出
            self.click_element(PageElements.setting_act_logout_btn)
        else:
            # 点击取消
            self.click_element(PageElements.setting_dis_logout_btn)
