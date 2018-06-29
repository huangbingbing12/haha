import pytest
from appium import webdriver
class Test_Seach():
    # def setup(self):
        #
        # # server 启动参数
        # desired_caps = {}
        # # 设备信息
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1'
        # desired_caps['deviceName'] = '192.168.56.101:5555'
        # # app的信息
        # desired_caps['appPackage'] = 'com.android.settings'
        # desired_caps['appActivity'] = '.Settings'
        #
        # # 声明我们的driver对象
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # @pytest.mark.parametrize("keyword", ["hello","1","huangbingbing"])
    # def test_seach(self,keyword):

# 找到搜索 并且点击
#         self.driver.find_element_by_id("com.android.settings:id/search").click()
#         # 找到输入框 输入文字
#         self.driver.find_element_by_id("android:id/search_src_text").send_keys(keyword)
#         # 点击返回
#         self.driver.find_element_by_class_name("android.widget.ImageButton").click()
#     @pytest.mark.parametrize(("username","password"), [("zhangsan","123456"), ("lisi","789456")])
#     def test_login(self,username,password):
#         print(username)
#         print(password)
    @pytest.mark.parametrize(("username",),[("xiaowang",),("lisi",)])
    def test_login(self,username):
        print(username)
        assert 1