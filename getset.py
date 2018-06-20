import socket
from threading import Thread

byte = 0
status = ""
sock = socket.socket()
conn = None
address_file = ""
ip = ""
port = 0

def set_file():
	global conn

	f = open(address_file, 'r')
	str_code = str(f.read())
	f.close()
	conn.send(str_code.encode("utf-8"))
	print()
	print("CODE:",str_code)
	print()

def get_file():
	global conn

	str_code = conn.recv(byte)
	print()
	print("CODE:",str_code.decode("utf-8"))
	print()
	f = open(address_file, 'w')
	f.write(str_code.decode("utf-8"))
	f.close()

def info():
	print()
	print("STATUS:",status)
	print("IP:",ip)
	print("PORT:",port)
	print("ADDRESS:",address_file)
	print("BYTE:",byte)
	print()

def work():
	global byte
	global address_file

	while True:
		i = str(input('@~'))
		if i == "set":
			set_file()
		elif i == "get":
			get_file()
		elif i == "info":
			info()
		elif i == "setbyte":
			byte = int(input("Byte:"))
		elif i == "setaddress":
			address_file = str(input("Address file:"))
		elif i == "exit":
			break
		elif i == "help":
			print()
			print("set")
			print("get")
			print("info")
			print("setbyte")
			print("setaddress")
			print()
		print()

def server():
	global ip
	global port
	global conn
	print("#######Server#######")
	ip = str(input("IP: "))
	port = int(input("PORT: "))

	sock.bind((ip, port))
	sock.listen(1)

	connect_list = []
	address_list = []
	index = 0
	passwort = "hackers"
	exit = 0

	print("Server created.")
	print("Connecting...")
	conn, add = sock.accept()
	print("Connected.")

	work()

	# t = Thread(target=recv, args=(conn,))
	# t.start()

	# while True:
	# 	i = input()
	# 	conn.send(i.encode("utf-8"))

def client():
	global ip
	global port
	global conn

	print("#######Client#######")
	ip = str(input("IP: "))
	port = int(input("PORT: "))

	conn = socket.socket()
	conn.connect((ip , port))

	print("Client created.")
	print("Connecting...")
	print("Connected.")

	work()

def main():
	global address_file
	global byte
	global status

	address_file = str(input("Address file:"))
	byte = int(input("Byte:"))
	msg = input("s/c ?: ")
	if msg == "s":
		status = "server"
		server()
	elif msg == "c":
		status = "client"
		client()

		
	
	


if __name__ == '__main__':
	print("hello")
	main()
