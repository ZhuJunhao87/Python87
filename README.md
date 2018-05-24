# Python87
Python简例

Python简单爬虫教程 
BY zhujunhao
1.安装Python，基于Python3
https://www.python.org/downloads/
下载安装包并安装，注意选择自动添加到系统PATH，否则可以重新安装或者手动配置PATH，可自行搜索配置方法

安装完成后，Win键+R输入CMD进入命令提示符输入：
python
显示python版本则安装成功
 
进入python后可直接输入代码测试，输入 exit() 可退出python
2.Intellij IDEA配置Python环境
Idea打开设置按下图安装python，也可以网站下载从本地安装
 
安装完成后重启Idea
3.创建Python工程
Idea工具栏File-New-Project：
略

4.打开Python工程并新建 .py文件测试
创建工程时选择了flask模板的话会有一个默认的.py文件。可在该文件内测试代码
 
5.安装BeautifulSoup（html代码解析工具）
win键+R输入CMD进入命令提示符输入：
pip install beautifulsoup4
等待安装完成，也可以网页下载后本地安装，方法自行搜索

6.连接MangoDB数据库
使用pip安装pymongo
教程：https://www.yiibai.com/mongodb/mongodb_python.html
win键+R输入CMD进入命令提示符输入：
python -m pip install pymongo

7．EXCEL处理
使用pip安装xlrd 
win键+R输入CMD进入命令提示符输入：
pip install xlrd

8．自动化测试工具Selenium
使用pip安装requests
win键+R输入CMD进入命令提示符输入：
pip install selenium

9．IP代理设置，
使用pip安装requests 
win键+R输入CMD进入命令提示符输入：
pip install requests

10．其他代码
链接编码处理，处理链接中带有中文的情况
from urllib.parse import quote
search_url = 'https://www.tianyancha.com/search?key=浙江大道保理有限公司'
url = quote(searchUrl, safe=string.printable)
python时间延迟
import time
time.sleep(0.001)  # 精确到毫秒
调用其他 .py文件方法
同路径文件：
from SharePython.AutoLogin import AutoLogin # 引入其他同路径下文件方法
不同路径的方法：
import sys
sys.path.append(path) # path为绝对路径

11．参考网站
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
http://www.runoob.com/python/python-tutorial.html
https://www.cnblogs.com/qqandfqr/p/7866650.html

12．注意事项
Python2和Python3区别较大，很多方法不能共用，本文是基于Python3的简单教程。
