#coding:GB2312
'''
Created on 2013-11-11

@author: Justin
'''
import cookielib
import urllib2
import urllib


def supervisor(mail):
    cj = cookielib.CookieJar()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    opener = urllib2.build_opener( urllib2.HTTPCookieProcessor(cj) )
    #====================
    
    page = opener.open( 'http://www.k4w.cn/level_search/1/80/0/0/0.html')
    html = page.read()
    if page.getcode() == 200:
        print 'right'
    page.close()
    
    
    
