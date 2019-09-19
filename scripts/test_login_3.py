import allure
import pytest

from base.get_data import GetData
from base.unite_page import UnitePage
from base.get_driver import get_driver


def get_login_suc_data():
    """获取测试用例数据"""
    data = GetData().get_yaml_data('login_test_data_2.yml')
    data_suc_list = []
    data_dis_list = []
    for i in data:
        if data.get(i).get('toast') is None:
            data_suc_list.append(
                (i, data.get(i).get('username'), data.get(i).get('password'), data.get(i).get('exp_data')))
        else:
            data_dis_list.append((i, data.get(i).get('username'), data.get(i).get('password'), data.get(i).get('toast'),
                                  data.get(i).get('exp_data')))
    return data_suc_list


def get_login_dis_data():
    """获取测试用例数据"""
    data = GetData().get_yaml_data('login_test_data_2.yml')
    data_suc_list = []
    data_dis_list = []
    for i in data:
        if data.get(i).get('toast') is None:
            data_suc_list.append(
                (i, data.get(i).get('username'), data.get(i).get('password'), data.get(i).get('exp_data')))
        else:
            data_dis_list.append((i, data.get(i).get('username'), data.get(i).get('password'), data.get(i).get('toast'),
                                  data.get(i).get('exp_data')))
    return data_dis_list


class TestLogin(object):
    def setup_class(self):
        # 初始化driver
        self.driver = get_driver('com.yunmall.lc', 'com.yunmall.ymctoc.ui.activity.MainActivity')
        # 实例化统一入口类
        self.unite_page = UnitePage(self.driver)

    def teardown_class(self):
        # 退出driver
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def go_to_login(self):
        """跳转到登录页面,每次用例执行都要依赖一次"""
        # 点击我
        self.unite_page.home_page().click_me_btn()
        # 点击已有账号去登录
        self.unite_page.choice_login().click_exists_account_login()

    def judge_login_btn_exists(self):
        """判断登录按钮"""
        if "登录" in self.unite_page.login_page().get_login_btn_text():
            # 关闭登录页面
            self.unite_page.login_page().close_login_page()
        else:
            # 登录按钮不在此页面
            # 1、点击设置
            self.unite_page.person_page().click_setting_btn()
            # 2、退出
            self.unite_page.setting_page().logout()

    @pytest.mark.parametrize('case_num, username, pwd, exp_data', get_login_suc_data())
    def test_suc_login(self, case_num, username, pwd, exp_data):
        """
        预期成功
        :param case_num: 用例编号
        :param username: 用户名
        :param pwd: 密码
        :param exp_data: 预期结果
        :return:
        """
        allure.attach('登录正向测试', '编号：%s,预期结果：%s' % (case_num, exp_data))
        # 登录
        self.unite_page.login_page().login(username, pwd)
        # 判断我的收藏是否在个人中心页面
        if exp_data in self.unite_page.person_page().get_text_my_shopping_cart():
            # 在==退出
            # 1、点击设置
            self.unite_page.person_page().click_setting_btn()
            # 2、退出
            self.unite_page.setting_page().logout()
        else:
            # 不在==判断登录按钮是否在此页面
            self.judge_login_btn_exists()

    @pytest.mark.parametrize('case_num, username, pwd,toast, exp_data', get_login_dis_data())
    def test_fail_login(self, case_num, username, pwd, toast, exp_data):
        """
        预期失败
        :param case_num: 用例编号
        :param username: 用户名
        :param pwd: 密码
        :param toast:消息拼接语句
        :param exp_data: 预期结果
        :return:
        """
        allure.attach('登录逆向测试', '编号：%s,预期结果：%s' % (case_num, exp_data,))
        # 登录
        self.unite_page.login_page().login(username, pwd)

        # 判断预期结果是否在获取的toast文本信息中
        # toast_info_text = self.unite_page.login_page().get_toast(toast)
        if exp_data in self.unite_page.login_page().get_toast(toast):
            # 预期结果在获取的toast文本信息中==>判断登录按钮
            self.judge_login_btn_exists()
        else:
            # 预期结果不在获取的toast文本信息中
            self.judge_login_btn_exists()
