'''
Created on Oct 25 2017

@author: Bourne
'''
import os
import requests
from bs4 import BeautifulSoup

def iyangzi(id):
    root_url = 'http://iyangzi.com/?p=' + id
    print(root_url)
    try:
        r = requests.get(root_url)
        if r.status_code == 200:
            girl_dir = "F:\python\python\File\girl"
            if not os.path.exists(girl_dir):
                os.mkdir(girl_dir)
            os.chdir(girl_dir)
            soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
            all_img = soup.find('div', class_='post-content').find_all('img')
            count = 1
            for img in all_img:
                src = img['src']
                name = 'iyangzi' + id + str(count)
                with open(name + '.jpg', 'ab') as img_object:
                    img_content = requests.get(src).content
                    img_object.write(img_content)
                    img_object.flush()
                count += 1
            pre_post = soup.find('div', class_='prev-post').find_all('a')
            href = pre_post[0]['href']
            if href == "javascript:;":
                exit("结束了")
            else:
                page = href.split('p=')[1]
                iyangzi(page)
    except requests.HTTPError as e:
        print(e)


iyangzi("239")
