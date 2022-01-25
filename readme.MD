# 项目描述

这是app的检测微信链接是否配置正确的自动化项目，基于selenium+appium框架

# 环境准备

1.python3.6
2.Appium_Python_Client1.3.0

依赖包安装
>pip install -r requirement.txt

# 运行用例

>python 

# 注意事项

本次是写死了使用三星机子g9300进行测试，若要更换，需修改以下几个地方
1.更换机子，需要在running.py里修改连接测试的机子设备名称、安卓版本等信息
2.目前暂时只支持安卓手机进行测试
3.更换机子后，需要在wechattest.py文件的circle_click方法修改两个self.touch_screen(520,2263)的坐标参数，根据测试机子对应屏幕坐标修改，可用安卓手机开发者模式下的显示指针位置查看
4.更换机子后，需要在wechattest.py文件的close方法修改self.driver.tap([[0,84],[136,248]], 100)的坐标参数，根据测试机子对应屏幕坐标修改，可用安卓手机开发者模式下的显示指针位置查看
5.测试时要确保连接手机成功，可用adb命令查看，需要启动appium一直连接

# txt配置

txt配置的描述
'''
读取文件路径是写死在XXX\\Appium_Demo_weixin\\paylink.txt
写入文件路径是写死在XXX\\Appium_Demo_weixin\\result.txt
若要更换，需要到data.py修改对应路径

'''