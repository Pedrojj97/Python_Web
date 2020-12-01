import multiprocessing

q= multiprocessing.Queue(3)

def download(q):
	data=[1,2,3]
	for i in data:
		q.put(i)

def handle(q):
	data=list()
	while True:
		data.append(q.get())
		if q.empty():
			break
	print('下载的数据为{}'.format(data))
def main():
	p1=multiprocessing.Process(target=download,args=(q,))
	p2=multiprocessing.Process(target=handle,args=(q,))
	p1.start()
	p2.start()


if __name__ == '__main__':
	main()