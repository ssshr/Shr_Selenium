from selenium import webdriver
from tools.ShowapiRequest import ShowapiRequest
import time
import random
from PIL import Image

class GetCode:

    def __init__(self, driver):
        self.driver = driver
    def get_code_img(self,file_name):
        self.driver.save_screenshot(file_name)
        # 定位验证码
        img_element = self.driver.find_element_by_xpath("//*[@id='regEmailForm']/div[4]/img")
        location = img_element.location  # 获取验证码x,y轴坐标
        size = img_element.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 截取位置坐标
        im = Image.open(file_name)
        img = im.crop(rangle)  # 使用Image的crop函数，从截图中再次截取需要区域
        img.save(file_name)  # 保存验证码图片
        time.sleep(2)

    # 使用第三方工具，解析图片
    def code_img_read(self,file_name):
        self.get_code_img(file_name)
        r = ShowapiRequest("http://route.showapi.com/932-2", "174882", "5b6f22b7ae834baa8dff02ceaa9e46fa")
        r.addBodyPara("length", "4")
        r.addBodyPara("specials", "false")
        r.addBodyPara("secure", "false")
        # 文件上传位置
        r.addFilePara("image", file_name)
        res = r.post()
        code_text = res.json()['showapi_res_body']['code']
        # print(code_text)
        time.sleep(2)
        return code_text