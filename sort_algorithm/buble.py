def sort_buble(li):
	for i in range(len(li)-1):#只进行n-1趟循环，
		for j in range(0,len(li)-i-1):#无序区减少
			if li[j]>li[j+1]:
				li[j],li[j+1] = li[j+1],li[j]
	return li
def sort_buble_early_stop(li):
	for i in range(len(li)-1):#只进行n-1趟循环
		exchang=False
		for j in range(0,len(li)-i-1):
			if li[j]>li[j+1]:
				exchang=True
				li[j],li[j+1] = li[j+1],li[j]
		if exchang==False:
			break
	return li


if __name__ == '__main__':
	li=input('输入要排序的列表')
	li=li.split(',')
	li = [int(a) for a in li]
	sort_li=sort_buble(li)
	print('排序完的列表:{}'.format(sort_li))