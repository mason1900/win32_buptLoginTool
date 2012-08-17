#!/usr/bin/python
# -*- encoding:utf-8 -*-

def MrMsgConvert(idic):
	try:
		msg=int(idic['msg'])
		msga=idic['msga']
		xip=idic['xip']
		print msg,msga,xip
		if(msg==1):
			if(msga!=''):
				if(msga=='error0'):
					return "本IP不允许Web方式登录\n"
				elif(msga=='error1'):
					return "本账号不允许Web方式登录\n"
				elif(msga=='error2'):
					return "本账号不允许修改密码\n"
				else:
					return msga
			return "用户名或密码错误"
		elif(msg==2):
			return "该账号正在IP为："+xip+"的机器上使用，请点击<a href='gw.bupt.edu.cn/a11.htm'>继续</a>强制登录。\n"
		elif(msg==3):
			return "本账号只能在指定地址使用\n";
		elif(msg==4):
			return "本账号费用超支或时长流量超过限制\n(悲剧啊孩纸)\n"
		elif(msg==5):
			return "本账号暂停使用\n";
		elif(msg==6):
			return "System buffer full  (What's out?)"
		elif(msg==8):
			return "本账号正在使用,不能修改\n"
		elif(msg==9):
			return "新密码与确认新密码不匹配,不能修改\n"
		elif(msg==10):
			return "密码修改成功\n"
		elif(msg==11):
			return "本账号只能在指定地址使用\n"
		elif(msg==7):
	      	#return UT+UF+UM
			return u'未能解析的结果'
		elif(msg==14):
			#return "注销成功 Logout successfully"+pp+UT+UF+UM);
			return u'未能解析的结果'
		elif(msg==15):
			#return "登录成功 Login successfully"+pp+UT+UF+UM);
			return u'未能解析的结果'
		else:
			return '???'
	except:
		return u'未能解析的结果'
