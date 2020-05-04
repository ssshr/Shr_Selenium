from tools.excel_tool import ExcelTool
from keyword_mode.actionMethod import ActionMethod


class KeyWordCase:
    def run_main(self,excel_case):
        self.action_method = ActionMethod()
        handle_excel = ExcelTool(excel_case)
        # 获取行数
        case_lines = handle_excel.get_lines()
        if case_lines:
            # 循环行数，执行case
            for i in range(1, case_lines):
                is_run = handle_excel.get_cell_value(i,3)
                if is_run == 'yes':#是否执行
                    method = handle_excel.get_cell_value(i, 4)#执行方法
                    send_value = handle_excel.get_cell_value(i, 5)#输入数据
                    handle_value = handle_excel.get_cell_value(i, 6)#操作元素
                    except_result_method = handle_excel.get_cell_value(i,7)#预期结果元素
                    except_result = handle_excel.get_cell_value(i,8)#预期结果值
                    # if send_value: #是否有输入数据
                    print("[",is_run,"]","[",method,"]","[",send_value,"]","[",handle_value,"]")
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'Pass')
                            else:
                                handle_excel.write_value(i,'Fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i, 'Pass')
                            else:
                                handle_excel.write_value(i, 'Fail')




    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')#根据'='拆分字符串



    def run_method(self,method,send_value='',handle_value=''):

        method_value = getattr(self.action_method, method)#返回对象属性值，属性值不存在则返回异常
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        elif send_value != '' and handle_value != '':
            result = method_value(send_value,handle_value)
        else:
            result = method_value()
        return result

if __name__ == '__main__':
    test = KeyWordCase()
    test.run_main()





