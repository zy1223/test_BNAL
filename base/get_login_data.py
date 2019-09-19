from base.get_data import GetData


class GetLoginData(object):
    """获取login数据类"""
    data = GetData().get_yaml_data('login_test_data_2.yml')
    data_suc_list = []
    data_dis_list = []
    for i in data:
        if data.get(i).get('toast') is None:
            data_suc_list.append(
                (i, data.get(i).get('username'), data.get(i).get('password'), data.get(i).get('exp_data')))
        else:
            data_dis_list.append(
                (i, data.get(i).get('username'), data.get(i).get('password'), data.get(i).get('toast'),
                 data.get(i).get('exp_data')))

    def get_login_suc_data(self):
        """获取正向测试用例数据"""
        return self.data_suc_list

    def get_login_dis_data(self):
        """获取逆向测试用例数据"""
        return self.data_dis_list
