import time
import threading
num=0

def sing(nums):
	global num
	for i in range(nums):
		num+=1
	print('sing{}'.format(num))

def dance(nums):
	global num
	for i in range(nums):
		num+=1
	print('dance{}'.format(num))
def main():
	t1 = threading.Thread(target=sing,args=(10000000,))

	t2 = threading.Thread(target=dance,args=(10000000,))
	t1.start()
	t2.start()
	time.sleep(2)
	print(num)
if __name__ == '__main__':
	main()