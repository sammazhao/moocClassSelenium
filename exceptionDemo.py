########## 07/12/2019
# 1. 异常处理：try/except。一个try可以包含多个except自居，但只有一个分支会被处理--对应error的except语句
def exp_exception(x,y):
    try:
        result=x/y
        print("result = ",result)
    except Exception:
        print("Exception!! the divide number cannot be 0")

# exp_exception(6,0)

# 2. 抛出异常: raise语句。可通过类或实例化参数调用raise语句。
def exp_raiseException(x,y):
    try:
        raise ZeroDivisionError("This is a Zerodivision error!!")
    except ZeroDivisionError:
        print("an error occurred")
        raise
#exp_raiseException(4,0)

# 3. 捕捉对象: 在except字句中访问异常对象本身，即见到真正的异常信息，而不是自定义的。用as e。多个异常时会处理try中第一个异常
def model_exception(x,y):
    try:
        result=x/y
        a=name
    except(ZeroDivisionError,NameError,TypeError)as e:
        print(e)
    else:
        print("running pass!")
#model_exception(3,2)

# 4. 自定义异常
class MyError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "this is customized error"
    def error_test(self):
        try:
            raise MyError()
        except MyError as e:
            print("customized exception is: ",e)
        finally:
            print("I will appear at the end")
error=MyError()
error.error_test()
