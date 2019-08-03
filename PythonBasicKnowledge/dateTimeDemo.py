##### 07/12/2019

# 1. time模块
# time()函数：返回当前时间的时间戳
import time
print(time.time())

# localtime([secs]) 格式化时间戳为本地时间
print(time.localtime())

# gmtime([secs]) 将一个时间戳转换为UTC=0的struct_time
print(time.gmtime())

# asctime([t]) 返回一个刻度的日期时间字符串.参数t为完整的9为元组元素或通过gmtime(), localtime()返回的值
t=time.localtime()
print(time.asctime(t))

# ctime([secs]) 将时间戳转换为time.asctime()形式。作用相当于ctime(localtime())
print(time.ctime())

# strftime()

# datetime模块
import datetime
print(datetime.datetime.today())