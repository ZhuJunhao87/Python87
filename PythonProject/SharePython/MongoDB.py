# -*- coding: UTF-8 -*-
from pymongo import MongoClient

'''MongoDB数据库操作'''
class MongoDB(object):
    '''定义数据库连接参数'''
    def __init__(self):
        client = MongoClient('192.168.2.203', 27017)  # MongoDB数据库地址及端口号
        username = "gt_rw"  # 数据库用户名
        password = "greattao5877"  # 数据库密码
        self.db = client.baoliDb
        self.db.authenticate(username, password)

    '''查询所有记录'''
    def findAll(self):
        companyInfo = self.db.CompanyInfo
        all = companyInfo.find()
        for item in all:
            print(item)
        return companyInfo.find()

    '''查询单条记录'''
    def findOne(self, value):
        companyInfo = self.db.CompanyInfo
        one = companyInfo.find_one({"company_name": value})
        return one

    '''插入一条新纪录'''
    def insertOne(self, info):
        companyInfo = self.db.CompanyInfo
        infoId = 0
        if self.findOne(info['company_name']) is None:  # 判断是否已存在
            infoId = companyInfo.insert_one(info).inserted_id  # 返回插入的_id
        return infoId

if __name__ == '__main__':
    mongoDB = MongoDB()
    # mongoDB.findAll()

    # mongoDB.findOne()

    # config = {"name": "ceshi", "model": "mi", "type": "android"}
    # mongoDB.insertOne(config)
