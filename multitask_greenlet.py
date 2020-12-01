from greenlet import greenlet
import time
def task1():
	while True:
		print('----1----')
		gr2.switch()
		time.sleep(1)
		
def task2():
	while True:
		print('----2----')
		gr1.switch()
		time.sleep(1)	
gr1=greenlet(task1)
gr2=greenlet(task2)		
def main():

	gr1.switch()
if __name__ == '__main__':
	main()