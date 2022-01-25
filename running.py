# encoding=utf-8
from appium import webdriver
import time
import data
import wechattest

des_leidian = {
                "platformName": "Android",#设备系统
                "deviceName": "2e1bd4f97d84",#设备名称，adb devices查看
                "platformVersion": "7.1.2",#手机或模拟器的版本号
                "appPackage": "com.android.browser",#apk包名
                "appActivity": "com.android.browser.BrowserActivity",#打开的进程名
                "noReset": True,
                "udid": "2e1bd4f97d84",   # 识别手机唯一标识
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                'noSign': True,
                "automationName": "Uiautomator2",  # toast 必须用Uiautomator2
                "autoGrantPermissions": True
                }

des_yeshen = {
                "platformName": "Android",
                "deviceName": "5de12c08",
                "platformVersion": "6.0.1",
                "appPackage": "com.mmc.feelsowarm",
                "appActivity": "com.mmc.feelsowarm.WelcomeActivity",
                "noReset": True,
                "udid": "5de12c08",   # 识别手机唯一标识
                "automationName": "Uiautomator2",  # toast 必须用Uiautomator2
                "autoGrantPermissions": True,
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                }


def start_app(deviceName="leidian", port=4723):
    '''启动app'''
    if deviceName == "leidian":
        des = des_leidian
    elif deviceName == "yeshen":
        des = des_yeshen
    else:
        des = des_leidian
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % port, des)
    #driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub' , des)
    return driver


if __name__ == '__main__':
    print('开始测试')
    driver = start_app()
    weiLink = wechattest.WeiXinLink(driver)
    time.sleep(20)
    weiLink.search()
    writedatas=[]
    datas = data.get_data()
    print(datas[0])
    weiLink.no_message(datas)
    weiLink.circle_click(writedatas,datas)
    data.wirtein(writedatas)
    time.sleep(10)
    driver.quit() # 退出driver
    print('测试结束！')







