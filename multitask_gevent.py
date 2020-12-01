import gevent
from gevent import monkey
import time
monkey.patch_all()#打包，将所有延时操作换成gevent的函数，如sleep recieve等
	
def task1(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		time.sleep(1)
def task2(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		time.sleep(1)
def task3(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		time.sleep(1)
# g1=gevent.spawn(task1,5)
# g2=gevent.spawn(task2,5)
# g3=gevent.spawn(task3,5)
# g1.join()
# g2.join()
# g3.join()
gevent.joinall([
	gevent.spawn(task1,5),
	gevent.spawn(task2,5),
	gevent.spawn(task3,5)
	])