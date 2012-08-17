测试小程序
北邮网关登录工具buptLoginTool，基于python 和 pyGTK编写
程序作者丁神，我在其基础上做了一点点修改，在Windows环境下编译成功，由于条件有限，目前只是在一台XP和Vista上进行了测试，欢迎测试～
如不能运行，请将文件夹下生成的.log文件内容回复在下面，或者发给mw2010a@gmail.com

Win32版地址
http://pan.baidu.com/share/link?shareid=3416&uk=503587752（百度网盘，5MB左右）

修改后的源码：
https://github.com/mason1900/win32_buptLoginTool

头回用这个东西不太习惯……各路神牛勿喷……

主要修改内容：
1.	删去了不必要的库
2.	修正了LoginToolUI.py中斜杠在windows下造成的问题（同时删去sys.path[0]+）
3.	编写setup.py用于py2exe（这里给出了用于pyGTK的通用写法）
4.	将logo.png转换为logo.ico（避免特殊情况下程序崩溃）
5.	修改了ui.glade中gtk版本号为2.16（因为我在windows上的gtk是2.16，原来版本2.24我这里不能编译）

主要问题：
1.	用py2exe制作的程序界面与GTK界面有差距（”关于”对话框还是比较像的），原因目前还没弄清楚，不过我电脑上GnuPG软件的GTK图形界面也是如此。用python来执行LoginToolUI.py可以实现完美的GTK界面。
2.	程序自身的一些小问题。期待丁神的更新～

若在Windows下使用源代码，需注意：
1.	如果使用我修改后的代码在python中执行，至少需要pyGTK, GTK+, pyCrypto, pycairo，这些各官网都有windows版安装程序，然后修改系统环境变量加入python和GTK的路径; 如果要通过py2exe编译为独立运行的exe，首先还是修改系统环境变量Path加入python和GTK路径，然后可能还要安装其他库——我的电脑上安装的是一个牛人做的pyGTK All-In-One pack，选择安装时自动分析依赖关系，省事了，不过假如你刚才装了GTK的话要把它先删掉。
2.	原来的代码还包含import webkit，这个……pyWebkitGTK在windows上没有现成的bin，我整了N久也没弄出来，（可以做到，但太太太麻烦了）最后还是在这个All-In-One pack中找到了，这个是牛人用mingw编译的。后来精简库文件时发现代码中的webkit并非必要，就取消了。
3.	关于这个pyGTK All-In-One pack：
http://opensourcepack.blogspot.com/2009/12/pywebkitgtk-windows-binary.html
这个页面有详细的说明，不过不好意思blogspot是谷歌的服务，需要爬墙。
下载地址是在国外网盘dropbox上，所以也需要爬墙。
4.	没了……
