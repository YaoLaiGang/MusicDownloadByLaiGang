import requests
import re
from tqdm import tqdm

MUSIC_NAME = "./name.txt"

re_music = re.compile(r'https\:\/\/music\.hwkxk\.cn\/api\/\?id\=[0-9]+\&source\=kuwoST')
re_name = re.compile(r'下载.+?song-bitrate')
def downMusic(music_name="不再打扰"):
    print("正在下载{}".format(music_name))
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'https://music.hwkxk.cn/'
    cs = {'mk_encrypt_c21f969b5f03d33d43e04f8f136e7682':"bb5cf23bee8fc811f66fd85325589960"}
    rq = requests.get(url = url, headers = headers, cookies = cs, params={'kw': music_name, 'source': 'kuwo'})
    if rq.status_code==200:
        rq.encoding = "utf-8"
    else:
        print(rq.status_code)
        print("访问{}失败，请重新填写cookie".format(music_name))
        exit(0)
    html_text = rq.text
    index = re_music.search(html_text).span()
    name_index = re_name.search(html_text).span()
    music_url = html_text[index[0]:index[1]]
    real_name = html_text[name_index[0]:name_index[1]][62:-28]
    music_rq = requests.get(url = music_url, headers = headers, cookies = cs)
    if music_rq.status_code!=200:
        print("下载音乐{}失败".format(real_name))
        exit(0)
    with open(real_name+".mp3",'wb') as f:
        f.write(music_rq.content)
        print("下载音乐{}成功".format(real_name))

name_file = open(MUSIC_NAME)
music_list = name_file.readlines()
dj_music = map(lambda x: x[:-1]+"DJ", music_list)

for music_name in dj_music:
    downMusic(music_name)