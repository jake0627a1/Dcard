import requests
from bs4 import BeautifulSoup
import json
import os

def create_folder(photo_name):
    folder_name=input('輸入資料夾名稱: ')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print('資料夾不存在, 建立新資料夾: '+ folder_name)
    else:
        print('找到資料夾: '+ folder_name)
    return folder_name

def download_pic(url,path):
    pic=requests.get(url,path)
    path+=url[url.rfind('.'):]
    f=open(path,'wb')
    f.write(pic.content)
    f.close
#url='https://imgur.dcard.tw/OVnUbhE.jpg'
#pic_path="donload"
#download_pic(url,pic_path)
#********************************************************************************************************#
test = open('D:\\vscodepython\\demo\\vscode\\sex.txt',"w",encoding='UTF-8')
p=requests.session()
url='https://www.dcard.tw/f/sex?latest=true'
hd={'user-agent': 'Mozilla/5.0 '}
html=requests.get(url,hd)
html.encoding='utf-8'
bs=BeautifulSoup(html.text,'html.parser')
sel = bs.select("div.PostList_entry_1rq5Lf a.PostEntry_root_V6g0rd") #選擇每篇文章
a=[]
for s in sel:
    a.append(s["href"])
url = "https://www.dcard.tw"+ a[2]
for k in range(0,50):         #滾輪下滑
    post_data={
        "before":a[-1][9:18],
        "limit":"30",
        "popular":"false"     #false=最新 true=熱門
    }
    r=p.get('https://www.dcard.tw/_api/forums/sex/posts',params=post_data,headers=hd)
    data2 = json.loads(r.text)
    for u in range(len(data2)):
        Temporary_url = "/f/sex/p/"+ str(data2[u]["id"]) + "-" + str(data2[u]["title"].replace(" ","-"))
        a.append(Temporary_url)
j=0
q=0
for i in a[2:]:
    url = "https://www.dcard.tw"+i
    j+=1
    print ("第",j,"頁的URL為:"+url)
    #file.write("temperature is {} wet is {}%\n".format(temperature, humidity))
    test.write("第 {} 頁的URL為: {} \n".format(j,url))
    url=requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_jpg = soup.select("div.Post_content_NKEl9d div div div img.GalleryImage_image_3lGzO5")
    for c in sel_jpg:
        q+=1
        print("第",q,"張:",c["src"])
        test.write("%\n""第 {} 張: {} \n".format(q,c["src"])) 
        pic=requests.get(c["src"])
        img2 = pic.content
        pic_out = open('D:\\vscodepython\\demo\\vscode\\sex\\'+str(q)+".png",'wb')
        pic_out.write(img2)
        pic_out.close()

test.close()
print("爬蟲結束")