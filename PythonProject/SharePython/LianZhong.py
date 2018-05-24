# coding: utf-8
import base64

import requests


def main(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type, tools_token):
    '''
            main() 参数介绍
            api_username    （API账号）             --必须提供
            api_password    （API账号密码）         --必须提供
            file_name       （需要打码的图片路径）   --必须提供
            api_post_url    （API接口地址）         --必须提供
            yzm_min         （验证码最小值）        --可空提供
            yzm_max         （验证码最大值）        --可空提供
            yzm_type        （验证码类型）          --可空提供
            tools_token     （工具或软件token）     --可空提供
    '''
    # api_username =
    # api_password =
    # file_name = 'c:/temp/lianzhong_vcode.png'
    # api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    # yzm_min = '1'
    # yzm_max = '8'
    # yzm_type = '1303'
    # tools_token = api_username

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    print(r.text)
    return r.text


def download_vcode(url, file_name):
    try:
        imgdata = base64.b64decode(url)
        file = open(file_name, 'wb')
        file.write(imgdata)
        file.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    file_name = 'D:/Test/lianzhong_vcode.png'  # 本地图片地址
    url = ''  # 图片链接地址
    download_vcode(url[22:], file_name)  # 下载图片到指定本地地址

    main('账号',
         '密码',
         file_name,
         "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload",
         '1',
         '8',
         '1108',
         '')

    '''
        1108 不定数中文
    '''
    '''
        main() 参数介绍
        api_username    （API账号）             --必须提供
        api_password    （API账号密码）         --必须提供
        file_name       （需要打码的图片路径）   --必须提供
        api_post_url    （API接口地址）         --必须提供
        yzm_min         （验证码最小值）        --可空提供
        yzm_max         （验证码最大值）        --可空提供
        yzm_type        （验证码类型）          --可空提供
        tools_token     （工具或软件token）     --可空提供
    '''
