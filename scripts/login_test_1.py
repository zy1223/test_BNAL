import sys, os

sys.path.append(os.getcwd())
import allure
import pytest

from base.unite_page import UnitePage
from base.get_driver import get_driver
from base.get_data import GetData


def get_login_data():
    data = GetData().get_yaml_data('login_data_1.yml')
    """
    {'login_data': {'test_num1': {'username': 13606463805, 'password': 'zy1314,,', 'exp': '我的收藏'}}}
    """
    data_values = data.get('login_data')
    data_list = []
    for i in data_values.keys():
        data_list.append(
            (i, data_values.get(i).get('username'), data_values.get(i).get('password'), data_values.get(i).get('exp')))
    return data_list


# print(get_login_data())



class TestLogin(object):
    """登录测试"""

    def setup_class(self):
        self.driver = get_driver('com.yunmall.lc', 'com.yunmall.ymctoc.ui.activity.MainActivity')
        self.unit_page = UnitePage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('test_num,username,password,exp', get_login_data())
    def test_login(self, test_num, username, password, exp):
        allure.attach('登录测试', '%s  预期：%s' % (test_num, exp))
        # 点击我
        self.unit_page.home_page().click_me_btn()
        # 选择已有账号去登录
        self.unit_page.choice_login().click_exists_account_login()
        # 登录
        self.unit_page.login_page().login(username, password)
        # 断言
        assert exp in self.unit_page.person_page().get_text_my_shopping_cart()
        # 点击设置
        self.unit_page.person_page().click_setting_btn()
        # 退出登录
        self.unit_page.setting_page().logout()
