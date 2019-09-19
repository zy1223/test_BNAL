from selenium.webdriver.common.by import By


class PageElements(object):
    """页面元素类"""
    """百年奥莱首页"""
    # 我
    home_me_btn_id = (By.ID, 'com.yunmall.lc:id/tab_me')
    """登录选择页面"""
    # 已有账号去登录
    choice_login_exist_account_login_btn_id = (By.ID, 'com.yunmall.lc:id/textView1')
    """登录页面"""
    # ×号==关闭登录页面按钮
    login_close_login_page_btn_id = (By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image')
    # 账号
    login_username_id = (By.ID, 'com.yunmall.lc:id/logon_account_textview')
    # 密码
    login_password_id = (By.ID, 'com.yunmall.lc:id/logon_password_textview')
    # 登录按钮
    login_login_btn_id = (By.ID, 'com.yunmall.lc:id/logon_button')
    """个人中心页面"""
    # 设置按钮
    person_setting_btn_id = (By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image')
    # 我的收藏
    person_my_shopping_cart_id = (By.ID, 'com.yunmall.lc:id/txt_my_shoppingcart')
    """设置页面"""
    # 退出按钮
    setting_logout_btn = (By.ID, 'com.yunmall.lc:id/setting_logout')
    # 确认退出按钮
    setting_act_logout_btn = (By.ID, 'com.yunmall.lc:id/ymdialog_right_button')
    # 取消退出按钮
    setting_dis_logout_btn = (By.ID, 'com.yunmall.lc:id/ymdialog_left_button')
