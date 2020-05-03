import configparser

class ReadIni(object):

    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = r"D:\bsssss\500dTest\config\LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    #获取值
    def get_value(self,key):
        data = self.cf.get(self.node, key)
        return data

if __name__ == '__main__':
    read_ini = ReadIni()
    read_ini.get_value("main_login_btn")
    print(read_ini.get_value())



#注册信息配置
# main_login_btn = cf.get('RegisterElement','main_login_btn')
# login_mode_btn = cf.get('RegisterElement','login_mode_btn')
# email_mode_btn = cf.get('RegisterElement','email_mode_btn')
# user_name_input = cf.get('RegisterElement','user_name_input')
# user_email_input = cf.get('RegisterElement','user_email_input')
# user_password_input = cf.get('RegisterElement','user_password_input')
# code_image = cf.get('RegisterElement','code_image')
# code_text_input = cf.get('RegisterElement','code_text_input')