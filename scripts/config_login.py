from selenium.webdriver.common.by import By

from base.unite_page import UnitePage
from base.get_driver import get_driver
from appium import webdriver

# 声明driver
driver = get_driver('com.yunmall.lc', 'com.yunmall.ymctoc.ui.activity.MainActivity')
unite_page = UnitePage(driver)
# 点击我
unite_page.home_page().click_me_btn()
# 选择已有账号去登录
unite_page.choice_login().click_exists_account_login()
# 登录
unite_page.login_page().login('13606463805', 'zy131412')
# 获取toast消息
toast_info = unite_page.login_page().get_toast("错误")
print(toast_info)
# # 打印我的收藏
# text = unite_page.person_page().get_text_my_shopping_cart()
# print('个人中心：', text)
# # 点击设置
# unite_page.person_page().click_setting_btn()
# # 退出
# unite_page.setting_page().logout()
