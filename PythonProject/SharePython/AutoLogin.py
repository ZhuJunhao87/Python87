# -*- coding: UTF-8 -*-
import string
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote

'''登录并获取页面数据'''
class AutoLogin(object):
    '''定义cookie'''
    def __init__(self, cookie):
        self.cookie = cookie

    '''登录'''
    def login(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Connection': 'keep-alive',
            'cookie': self.cookie,
        }
        request = urllib.request.Request(login_url, headers=headers)
        response = urllib.request.urlopen(request)
        thePage = response.read().decode('utf-8')
        print(thePage)

    '''默认方法，固定cookie'''
    def search(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Connection': 'keep-alive',
            'cookie': self.cookie,
        }
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        thePage = response.read().decode('utf-8')
        soup = BeautifulSoup(thePage, 'lxml')
        return soup

    '''代理访问方式，传proxies，固定cookie'''
    def searchByProxies(self, url, proxies):
        headers = [('User-Agent',
                    'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36'),
                   ('Connection', 'keep-alive'),
                   ('cookie', self.cookie)]
        proxy_support = request.ProxyHandler(proxies)  # 创建ProxyHandler
        opener = request.build_opener(proxy_support)  # 创建Opener
        opener.addheaders = headers  # 添加User Angent
        request.install_opener(opener)  # 安装OPener
        response = request.urlopen(url)  # 使用自己安装好的Opener
        thePage = response.read().decode("utf-8")  # 读取页面并解码
        soup = BeautifulSoup(thePage, 'lxml')
        return soup

    '''处理页面数据'''
    def getContent(self, searchUrl, proxies):
        # 中文链接处理
        url = quote(searchUrl, safe=string.printable)
        soup = self.search(url)
        # 判断是否查询到数据
        single_company = soup.find('div', {'class': 'search_right_item'})
        if single_company is None:
            aBmid = soup.find("span", {'class': 'ABmid'})
            if aBmid is not None:
                return "code"
            return None
        # 公司名称
        company_name = soup.find("a", {'class': 'sv-search-company'}).get_text()
        # 公司详情页链接
        company_detail_url = soup.find("a", {'class': 'sv-search-company'}).get('href')
        # 公司状态
        company_status_type = soup.find("div", {'class': 'statusTypeNor'}).get_text()
        # 法人和链接
        company_legal_person = soup.find("a", {'class': 'legalPersonName'})
        company_legal_person_name = ""
        company_legal_person_name_url = ""
        if company_legal_person is not None:
            company_legal_person_name = soup.find("a", {'class': 'legalPersonName'}).get('title')
            company_legal_person_name_url = soup.find("a", {'class': 'legalPersonName'}).get('href')
        # 注册资本 和 注册时间
        company_detail = soup.select_one("div .search_row_new").select("div .title")
        for item in company_detail:
            if item.get_text().find("注册资本") != -1:
                registered_capital = item.get_text()[5:]
            elif item.get_text().find("注册时间") != -1:
                registration_date = item.get_text()[5:]
        # 公司评分
        company_grade_span = soup.find("span", {'class': 'c9 f20'})
        company_grade = ""
        if company_grade_span is not None:
            company_grade = soup.find("span", {'class': 'c9 f20'}).get_text()
        # 数据格式处理
        info = {"company_name": company_name, "company_detail_url": company_detail_url,
                "company_status_type": company_status_type,
                "company_legal_person_name": company_legal_person_name,
                "company_legal_person_name_url": company_legal_person_name_url,
                "registered_capital": registered_capital,
                "registration_date": registration_date,
                "company_grade": company_grade}
        return info


if __name__ == '__main__':
    login_url = 'https://www.tianyancha.com'  # 登录地址
    search_url = 'https://www.tianyancha.com/search?key=测试'  # 扒取地址
    cookie = 'xxxxxxx'  # 登录后的cookie数据

    autoLogin = AutoLogin(cookie)
    # autoLogin.login()
    autoLogin.search()
    # info = autoLogin.getContent(search_url, proxies)
    # print(info)
