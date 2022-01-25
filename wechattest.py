# encoding=utf-8
import time

class WeiXinLink():
    def __init__(self,driver):
         self.driver = driver

    def search(self):
        '''点击微信搜索-输入文件字样-模糊搜索出文件传输助手进行点击进入文件助手'''
        self.driver.find_element_by_id("com.android.browser:id/b0p").click()  # 点击输入栏
        time.sleep(5)
        self.driver.find_element_by_id("com.android.browser:id/bla").send_keys('https://cs.lingjisuanming.cn/api/test?report_ip=1') # 输入链接
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@text, '前往')]").click() # 点击访问
        time.sleep(5)
        print("访问成功！")
        self.driver.quit()

    def get_phonescreen(self):
        '''获取识别屏幕宽高 '''
        x = self.driver.get_window_size()['width'] # 获取手机宽
        y = self.driver.get_window_size()['height'] # 获取手机高
        print(self.driver.get_window_size()) # 可以获取当前手机屏幕大小 打印出为 1080，2244

    def touch_screen(self,click_a,click_b):
        '''click_a,click_b为该点的手机屏幕的横坐标、纵坐标，可用安卓手机开发者的指针功能查看'''
        ''':param click_a:横坐标'''
        ''':param click_b:纵坐标'''
        # 触屏点击对应坐标位置
        self.driver.tap([(click_a, click_b)],2)

    def send_message(self):
        '''点击发送对话'''
        # 点击发送按钮
        self.driver.find_element_by_xpath("//*[contains(@text, '发送')]").click()
        time.sleep(5)

    def no_message(self,datas):
        '''发送无效内容，填充对话栏'''
        ''':param datas:测试数据'''
        # 输入无效内容发送
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(datas[0])
        time.sleep(5)
        self.send_message()


    def close(self):
        '''关闭支付页'''
        # 模拟触屏点击左上角关闭按钮，不能用click，无效操作，更换测试手机需要更换坐标参数，不同手机屏幕尺寸不一样，坐标也会不一样
        self.driver.tap([[0,84],[136,248]], 100)
        time.sleep(5)



    def is_pay_correct(self,writedatas,data_line):
        '''判断是否未配置好不能调起支付'''
        ''':param data_line:测试链接'''
        ''':param writedatas:写入文件内容'''

        # 获取页面资源
        source=self.driver.page_source
        #print(source)
        # 判断页面资源是否有关键字 ，有则正常调起支付，无则将问题链接写入文件中
        if "请输入支付密码"in source:
            print('测试结果：微信正常支付')
            # 返回
            self.driver.back()
            time.sleep(5)
            # 关闭跳转界面
            self.close()
        else:
            print('测试结果：元素没找到！')
            # 将问题链接写入结果文件
            writedatas.append(data_line+'\n')
            print('写入文件内容writedatas:',writedatas)
            # toast_loc = ("xpath", ".//*[contains(@text,'确定')]" )
            # el = WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located(toast_loc))
            # print(el.text)
            # 关闭有问题链接弹出问题提示框
            element=self.driver.find_element_by_class_name("android.widget.Button")
            element.click()
            time.sleep(5)
            # 关闭跳转界面
            self.close()

    def  circle_click(self,writedatas,datas):
        '''循环发送每个校验的链接，点击跳转到支付页'''
        ''':param datas:文件数据'''
        ''':param writedatas:写入文件内容'''
        for data_line in datas[1:]:
            #从第二个开始遍历，第一个为无效内容
            print('测试链接data_line:',data_line)
            # 输入发送内容
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys(data_line)
            time.sleep(5)
            # 点击发送按钮
            self.send_message()
            # 点击链接微信跳转,更换测试手机需要更换坐标参数，不同手机屏幕尺寸不一样，坐标也会不一样
            self.touch_screen(520,2263) # 此为相对坐标，点击链接，因为click事件点击链接不起效，只能使用相对坐标触屏点击，坐标发生改变就可能定位不到
            time.sleep(5)
            # 在微信提示链接有风险的界面点击继续访问，更换测试手机需要更换坐标参数，不同手机屏幕尺寸不一样，坐标也会不一样
            self.touch_screen(733,1879) # 此为相对坐标，点击继续访问，因为整个元素都是图片，获取不到继续访问按钮元素，只能用相对坐标触屏点击
            time.sleep(20)
            # 判断是否正确调起支付
            self.is_pay_correct(writedatas,data_line)