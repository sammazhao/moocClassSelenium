# 1. __str__()   返回用户可以看的字符串
# 2. __repr__()  debug时返回好看的字符串

class student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
            return "学生姓名：%s " %self.name
    __repr__=__str__
print(student("xiaoming"))


# 3. __iter__   将一个类用于for...in循环，类似list，tuple用法，需要用此方法，返回一个迭代对象。__next__()
#e.g: 实现斐波那契数列
# class Fib():
#     def __init__(self):
#         self.a, self.b=0,1
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b, self.a+self.b
#         if self.a >10000:
#             raise StopIteration()
#         return self.a
#
# 4. __getattr__() 动态返回一个属性，当调用不存在时。
class student():
    def __init__(self):
        self.name="xiaoming"
    def __getattr__(self, item):
        if item=="score":
            return 60
stu=student()
print(stu.score)

# 5. __call__() 任何类，只要定义一个此方法，就可以直接对实例进行调用
class newStudent():
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print("名字：%s" %self.name)
stu=newStudent("xionger")
stu()

# 6. 判断一个对象是否能被调用 Callable()函数
print(callable(stu))
a=33
print(callable(a))




