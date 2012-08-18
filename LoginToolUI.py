#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import httplib, urllib 
import threading
import time
#import gobject
import gtk,pygtk 
#import sys,os
#import webkit
from getInfo import parseHTMLTitle
from getInfo import parseMsg
from msgConvert import MrMsgConvert

#注：取消了部分用不到的库
try:
    from hashlib import md5
except:
    import md5  
    

pygtk.require('2.0')

prefix='__MD5__'
HTTPheader = {"Content-type": "application/x-www-form-urlencoded",
            "Connection":"keep-alive"}

def getItemFromFile():
	res={}
	try:
		infofile=open("info.txt")
		for line in infofile:
			line=[x.strip() for x in line.split("=")]
			res[line[0]]=line[1]
		infofile.close()
	except:
		pass
	return res


	
class HTTPCnc():
	def __init__(self):
		self.md5=md5()
		self.conn=None
	def connect(self):
		self.conn=httplib.HTTPConnection("gw.bupt.edu.cn")
		
	def disconnect(self):
		self.conn.close()
		
	def MD5_encode(self,pword):
		self.md5=md5()
		pword="1"+pword+"12345678"
		self.md5.update(pword)
		return self.md5.hexdigest()+"123456781"
	
	def login(self,uname,pword):
		if(prefix not in pword):
			md5password=self.MD5_encode(pword)
		else:
			md5password=pword.lstrip(prefix)
		try:
			self.connect()
			sendItem="DDDDD="+uname+"&upass="+md5password+"&R1=0&R2=1&para=00&0MKKey=123456"
			print(sendItem)
			self.conn.request("POST", "", sendItem, HTTPheader)
			response = self.conn.getresponse()	
			data = response.read()
			title=parseHTMLTitle(data)
			self.disconnect()
			if(title==u'登录成功窗'):
				return {'status':True,'info':u'成功登录！别忘了注销哦～\n','pword':md5password}
			else:
				info=parseMsg(data)
				info=u'提示信息: '+MrMsgConvert(info)
				return {'status':False,'info':info,'pword':md5password}
		except:
			return {'status':False,'info':u'登录失败，请检查网络连接','pword':md5password}
	
	def logout(self):
		try:
			self.connect()
			self.conn.request("GET","/F.htm")
			response = self.conn.getresponse()
			data=response.read()
			self.disconnect()
			return u'登出成功'
		except:
			return u'登出失败，请检查网络连接'

class aboutDlg():
	def __init__(self):
		self.gladeFile="ui.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_objects_from_file(self.gladeFile,["aboutDlg"]) 
		self.gladeMain.connect_signals(self)
		
		self.mainDlg = self.gladeMain.get_object("aboutDlg")
		self.mainDlg.connect('destroy',lambda q :gtk.main_quit())
		self.mainDlg.connect("response", lambda d, r: d.destroy())
		self.mainDlg.show()
		
	def main(self):
		gtk.main()
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()
		
class mainDlg():
	def __init__(self):
		self.gladeFile="ui.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_objects_from_file(self.gladeFile,["mainDlg"]) 
		self.gladeMain.connect_signals(self)
		
		#添加主界面
		self.mainDlg = self.gladeMain.get_object("mainDlg")
		self.mainDlg.set_default_size(320,240) 
		self.mainDlg.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.mainDlg.connect('destroy',lambda q :gtk.main_quit())
		dictItem=getItemFromFile()
		if('uname' in dictItem and 'pword' in dictItem):
			self.gladeMain.get_object('userEntry').set_text(dictItem['uname'])
			self.gladeMain.get_object('pwdEntry').set_text(prefix+dictItem['pword'])
		self.cnc=HTTPCnc()			
		self.mainDlg.show()
	
	def on_loginBtn_clicked(self,*args):
		uname=self.gladeMain.get_object('userEntry').get_text()
		pword=self.gladeMain.get_object('pwdEntry').get_text()
		res=self.cnc.login(uname,pword)
		
		if(res['status']):
			infofile=open("info.txt","w")
			infofile.write("%s=%s\n" % ('uname',uname))
			infofile.write("%s=%s\n" % ('pword',res['pword']))
			infofile.close()
			self.gladeMain.get_object('userEntry').set_text(uname)
			self.gladeMain.get_object('pwdEntry').set_text(prefix+res['pword'])
		
		errorMsgBox=gtk.MessageDialog(None,gtk.DIALOG_MODAL,
											gtk.MESSAGE_INFO,gtk.BUTTONS_OK,
											u'提示信息')
			
		errorMsgBox.format_secondary_text(res['info'])
		errorMsgBox.run()
		errorMsgBox.destroy()
		return None
	
	def on_logoutBtn_clicked(self,*args):
		res=self.cnc.logout()
		errorMsgBox=gtk.MessageDialog(None,gtk.DIALOG_MODAL,
											gtk.MESSAGE_INFO,gtk.BUTTONS_OK,
											u'提示信息')
			
		errorMsgBox.format_secondary_text(res)
		errorMsgBox.run()
		errorMsgBox.destroy()
	
	def on_aboutBtn_clicked(self,*args):
		_aboutDlg=aboutDlg()
		_aboutDlg.main()
	
	def main(self):
		gtk.main()
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()

		
if(__name__=='__main__'):
	_mainDlg=mainDlg()
	_mainDlg.main()

