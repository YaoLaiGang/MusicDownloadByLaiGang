import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://music.hwkxk.cn/'
cs = {'mk_encrypt_c21f969b5f03d33d43e04f8f136e7682':"bb5cf23bee8fc811f66fd85325589960"}
rq = requests.get(url = url, headers = headers, cookies = cs, params={'kw': '不再打扰', 'source': 'kuwo'})
print(rq.url)
if rq.status_code==200:
    rq.encoding = "utf-8"
    print(rq.text)
else:
    print(rq.status_code)

