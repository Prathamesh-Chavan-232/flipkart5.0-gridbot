import bluetooth
# import nema
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1  # You can choose any available port

server_sock.bind(("", port))
server_sock.listen(1)

print("Waiting for a connection...")

client_sock, client_info = server_sock.accept()
print(f"Accepted connection from {client_info}")

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        
        if data.decode('utf-8').split(sep='.')[0] == 'x':
            print("moving x")
        
        if data.decode('utf-8').split(sep='.')[0] == 'y':
            print("moving y")
            
        if data.decode('utf-8').split(sep='.')[0] == 'z':
            print("moving z")
        # print(f"Received: {data.decode('utf-8')}")
        
        if data.decode('utf-8').split(sep='.')[0] == "exit":
            print("exiting")


except KeyboardInterrupt:
    pass

print("Closing connection...")
client_sock.close()
server_sock.close()
