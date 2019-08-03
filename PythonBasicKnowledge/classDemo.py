# 构造方法： __init__() 在对象实例化时被调用
# 一个类中可以有多个构造方法，最后一个构造方法会覆盖前面的，实例化时根据最后一个传参。
# 类中的非构造方法可以调用构造方法实例变量的属性。self.xxx。可以在类外部修改属性。
#__xxx 私有属性，类外部无法访问
# 用get_attrs方法来获取类中的私有变量

class classDemo():
    # def __init__(self):
    #     print("我是不带参数的构造函数")
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        print("我是带名字的构造函数，我的名字是：", self.__name, "年龄是：", self.__age)
    def personalInfo(self, info):
        for key, value in info.items():
            print(type(key))
            print(type(value))
            print(key + ' is:' + value + ' '+ self.__name)
    def __privateFunction(self):
        print("/")

list={'姓名':'xiongda','年龄':'28','爱好':'拉屎'}
# callFunc1=classDemo("xiaoming")
ins=classDemo("xiaoming", 2)






