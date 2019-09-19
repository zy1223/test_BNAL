import os

import yaml


class GetData(object):
    def get_yaml_data(self, name):
        """
        获取yaml数据
        :param name: 需要读取的文件的名字
        :return:
        """
        with open('.' + os.sep + 'data' + os.sep + name, 'r', encoding='utf-8') as f:
            # with open('E:\\3_app_code\\day10\\self\\data'+os.sep + name, encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data
