import urllib,urllib2,random
import Image,ImageEnhance,ImageFilter

import os

def get_images(count,url):
    for i in range(count):
        #url = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew.do?module=regist&rand=sjrand&0.5741623679641634"
        print 'downloaded'
        file("./img/%04d.png" % random.randrange(10000), "wb").write(urllib.urlopen(url).read())


#url = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew.do?module=regist&rand=sjrand&0.5741623679641634"
#get_images(50,url)

def get_captcha():
    dir = "./img/"
    path = "./font/"
    for f in os.listdir(dir):
        if f.endswith(".png"):
            print dir+f
            img = Image.open(dir+f)
            img = img.convert("RGB")
            pixdata = img.load()

