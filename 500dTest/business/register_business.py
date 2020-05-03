import time
from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def uesr_base(self,name,email,password,code):
        self.register_h.send_user_name(name)
        self.register_h.send_user_email(email)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_btn()


    def register_function(self,name,email,password, code,assertCode,assertText):
        self.uesr_base(name, email, password, code)
        if self.register_h.get_user_text(assertCode, assertText) == None:
            return True
        else:
            return False

    def register_success(self):
        if self.register_h.get_register_btn_text() == None:
            print('注册成功')
            return True
        else:
            return False
    #使用错误邮箱
    def login_email_error(self,name,email,password,file_name):
        self.uesr_base(name, email, password, file_name)
        if self.register_h.get_user_text("user_email_error","请输入正确的邮箱账号") == None:
            return True
        else:
            return False

    #使用错误密码
    def login_password_error(self, name, email, password, file_name):
        self.uesr_base(name,email,password,file_name)
        if self.register_h.get_user_text("user_password_error","请输入6-20个字符的密码") == None :
            return True
        else:
            return False
    #验证码错误
    def login_code_error(self, name, email, password, file_name):
        self.uesr_base(name,email,password,file_name)
        if self.register_h.get_user_text("code_text_error", "验证码错误") == None:
            return True
        else:
            return False