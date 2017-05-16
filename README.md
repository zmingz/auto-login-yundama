# auto-login-yundama
云打码方式实现网站自动登录

* 操作系统：linux
* 运行环境：python3.3+
* 库支持：selenium
* 浏览器：firefox
* 插件：geckodriver

运行程序前先准备好以上的运行环境。selenium库的安装为在linux终端输入

    pip install selenium

然后把火狐浏览器的geckodriver插件[下载](https://github.com/mozilla/geckodriver/releases)，我把该插件放到`/home/zmz/下载`这个路径，如果你把它放到其他路径，则需要修改代码文件`autologin.py`的插件路径，位置如下

```javascript
webdriver.Firefox(executable_path="/home/zmz/下载/geckodriver")
```

到此运行环境准备好了，运行`autologin.py`，它会调用`YDMHTTPDemo3x.py`中类的方法实现云识别验证码，正确率大于90%，实现自动登录网站的目的，程序里我举例实现去哪儿酒店、艺龙网酒店、美团网酒店、携程网酒店的4个商家网站的自动登录，该程序只要稍作修改即可用于其他网站的自动登录，让我们愉快堤耍起来吧(跑：
