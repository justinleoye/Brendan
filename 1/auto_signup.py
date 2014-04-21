#coding:GB2312
'''
Created on 2012-7-30

@author: Administrator
'''
import cookielib
import urllib2
import urllib

from kinect_captcha import get_captcha

import md5
import random
import string

def md5_generator(s):
    m = md5.new()

    m.update(s)

    return m.hexdigest()


def make_user_name():
    return ''.join(random.choice(string.letters) for x in xrange(5))


def signup(mail):
    cj = cookielib.CookieJar()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    opener = urllib2.build_opener( urllib2.HTTPCookieProcessor(cj) )
    #====================
    urllib2.install_opener(opener)

    url = "http://www.k4w.cn/message/code.html"
    print "download"
    page = opener.open(url)
    file("./img/target.png", "wb").write(page.read())
    page.close()
#~ #~
    user_name = make_user_name()
    captcha = get_captcha()
    signup_data = urllib.urlencode( {'mail' : mail, 'password' : 'asdfghjkl', 'verifypwd':'asdfghjkl', 'user_name':user_name, 'v_code':captcha})
    print '>>start signup...'
    page = urllib2.urlopen( 'http://www.k4w.cn/user/insert.html', data = signup_data )
    #print page.read()
    #print page.getcode()
    page.close()

    m_user = md5_generator(mail)
    m_user_url = 'http://www.k4w.cn/m_user/'+m_user+'.html'
    #~ m_user_url = 'http://www.k4w.cn/m_user/9c85bbb476128d970b2938df4a713dfc.html'
    print '>>start verify email...'
    print m_user_url
    page = urllib2.urlopen(m_user_url)

    print page.read()
    print page.getcode()
    page.close()


#~ mail_head = 'justinleorobot' #0-99

#~ mail_head = 'alexrobot' #0-99
#~ mail_head = 'dustinrobot' #0-199
#~ mail_head = 'austinrobot' #0-199
mail_head = 'justinleorobot' #100-999
for i in range(1499,1500):
    print 'start'
    mail = mail_head + str(i)+ '@qq.com'
#~ #~
    signup(mail)
    print 'success',i




#not verified >> 141 142,881
#~ for i in [141,142,881]:
    #~ print 'start'
    #~ mail = mail_head + str(i)+ '@qq.com'
    #~ signup(mail)
    #~ print 'success',i
























