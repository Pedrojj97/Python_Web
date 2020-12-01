import urllib.request

def main():
	ret=urllib.request.urlopen('https://www.baidu.com')
	img=ret.read()
	with open('1.jpg','wb') as f:
		f.write(img)
if __name__ == '__main__':
	main()