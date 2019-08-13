from selenium import webdriver
import time
path = "C:\\Users\\15040\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://passport.jd.com/new/login.aspx")
driver.maximize_window()

# 强制等待
time.sleep(3)

#隐形等待   设置一个最长等待时间，在规定时间内网页加载完成，则执行下一步，否则就一直等到时间截止，然后执行下一步
#隐形等待只要设置一次，全局生效。
driver.implicitly_wait(10)

# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 定位元素
locator=(By.CSS_SELECTOR, ".login-tab.login-tab-r")

# 判断账号登录元素是否存在
element=WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
element.click()