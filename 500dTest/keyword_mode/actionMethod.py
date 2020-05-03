import time

from selenium import webdriver
from base.find_element import FindElement

class ActionMethod:
    #打开浏览器
    def open_browser(self,browser):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    #输入网址url
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    #输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        self.get_element(key).click()

    #等待
    def time_sleep(self,t):
        time.sleep(float(t))

    #获取title
    def get_title(self):
        return self.driver.title

    #关闭浏览器
    def close_browser(self,*args):
        self.driver.close()



