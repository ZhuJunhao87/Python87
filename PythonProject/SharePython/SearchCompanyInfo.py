# -*- coding: UTF-8 -*-
from SharePython.AutoLogin import AutoLogin
from SharePython.Excel import Excel
from SharePython.MongoDB import MongoDB

if __name__ == '__main__':
    company_url = "D:\\Test\\123\\1.xlsx"
    search_url = "https://www.tianyancha.com/search?key="
    cookie = 'TYCID=06d37e4054ce11e8b7d31fdf9520e6c1; undefined=06d37e4054ce11e8b7d31fdf9520e6c1; __guid=103457414.875897395654713300.1526010520167.5085; ssuid=6020468608; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODM2ODQyMDQwMSIsImlhdCI6MTUyNjYyNTU4MCwiZXhwIjoxNTQyMTc3NTgwfQ.CR9GxAGa7FpXmZkjyfXikw8GOBJpelb_SH47Xy7u1WTTtdqsBNgva7II4qL3voCJ78bmHwRi4xiMiyHWZFm67Q%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218368420401%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODM2ODQyMDQwMSIsImlhdCI6MTUyNjYyNTU4MCwiZXhwIjoxNTQyMTc3NTgwfQ.CR9GxAGa7FpXmZkjyfXikw8GOBJpelb_SH47Xy7u1WTTtdqsBNgva7II4qL3voCJ78bmHwRi4xiMiyHWZFm67Q; aliyungf_tc=AQAAAHwBRlAYigAAJvTjevwIvJjA8tqu; csrfToken=0J_ErhZ1gKiCwjitEhWFQVTB; monitor_count=7; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1526260403,1526625622,1526862905,1526951641; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1526951750'

    cookie1 = 'aliyungf_tc=AQAAAGrGpTfynQgAJvTjegWnm4Qpsx6j; csrfToken=u3AI9tClbuENo9AGW6ze6uXS; TYCID=5ff276505d8111e885c73f9a6495e65b; undefined=5ff276505d8111e885c73f9a6495e65b; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1526967170; ssuid=2523414884; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTc1Nzg1NjU3NyIsImlhdCI6MTUyNjk2NzA5NiwiZXhwIjoxNTQyNTE5MDk2fQ.wtewGlqa__K69XLdbtF0rsmZGeGDd3iSeYpHG9C6alpo24c2BrTJNwF-p1vo6JjDWvnh-J85MjIdm87nEY6h8A%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215757856577%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTc1Nzg1NjU3NyIsImlhdCI6MTUyNjk2NzA5NiwiZXhwIjoxNTQyNTE5MDk2fQ.wtewGlqa__K69XLdbtF0rsmZGeGDd3iSeYpHG9C6alpo24c2BrTJNwF-p1vo6JjDWvnh-J85MjIdm87nEY6h8A; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1526967186'

    cookie2 = 'TYCID=aacf4ff05a6511e8acbfb755297d4905; undefined=aacf4ff05a6511e8acbfb755297d4905; ssuid=2185309208; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1526625411,1526863361,1526951661; aliyungf_tc=AQAAAMg1wnFCvAYAJvTjemZILhUBfFWL; csrfToken=BI2yKIZBh0ZWcQmdv8tsLtPk; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1526978553; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgxNTI4NDgwNCIsImlhdCI6MTUyNjk3ODQ2OSwiZXhwIjoxNTQyNTMwNDY5fQ.dBExNt7RYcSeqsAiU8XYbF5WDumLLED-YaQ06HMIJn_PE81Cx2RcVdwLgl8qq-2_OjN1lNdC1BtPDEIyvOx4MA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218815284804%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgxNTI4NDgwNCIsImlhdCI6MTUyNjk3ODQ2OSwiZXhwIjoxNTQyNTMwNDY5fQ.dBExNt7RYcSeqsAiU8XYbF5WDumLLED-YaQ06HMIJn_PE81Cx2RcVdwLgl8qq-2_OjN1lNdC1BtPDEIyvOx4MA'

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
