# -*- coding: UTF-8 -*-
import xlrd


'''处理EXCEL文件'''
class Excel(object):
    def __init__(self):
        print()

    '''打开EXCEL文件并获取数据'''
    def openWorkbook(self, url, index):
        rowlist = []
        data = xlrd.open_workbook(url)
        table = data.sheets()[0]  # 第一个sheet
        nrows = table.nrows  # sheet的行数
        for i in range(index, nrows):  # 循环每一行
            rowlist.append(table.row_values(i)[:1][0])  # 取第一列数据
            # print(table.row_values(i)[:1][0])
        return rowlist

    '''处理每行数据，此处为删除该行数据'''
    def delRows(self, url, rows):
        data = xlrd.open_workbook(url)
        sheet = data.sheets()[0]
        for i in range(rows) :
            sheet.Rows(i).Delete()

if __name__ == '__main__':
    excel = Excel()

    url = 'D:\\Test\\测试.xlsx'
    # excel.openWorkbook(url)
    excel.delRows(url,2)