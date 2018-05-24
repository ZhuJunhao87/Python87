# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

import random
from bs4 import BeautifulSoup

import requests

'''获取代理IP地址'''
class IP(object):
    def __init__(self):
        print()

    '''获取IP列表'''
    def get_ip_list(self, url, headers):
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        return ip_list

    '''获取随机IP'''
    def get_random_ip(self, ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'https': proxy_ip}
        return proxies

    '''获取IP'''
    def get_ip(self):
        url = 'http://www.xicidaili.com/nn/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
        }
        ip_list = self.get_ip_list(url, headers=headers)
        proxies = self.get_random_ip(ip_list)
        return proxies


if __name__ == '__main__':
    ip = IP()
    proxies = ip.get_ip()
    print(proxies)
