# selenium定位不到的 用js定位
from selenium import webdriver
import time

path = "C:\\Users\\15040\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.maximize_window()

driver.get("https://www.12306.cn/index/")
from_elem=driver.find_element_by_id("fromStationText")
time.sleep(3)
from_elem.click()
time.sleep(3)
from_elem.send_keys("北京")
driver.find_element_by_xpath("//*[text()='北京北']").click() # 任意路径下的任意标签中的text文本=北京北
time.sleep(3)
to_elem=driver.find_element_by_id("toStationText")
to_elem.click()
to_elem.send_keys("长春")
driver.find_element_by_xpath("//*[text()='长春南']").click()

# js定位，首先要去掉readonly属性

js="$('input[id=train_date]').removeAttr('readonly')"  #任意一个input标签中id=train_date
driver.execute_script(js)
date_elem=driver.find_element_by_id("train_date")
time.sleep(3)
date_elem.click()
time.sleep(3)
date_elem.clear()
date_elem.send_keys("2019-07-26")
time.sleep(3)
driver.find_element_by_class_name("form-label").click()
#直接点击查询按钮
driver.find_element_by_id("search_one").click()

