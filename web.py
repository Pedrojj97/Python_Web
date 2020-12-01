import socket
def server(socket):
	while True:
		request=socket.recv(1024)
		if request.decode()=='close':
			print('关闭连接')
			break
		if not request:#对方调用close时，request为空数据
			print('关闭连接')
			break
		print(request)
		reponse='HTTP/1.1 200 OK\r\n'
		reponse+='\r\n'
		reponse+='<h3>haha<h3>'
		socket.send(reponse.encode('utf-8'))	
	socket.close()
def main():
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind(('',8080))
	server_socket.listen(128)
	while True:
		
		new_socket,client_addr=server_socket.accept()
		print('连接成功')
		server(new_socket)
	server_socket.close()
if __name__ == '__main__':
	main()