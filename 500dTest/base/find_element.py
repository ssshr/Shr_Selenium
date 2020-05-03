from tools.read_ini import ReadIni

class FindElement(object):

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'xpath':
                value.replace('"', "'")
                return self.driver.find_element_by_xpath(value)
        except:
            # self.driver.save_screenshot('D:/bsssss/500dTest/image/%s.png' %value)
            return None

