# python中的魔法方法
class Person():
    def __init__(self,name):
        print("构造函数运行")

    #call方法可以让类像函数一样来使用。 类后添加参数时， call方法变成可调用的，并被自动调用
    def __call__(self, *args, **kwargs):
        print("call方法运行")

    # new方法真正决定了实例化哪个类。决定类的数据类型
    def __new__(cls, *args, **kwargs):
        print("New 方法运行")
        return object.__new__(Person)
        #return Dog()

    # del方法为 析构函数。类销毁时会运行
    def __del__(self):
        print("析构函数 del方法运行")

class Dog():
    def run(self):
        print("dog running")
p("xiaoming")
Person("xiaoming")(2)
