# -*- coding: utf-8 -*-
#by zhangmingzhi date: 2017.5.16 08:17

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from YDMHTTPDemo3x import verify_captcha

import time


if __name__ == "__main__":
    """自动登录去哪儿网商家页面"""
    driver1 = webdriver.Firefox(executable_path="/home/zmz/下载/geckodriver")
    browser = driver1
    browser.maximize_window()
    browser.get("http://ebooking.qunar.com/ebPage/login.html")
    # time.sleep(1) #网速不好须延时一下,这里延时1s
    browser.find_element_by_css_selector(".login_name div input[name='username']").send_keys("××××××")   #帐号
    browser.find_element_by_css_selector(".login_pass div input[name='password']").send_keys(("××××××"))  #密码
    time.sleep(5) #延时5s等待验证码加载完毕
    for count in range(10):
        browser.find_element_by_css_selector(".vcodeImg.f_r").screenshot("captcha.jpg")   #截图方式保存验证码
        cid, result = verify_captcha('captcha.jpg', 1004)                                      #云打码平台识别验证码
        browser.find_element_by_css_selector(".login_check_code input[name='vcode']").send_keys(result)
        browser.find_element_by_css_selector(".login_submitd .login_icon").click()
        time.sleep(5)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".head-menu-active a")))#最多等待10s,每隔500ms查询一次元素
        try:
            if(browser.find_element_by_css_selector(".head-menu-active a").text == u"首页"):
                print("去哪儿验证码校成功")
                break
        except Exception as e:
            print("去哪儿验证码校验失败")


    """自动登录艺龙网商家页面"""
    driver2 = webdriver.Firefox(executable_path="/home/zmz/下载/geckodriver")
    browser = driver2
    browser.maximize_window()
    browser.get("http://ebooking.elong.com/ebkauth/login")
    # time.sleep(1) #网速不好须延时一下,这里延时1s
    browser.find_element_by_css_selector("#hotel_user").send_keys("××××××")   #帐号
    browser.find_element_by_css_selector("#password").send_keys(("××××××"))  #密码
    browser.find_element_by_css_selector("#submit").click()                          #点击登录为了先让验证码显示出来
    time.sleep(5)  #延时1s等待验证码加载完毕
    for count in range(10):
        browser.find_element_by_css_selector("#imgCode").screenshot("captcha.jpg")  #截图方式保存验证码
        cid, result = verify_captcha('captcha.jpg', 1004)  #云打码平台识别验证码
        browser.find_element_by_css_selector("#valicode").send_keys(result)
        browser.find_element_by_css_selector("#submit").click()
        time.sleep(5)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dashboard")))#最多等待5s,每隔500ms查询一次元素
        try:
            if(browser.find_element_by_css_selector("#dashboard").text == u"首页"):
                print("艺龙验证码校成功")
                break
        except Exception as e: #因为已经登录成功,所以找不到元素了
            print("艺龙验证码校验失败")


    """自动登录美团网商家页面"""
    driver3 = webdriver.Firefox(executable_path="/home/zmz/下载/geckodriver")
    browser = driver3
    browser.maximize_window()
    browser.get("http://eb.meituan.com/account/login?redirect=http%3A%2F%2Feb.meituan.com%2Feb%2Froomstatus/")
    time.sleep(1) #网速不好须延时一下,这里延时1s
    browser.switch_to_frame(browser.find_element_by_css_selector(".login-iframe")) #该网站加载了frame,先切换到里面去再输入账号密码
    browser.find_element_by_css_selector(".login__login").send_keys("××××××")   #帐号
    browser.find_element_by_css_selector(".login__password").send_keys(("××××××"))  #密码
    browser.find_element_by_css_selector(".login__submit").click()


    """自动登录携程商家页面"""
    driver4 = webdriver.Firefox(executable_path="/home/zmz/下载/geckodriver")
    browser = driver4
    browser.maximize_window()
    browser.get("http://ebooking.ctrip.com/ebkassembly/login.aspx?targetPath=%2febooking%2fHome.aspx")
    time.sleep(1) #网速不好须延时一下,这里延时1s
    browser.find_element_by_css_selector("#userName").send_keys("××××××")   #帐号
    browser.find_element_by_css_selector("#userPwd").send_keys(("××××××"))  #密码
    browser.find_element_by_css_selector("#accSubmit").click()
















