#!/usr/bin/python
# -*- encoding:utf-8 -*-
from HTMLParser import HTMLParser
import re

class TitleParser(HTMLParser): 
	def __init__(self): 
		self.title = '' 
		self.readingtitle = 0 
		HTMLParser.__init__(self) 
 
	def handle_starttag(self , tag , attrs): 
		if tag == 'title': 
			self.readingtitle = 1 
	def handle_data(self , data): 
		if self.readingtitle: 
			self.title += data 
	def handle_endtag(self , tag): 
		if tag == 'title': 
			self.readingtitle = 0 
	def gettitle(self): 
		return self.title 
 
def parseHTMLTitle(idata): 
	tp = TitleParser() 
	tp.feed(idata) 
	return unicode(tp.gettitle().strip(), "gb2312")
	
def parseMsg(data):
	data=unicode(data, "gb2312")
	msg=re.findall('Msg=\d+',data)
	info=re.findall('msga=\'.*\'',data)
	xip=re.findall('xip=\'.*?\'',data)
	print msg,info,xip
	try:
		msg=msg[0].split('=')[1].strip().replace('\'','').replace(';','')
	except:
		return u'Parse Error!'
	
	try:
		info=info[0].split('=')[1].strip().replace('\'','').replace(';','')
	except:
		info=''
	
	try:
		xip=xip[0].split('=')[1].strip().replace('\'','').replace(';','')
	except:
		xip=u'Unknown IP'
		
	return {'msg':msg,'msga':info,'xip':xip}
