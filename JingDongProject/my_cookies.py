from selenium import webdriver
import time
import os
import json
# 用cookies绕过登陆，步骤：获取到cookies， 存储到文件中，访问时带着cookie
path = "C:\\Users\\15040\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.maximize_window()
def save_cookies(driver):
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path + "/cookies/"
    if not os._exists(file_path):
        os.mkdir(file_path)
    #从driver中获取cookies
    cookies=driver.get_cookies()

    #with open 会自动管理文件流
    with open(file_path + "jd.cookies", "w") as c:
        json.dump(cookies, c) #json.dump ---将文件内容转换成Json格式
        #必须用json.dump, 将来在取cookies时，使用json.loads方法，不用的话格式会不匹配

def login():
    try:
        driver.get("https://www.jd.com")
        driver.find_element_by_class_name("link-login").click()
        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_id("loginname").send_keys("samma.2009@163.com")
        driver.find_element_by_id("nloginpwd").send_keys("949454tc19")
        driver.find_element_by_id("loginsubmit").click()

        # 保存cookies到文件中
        save_cookies(driver)
    finally:
        time.sleep(5)
        driver.quit()

def get_url_with_cookies():
    # 使用https://order.jd.com/center/list.action  个人订单页面的url，访问他来判断cookies是否生效
    # 1. 获取cookies
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path + "/cookies/"
    cookies_file=file_path+"jd.cookies"

    jd_cookies_file=open(cookies_file, "r")
    jd_cookies_str=jd_cookies_file.readline()
    # 加载cookies信息
    # json.loads --用于处理字符串，将一个JSON编码的字符串转换回一个Python数据结构
    jd_cookies_dict=json.loads(jd_cookies_str)

    # 必须先访问网站，把旧的cookies删除掉，再把我们保存的cookies添加进去
    time.sleep(3)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    #将cookies信息添加到driver
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    #检查登录是否成功
    time.sleep(3)
    driver.get("https://order.jd.com/center/list.action")


if __name__ == "__main__":
    #login()
    get_url_with_cookies()