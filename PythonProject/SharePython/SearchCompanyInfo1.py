# -*- coding: UTF-8 -*-
from SharePython.AutoLogin import AutoLogin
from SharePython.Excel import Excel
from SharePython.MongoDB import MongoDB

if __name__ == '__main__':
    company_url = "D:\\Test\\123\\2.xlsx"
    search_url = "https://www.tianyancha.com/search?key="
    cookie = 'TYCID=d6d951805a7511e8a5f02dafcbb1477d; undefined=d6d951805a7511e8a5f02dafcbb1477d; ssuid=3715739870; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY4NTgyNzY0NyIsImlhdCI6MTUyNjYzMjM1NCwiZXhwIjoxNTQyMTg0MzU0fQ.sZvq1WX9kAaMwnBIyfyP3976OPRjaunJSnPSpP6LGj2WSqsZDOt4jAA_RYN65_Pes8YWzeUcDWcUwyrvXDS15Q%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213685827647%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY4NTgyNzY0NyIsImlhdCI6MTUyNjYzMjM1NCwiZXhwIjoxNTQyMTg0MzU0fQ.sZvq1WX9kAaMwnBIyfyP3976OPRjaunJSnPSpP6LGj2WSqsZDOt4jAA_RYN65_Pes8YWzeUcDWcUwyrvXDS15Q; aliyungf_tc=AQAAADZYeXYPlgwAJvTjelJXWsqMQXgB; csrfToken=vQX6QhCVgkTxjwUVE9RDfKAr; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1526632403,1526863564,1526949582,1527036622; RTYCID=d5175004bb78492082bd0b981bad6385; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1527037035'
    cookie1 = 'TYCID=f7efe1505a6511e8aca3714785189352; undefined=f7efe1505a6511e8aca3714785189352; ssuid=1575878839; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgxNTI4OTYxMSIsImlhdCI6MTUyNjk0OTQ5NSwiZXhwIjoxNTQyNTAxNDk1fQ.Z74xyutqE38L08vOutl_94v_sW_ZLNiQXEF-RkHXJ6-7MtdaruKo-5B4ms8bmZzBulrjWnZ0xnwRyRToyBxq5A%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218815289611%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgxNTI4OTYxMSIsImlhdCI6MTUyNjk0OTQ5NSwiZXhwIjoxNTQyNTAxNDk1fQ.Z74xyutqE38L08vOutl_94v_sW_ZLNiQXEF-RkHXJ6-7MtdaruKo-5B4ms8bmZzBulrjWnZ0xnwRyRToyBxq5A; aliyungf_tc=AQAAADRb0he6rAAAJvTjelU1UQxwMep/; csrfToken=GQT3YGGkRQpYpcHH1gNVR8kK; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1526632772,1526863554,1526949573,1527036611; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1527037059'
    cookie2 = 'aliyungf_tc=AQAAAIm2JUj+1A0AJvTjegDIRVidDvuh; csrfToken=lZGkglrhDMa6Y7OzlPUOHEsm; TYCID=f385d2205e2311e8885033b5af9388e7; undefined=f385d2205e2311e8885033b5af9388e7; ssuid=8095614874; token=ddae180e48bc4052b8c32ee16c81834b; _utm=547018339305484d861e312322309114; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODA2NzM3NTA3NiIsImlhdCI6MTUyNzAzNzA5NCwiZXhwIjoxNTQyNTg5MDk0fQ.ICjiH9R_5DNC7qfzH-lZ4GqWx-0yyjh3qbVmzl7P9ynIrFGGqAiDQAe6l-bAezFQTQcpiXWkHWIyM4L-7YsB0A%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218067375076%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODA2NzM3NTA3NiIsImlhdCI6MTUyNzAzNzA5NCwiZXhwIjoxNTQyNTg5MDk0fQ.ICjiH9R_5DNC7qfzH-lZ4GqWx-0yyjh3qbVmzl7P9ynIrFGGqAiDQAe6l-bAezFQTQcpiXWkHWIyM4L-7YsB0A; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1527036998; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1527037175'

    excel = Excel()
    autoLogin = AutoLogin(cookie)
    # autoLogin = AutoLogin(cookie1)
    # autoLogin = AutoLogin(cookie2)
    cookieIndex = 0

    mongoDB = MongoDB()  # M
    proxies = ""
    # 随机代理IP
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
