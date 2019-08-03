#通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

list=[2,-4,699,23,1,-9,6,7,88] #mid=23 left=[2,-4,1,-9,6,7] 23 right=[699,88]
# firstTime=[2,-4,1,-9,6,7] + [23] + [699,88]
# secondTime=[-4,-9] + [1] + [2,6,7] + [23] + [88, 699]
# thirdTime=[-9,-4,1,2,6,7,23,88,699]
def quickSort(list):
    if len(list) >=2:
        mid=list[len(list)//2]
        left, right=[],[]
        list.remove(mid)
        for num in list:
            if num >mid:
                right.append(num)
            else:
                left.append(num)
        return quickSort(left) + [mid] + quickSort(right)
    else:
        return list


print(quickSort(list))

