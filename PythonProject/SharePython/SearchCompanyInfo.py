# -*- coding: UTF-8 -*-
from SharePython.AutoLogin import AutoLogin
from SharePython.Excel import Excel
from SharePython.MongoDB import MongoDB

if __name__ == '__main__':
    company_url = "D:\\Test\\123\\1.xlsx"
    search_url = "https://www.tianyancha.com/search?key="
    cookie = ''

    cookie1 = ''

    cookie2 = ''

    excel = Excel()
    autoLogin = AutoLogin(cookie)
    # autoLogin = AutoLogin(cookie1)
    # autoLogin = AutoLogin(cookie2)
    cookieIndex = 0
    mongoDB = MongoDB()
    proxies = ""
    # ip = IP()
    # proxies = ip.get_ip()
    count = 0

    companyNameList = excel.openWorkbook(company_url, count)
    print(len(companyNameList))
    for companyName in companyNameList:
        count += 1
        info = ''
        if mongoDB.findOne(companyName) is not None:
            print(companyName, "数据库已存在，不再执行 :", count)
            continue
        # if count % 10 == 0:
        #     proxies = ip.get_ip() # 随机代理IP
        try:
            info = autoLogin.getContent(search_url + companyName, proxies)
        except Exception as e:
            print(companyName, "处理异常，不再执行 :", count)
            continue

        if info is None:
            print(companyName, "查无数据，无法保存 : ", count)
            continue
        elif info == 'code':
            print("----要输校验码了----换号继续----", companyName)
            cookieIndex += 1
            if cookieIndex == 1:
                autoLogin = AutoLogin(cookie1)
                info = autoLogin.getContent(search_url + companyName, proxies)
                # continue
            elif cookieIndex == 2:
                autoLogin = AutoLogin(cookie2)
                info = autoLogin.getContent(search_url + companyName, proxies)
                # continue
            elif cookieIndex == 3:
                break
        if info is None:
            print(companyName, "查无数据，无法保存 : ", count)
            continue

        infoId = mongoDB.insertOne(info)
        print(infoId, " : ", companyName, " : ", info['company_name'], " : ", count)
        # break # 只执行第一个
