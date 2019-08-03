from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

def screenshot(driver, filepath=None):
    if filepath==None:
        project_path=os.path.dirname(os.getcwd()) # 获取当前文件的上一层目录--PythonLearning
        print(project_path)
        file_path=project_path + "/images/"
        if not os.path.exists(file_path):
            os.mkdir(file_path)
            image_name=time.strftime("%Y%m%d-%H%M%S", time.localtime()) # string format time, 格式化当前时间
            file_path=file_path+image_name+".png"
            print(file_path)
        driver.save_screenshot(file_path)


try:
    path="C:\\Users\\15040\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://www.jd.com/")

    #鼠标悬停
    elem=driver.find_element_by_link_text("手机")
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(3)
    old_phone=driver.find_element_by_link_text("老人机")
    old_phone.click()
    #浏览器句柄切换
    handlers=driver.window_handles
    currentHandler=driver.current_window_handle
    for handler in handlers:
        if handler!=currentHandler:
            driver.switch_to.window(handler)
            screenshot(driver)
    driver.save_screenshot("laorenji.png")
finally:
    time.sleep(5)
    driver.quit()