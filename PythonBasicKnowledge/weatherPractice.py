############## 07/11/2019
# 1. weather类中包含方法：1.输入daytime返回可见度，2.根据input返回温度
class WeatherSearch():
    def __init__(self, input_daytime):
        self.input_daytime=input_daytime
    def search_visibility(self):
        visible_degree=0
        if self.input_daytime=="morning":
            visible_degree=2
        if self.input_daytime=="night":
            visible_degree=9
        return visible_degree
    def search_temperature(self):
        tem=0
        if self.input_daytime=="morning":
            tem=10
        if self.input_daytime=="night":
            tem=15
        return tem

# 2.OutAdvice 中包含2个方法：1.根据daytime返回建议的交通工具(覆盖父类的温度查找方法，返回工具)，2. 返回整体的建议
class OutAdvice(WeatherSearch):
    def __init__(self,input_daytime):
        WeatherSearch.__init__(self,input_daytime)
    def search_temperature(self):
        vehicle=""
        if self.input_daytime=="morning":
            vehicle= "bike"
        if self.input_daytime=="night":
            vehicle= "taxi"
        return vehicle
    def out_advice(self):
        visible_leave=self.search_visibility()
        if visible_leave==2:
            print("the weather is good, suggest to use %s" %self.search_temperature())
        elif visible_leave==9:
            print("the weather is not good, suggest to use %s" %self.search_temperature())
        else:
            print("I don't know!!")

use=OutAdvice("night")
use.out_advice()
