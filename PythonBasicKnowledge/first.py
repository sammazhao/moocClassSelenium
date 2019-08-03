# a="happy"
# print (a)
# print(a[1])
# print('p' in a)
# myList=[1,2,3,4,4,4,4]
# myList.append(5)
# print(len(myList))
# del myList[0]
# print(myList)
# count_p=myList.count(4)
# print(count_p)

# t=('a','b',['A','B'])
# t[2][0]='X'
# t[2][1]='Y'
# print((t))

# studnet=['xiaoming', 'xiongda', 'xionger','sb']
# stuNumber=[1001, 1002, 1003, 1004]
# for i in range(len(studnet)):
#     print(studnet[i],'的学号是： ',stuNumber[i])

others={'城市':'北京','爱好':'编程'}
def personinfo(name, number, **kwargs):
    print('名字：',name, '学号：', number, '其他：', kwargs)

personinfo('xiongda',1001,城市=others['城市'], 爱好=others['爱好'])
personinfo('熊二',1002,**others)

