import xlrd
import time
from xlutils.copy import copy

class ExcelTool:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = r'D:\bsssss\500dTest\config\casedata.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        #打开表格
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    #获取excel数据，每行一个list
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(self.get_lines()):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    #获取exce行数
    def get_lines(self):
        #行数
        rows = self.table.nrows
        if rows >= 1 :
            return rows
        return None
     #获取单元格数据
    def get_cell_value(self,row,col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    #写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)
        time.sleep(0.5)



if __name__ == '__main__':
    ex = ExcelTool(r'D:\bsssss\500dTest\config\keyword.xls')
    print(ex.write_value(7,8))