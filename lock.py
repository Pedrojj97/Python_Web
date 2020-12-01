import time
import threading
num=0

def sing(nums):
	global num
	mutex.acquire()
	for i in range(nums):
		num+=1
	mutex.release()
	print('sing{}'.format(num))

def dance(nums):
	global num
	mutex.acquire()
	for i in range(nums):
		num+=1
	mutex.release()
	print('dance{}'.format(num))
mutex=threading.Lock()#创建锁
def main():
	t1 = threading.Thread(target=sing,args=(10000000,))

	t2 = threading.Thread(target=dance,args=(10000000,))
	t1.start()
	t2.start()
	time.sleep(2)
	print(num)
if __name__ == '__main__':
	main()