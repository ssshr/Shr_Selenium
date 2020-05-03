from page.register_page import RegisterPage
from tools.get_code import GetCode

class RegisterHandle(object):

    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # 输入用户名
    def send_user_name(self,name):
        self.register_p.get_username_element().send_keys(name)

    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self,code):
        get_code_text = GetCode(self.driver)
        # code = get_code_text.get_code_img(file_name)
        self.register_p.get_code_element().send_keys(code)

    #获取错误提示信息
    def get_user_text(self,info,error_tips):
        try:
            if info == "user_email_error":
                text = self.register_p.get_email_error_element().get_attribute("innerText")
            elif info == "user_password_error":
                text = self.register_p.get_password_error_element().get_attribute("innerText")
            elif info == "code_text_error":
                text = self.register_p.get_code_error_element().get_attribute("innerText")
        except:
            text = None
        return text

    #点击注册按钮
    def click_register_btn(self):
        self.register_p.get_btn_element().click()
    #获取注册按钮文本信息
    def get_register_btn_text(self):
        return self.register_p.get_btn_element().get_attribute("innerText")

