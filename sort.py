def BubbleSort(data,reverse=False):
    """
    冒泡排序:根据大小交换相邻元素的位置，原理就是每次迭代后将最大或最小的元素放到最后
    :param data: 输入数组
    :param reverse: 是否反转，若为true,则为从大到小
    :return:
    """
    for j in range(len(data)-1):#控制每次冒泡排序的长度，一次排序后，需要排序的长度会减少１
        state=0#状态变量，若一次排序中，没有变化，则可以提前停止，减少时间
        for i in range(len(data)-j-1):
            if reverse:
                if data[i]<data[i+1]:
                    state=1
                    data[i],data[i+1]= data[i+1],data[i]
            else:
                if data[i]>data[i+1]:
                    state=1
                    data[i],data[i+1]= data[i+1],data[i]
        if state==0:
            break
    return data
def SelectionSort(data,reverse=False):
    """
    选择排序
    :param data: 输入数组
    :param reverse: 是否反转，若为true,则为从大到小
    :return:
    """
    for j in range(len(data)-1):
        tep=data[j]
        index=j
        for i in range(j,len(data)):
            if reverse:
                if tep<data[i]:
                    tep=data[i]
                    index=i
            else:
                if tep>data[i]:
                    tep=data[i]
                    index=i
        data[j],data[index]=data[index],data[j]
    return data
def InsertSort(data,reverse=False):
    for i in range(1,len(data)):
        num=data[i]
        for j in range(0,i):
            if reverse:
                if num>=data[j]:
                    data.insert(j,num)
                    del data[i + 1]
                    break
            else:
                if num<=data[j]:
                    data.insert(j,num)
                    del data[i + 1]
                    break
    return data
def SheelSort(data,reverse=False):
    dis=int(len(data)/2)
    while dis>0:
        for index in range(dis):
            for i in range(index+dis, len(data),dis):
                num = data[i]
                for j in range(index, i,dis):
                    if reverse:
                        if num >= data[j]:
                            data.insert(j, num)
                            del data[i + 1]
                            break
                    else:
                        if num <= data[j]:
                            data.insert(j, num)
                            del data[i + 1]
                            break
        dis=int(dis/2)
    return data

def MergerSort(data,reverse):
    if len(data)==1:
        return data
    else:
        data1=data[0:len(data)//2]
        data2=data[len(data)//2:]

        return merge(MergerSort(data1,reverse),MergerSort(data2,reverse),reverse=reverse)
def merge(data1,data2,reverse):
    data=[0]*(len(data1)+len(data2))
    if not reverse:
        for i in range(len(data)):
            if len(data1)*len(data2)==0:
                data[i:]=data1 if len(data2)==0 else data2
                break
            if data1[0]<data2[0]:
                data[i]=data1[0]
                del data1[0]
            else:
                data[i]=data2[0]
                del data2[0]
    else:
        for i in range(len(data)):
            if len(data1)*len(data2)==0:
                data[i:]=data1 if len(data2)==0 else data2
                break
            if data1[0]>data2[0]:
                data[i]=data1[0]
                del data1[0]
            else:
                data[i]=data2[0]
                del data2[0]
    return data

data=[1,2,3,3,24,32,1,5,57,123,24,213,12,312,3,24,123,12,3,23,12,31,23,12,3123,16]
data1=[5,2,4,3,2]
print(BubbleSort(data,reverse=False))
print(SelectionSort(data,reverse=False))
print(InsertSort(data,reverse=False))
print(SheelSort(data,reverse=True))
print(MergerSort(data1,reverse=True))


