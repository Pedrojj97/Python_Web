def sort_insert(li):
	for i in range(1,len(li)):
		for j in range(i-1,-1,-1):
			if li[i]> li[j]:
				li.insert(j+1,li[i])
				del li[i+1]
				break
		print(li)
	return li
def sort_insert_hounuo(li):
	for i in range(1,len(li)):
		cur=li[i]
		for j in range(i-1,-1,-1):
			if cur< li[j]:
				li[j+1]=li[j]
			else:
				break
		li[j+1]=cur
		print(li)
	return li



if __name__ == '__main__':
	li=input('输入要排序的列表')
	li=li.split(',')
	li = [int(a) for a in li]
	sort_li=sort_insert_hounuo(li)
	print('排序完的列表:{}'.format(sort_li))
