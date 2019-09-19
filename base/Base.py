import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组（By.ID,属性值），（By.CLASS_NAME,属性值），（By.XPATH,属性值）
        :param timeout: 超时时间10
        :param poll_frequency: 间隔时长1.0
        :return:定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元组（By.ID,属性值），（By.CLASS_NAME,属性值），（By.XPATH,属性值）
        :param timeout: 超时时间10
        :param poll_frequency: 间隔时长1.0
        :return:定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击方法
        :param loc: 元组（By.ID,属性值），（By.CLASS_NAME,属性值），（By.XPATH,属性值）
        :return:
        """
        self.get_element(loc).click()

    def send_element(self, loc, text):
        """
        输入方法
        :param loc:
        :param text: 元组（By.ID,属性值），（By.CLASS_NAME,属性值），（By.XPATH,属性值）
        :return:
        """
        self.get_element(loc).clear()
        self.get_element(loc).send_keys(text)

    def swipe_screen(self, tag=1):
        time.sleep(2)
        """
        滑动屏幕，默认向上滑动屏幕
        :param tag:1向上，2向下，3向左，4向右
        :return:
        """
        size = self.driver.get_window_size()  # 获取屏幕尺寸大小
        width = size.get('width')  # 获取屏幕宽
        height = size.get('height')  # 获取屏幕高
        if tag == 1:
            # 向上滑动 宽0.5，高0.8->高0.3
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3)
        elif tag == 2:
            # 向下滑动 宽0.5，高0.3->高0.8
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8)
        elif tag == 3:
            # 向左滑动 高0.5，宽0.8->宽0.3
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5)
        elif tag == 4:
            # 向右滑动 高0.5，宽0.3->宽0.8
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)

    def get_toast(self, mess):
        """
        获取toast消息
        :param mess: 要获取的toast消息中的部分文本内容
        :return:
        """
        message = (By.XPATH, '//*[contains(@text,"%s")]' % mess)
        return self.get_element(message, timeout=3, poll_frequency=0.3).text
