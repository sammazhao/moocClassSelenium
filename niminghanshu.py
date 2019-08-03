from functools import partial

# 通过过程式编程实现：
list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    if i>2:
        list2.append(i)
print("大于2的函数有：", list2)

# 通过函数式编程实现：
def func(x):
    return x>3
f_first=filter(func,[1,2,3,4,5,6])
print("大于3的函数有：",[item for item in f_first])

def mod(n,m):
    return n%m

mod_by_100=partial(mod,100)
print(mod_by_100(7))
