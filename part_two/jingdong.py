from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json

#启动browser
path = "C:\\Users\\15040\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.maximize_window()

#方法1：登录功能
def login():
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    time.sleep(3)
    driver.find_element_by_id("loginname").clear()
    driver.find_element_by_id("loginname").send_keys("samma.2009@163.com")
    driver.find_element_by_id("nloginpwd").send_keys("949454tc19")
    driver.find_element_by_id("loginsubmit").click()

    save_cookies_to_file(driver)

#方法2： 把cookies保存到文件中
def save_cookies_to_file(driver):
    #获取存储cookies的文件夹
    file_path=get_cookies_dir()
    #获取cookies
    cookies=driver.get_cookies()
    #存储cookies到文件中
    with open (file_path + "jd.cookies", "w") as f:
        json.dump(cookies, f)   #json.dump ---将文件内容转换成Json格式

#方法3： 定义并返回file path
def get_cookies_dir():
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path

# 方法4： 检查cookies是否生效
def check_cookies():
    #设置一个登录状态，初始值是未登录
    login_status=False
    #将cookies信息保存到driver中
    driver=save_cookies_to_driver()
    #进行跳转link的检测
    driver.get("https://order.jd.com/center/list.action")
    current_url=driver.current_url
    if current_url== "https://order.jd.com/center/list.action":
        login_status=True
        return login_status
    else:
        return login_status

#方法5： 保存cookies信息到driver
def save_cookies_to_driver():
    cookies_file=get_cookies_file()
    jd_cookies_file=open(cookies_file, "r")
    jd_cookies_str=jd_cookies_file.readline()
    jd_cookies_filedict=json.loads(jd_cookies_str)   # json.loads --用于处理字符串，将一个JSON编码的字符串转换回一个Python数据结构

    # 先清除掉旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    for cookie in jd_cookies_filedict:
        driver.add_cookie(cookie)
        return driver

# 方法6： 获取cookies file路径
def get_cookies_file():
    return get_cookies_dir() + "jd.cookies"

# 方法7： 跳转至商品页面
def to_goods_page():
    #先把页面放在首页上
    driver.get("https://www.jd.com")
    # 定位到“电脑”
    computer_element=driver.find_element_by_link_text("电脑")
    # 鼠标悬停至“电脑”
    ActionChains(driver).move_to_element(computer_element).perform()
    # 点击“笔记本”
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    handles=driver.window_handles
    index_handle=driver.current_window_handle
    for handle in handles:
        if handle !=index_handle:
            driver.switch_to.window(handle)
    # 点击thinkpad
    driver.find_element_by_xpath('//*[@id=\"brand-11518\"]/a').click()
    #点击7000以上，评论数，点击第一款电脑
    driver.find_element_by_xpath('//*[@id=\"J_selectorPrice\"]/div/div[2]/div/ul/li[7]/a').click()
    driver.find_element_by_xpath('//*[@id=\"J_filter\"]/div[1]/div[1]/a[3]').click()
    driver.find_element_by_xpath('//*[@id=\"plist\"]/ul/li[1]/div/div[1]/a/img').click()
    #切换句柄 -- 3个句柄
    notebook_handle=driver.current_window_handle
    handles=driver.window_handles
    for handle in handles:
        if handle !=index_handle and handle !=notebook_handle:
            driver.switch_to.window()


    # 点击规则与参数
    js="window.scrollTo(0,1500)" #横纵轴
    driver.find_element_by_xpath('//*[@id=\"detail\"]/div[1]/ul/li[2]').click()
    #解析所有标签
    #拿信息思路： 先拿整体，然后格式化成json，字典等等
    info_elements=driver.find_elements_by_class_name()

    #用一个list存储最终结果
    result_list=[]
    # 标签一个个解析
    for info_element in info_elements:
        info_element_dict=get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    #保存信息到文件中
    save_goods_info(result_list)

def save_goods_info(info_list):
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path + "goods_info"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open (file_path + "computer.infos", "a", encoding="utf-8") as f: # 不加utf-8 不能正确编码中文
        f.write(str(info_list)) # write不能直接写list类型，必须先转换成str
        print(info_list)



def get_info_element_dict(info_element):
    #拿到第一列的信息
    computer_part=info_element.find_element_by_tag_name("h3")
    #拿计算机信息中的key值
    computer_info_keys=info_element.find_elements_by_tag_name("dt")
    #拿计算机信息中的value值
    computer_info_values=info_element.find_elements_by_xpath("dl//dd[not(contains(@class,'Ptable-tips'))]")
    #存储key vlaue
    key_and_value_dict={}
    #存储所有计算机组成信息
    parts_dict={}
    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text]=computer_info_values[i].text
    parts_dict[computer_part.text]=key_and_value_dict
    return parts_dict



if __name__=="__main__":
    # 用一个循环来判断登录状态，判断登录是否成功
    try:
        #login()
        loop_status=True
        while loop_status:
            # 检验cookies是否生效
            login_status=check_cookies()
            if login_status:
                loop_status=False
            else:
                login()
        #跳转至商品信息页面
        to_goods_page()
    finally:
        time.sleep(3)
        driver.quit()
