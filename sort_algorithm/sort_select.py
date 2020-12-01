def sort_select(li):#
	for i in range(len(li)-1):#有序区域增长
		for j in range(i+1,len(li)):#无序区域减少
			if li[i]>li[j]:
				li[i],li[j]=li[j],li[i]#可以记录最小的值，这样就不用每次交换了
	return li
def sort_select_(li):#
	for i in range(len(li)-1):#有序区域增长
		min_index=i
		for j in range(i+1,len(li)):#无序区域减少
			if li[j]<li[min_index]:
				min_index=j#可以记录最小的值，这样就不用每次交换了
		li[i],li[min_index]=li[min_index],lip[i]
	return li



if __name__ == '__main__':
	li=input('输入要排序的列表')
	li=li.split(',')
	li = [int(a) for a in li]
	sort_li=sort_select(li)
	print('排序完的列表:{}'.format(sort_li))