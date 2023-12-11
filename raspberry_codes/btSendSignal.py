import bluetooth

server_mac_address = 'B8:27:EB:EA:57:AB'  # Replace with Raspberry Pi's Bluetooth address
port = 1  # Make sure it matches the server's port

client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_sock.connect((server_mac_address, port))

while True:
    message = input("Message=")
    client_sock.send(message)
    if message.split(sep='.')[0] == "exit":
        client_sock.close()


