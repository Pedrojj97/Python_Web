import socket
def send(tep_socket):
	des_ip=input('请输入目标IP')
	des_port=int(input('请输入目标端口'))
	data=input('请输入要发送的信息')
	tep_socket.sendto(data.encode('utf-8'),(des_ip,des_port))

def recieve(tep_socket):
	data,address=tep_socket.recvfrom(1024)
	print(data.decode('utf-8'))

def main():
	tep_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	tep_socket.bind(('',7788))
	while True:
		send(tep_socket)
		recieve(tep_socket)
if __name__ == '__main__':
	main()