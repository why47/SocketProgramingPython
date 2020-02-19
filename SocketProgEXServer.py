import socket
def main():
	# membuat Socket baru
	sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Koneksi nya tcp

	host = socket.gethostname()
	port = 12345
	sc.bind((host, port))
	sc.listen(2)

	print("Socket Sedang Listening")

	while True :
		connect, addr = sc.accept()
		print("Mendapat Koneksi Dari "+ str(addr))
		Msg = input("Masukan Pesan Yang Anda? ")
		connect.send(Msg.encode('ascii'))
		connect.close()
		break
if __name__ == '__main__':
			main()		