#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2013-11-11

@author: Justin
'''
import sys
import cookielib
import urllib2
import urllib


def login_and_vote(mail,team_num):
    team_id = {'1':'94','2':'89','3':'98','4':'123'}
    #check the team_id
    if not team_id.has_key(team_num):
        print 'Team number is not valided!'
        return False
    id = team_id[team_num]
    cj = cookielib.CookieJar()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    opener = urllib2.build_opener( urllib2.HTTPCookieProcessor(cj) )
    #====================
    urllib2.install_opener(opener)
    # login www.k4w.cn
    login_data = urllib.urlencode( {'mail' : mail, 'password' : 'asdfghjkl'})
    page = opener.open( 'http://www.k4w.cn/user/logoin.html', data = login_data )
    #~ print page.read()
    #~ print page.getcode()
    page.close()


    # vote
    vote_data = urllib.urlencode({'z_data': '10','id':id,'sid':'80'})
    page1=urllib2.urlopen('http://www.k4w.cn/zone/z_num.html', data = vote_data)
    #~ print page1.read()
    #~ print page1.getcode()
    page1.close()




#~ mail_head = 'justinleorobot' #0-100
#~ mail_head = 'alexrobot' # 0-100
#~ mail_head = 'dustinrobot' #0-200
#~ mail_head = 'austinrobot' #0-200
print 'Each day, you can vote less than 5000 points.'
print 'For each vote,you should input a start number and an end number,which should be in the range of 0 to 500.'
print 'The points of your vote equals (end - start)*10 for each vote.'
print 'If you want to continue your voting,you should keep the start following the end of your last vote,like 1-<0,20> => 2-<21,50> or 2-<30,50>.'
team_num = raw_input("Input the team number:")
start = int(raw_input("Input the 'start' for vote:"))
end = int(raw_input("Input the 'end' for vote:"))


if start not in range(0,2000) or end not in range(0,2000) or start > end:
    print 'Invalided input,oops!'
    sys.exit(0)

for i in range(start,end):
    if i in range(0,100):
        mail_head = 'alexrobot'
        mail = mail_head + str(i)+ '@qq.com'
    elif i in range(100,300):
        mail_head = 'dustinrobot'
        mail = mail_head + str(i-100)+ '@qq.com'
    elif i in range(300,500):
        mail_head = 'austinrobot'
        mail = mail_head + str(i-300)+ '@qq.com'
    elif i in range(500,2000):
        mail_head = 'justinleorobot'
        mail = mail_head + str(i-500)+ '@qq.com'

    print mail_head
    login_and_vote(mail,team_num)
    print 'success vote',i

print 'Done'
