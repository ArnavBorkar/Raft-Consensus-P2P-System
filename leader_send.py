import time
import zmq

context = zmq.Context()

# IP addresses to send messages to
ip_addresses = ["10.8.1.45", "10.8.1.48", "10.8.1.44"]

while True:
    # Read next line of message_received.txt
    with open("received_messages.txt", "r") as f:
        message = f.readline().strip()

    # Send message to each IP address
    for ip_address in ip_addresses:
        socket = context.socket(zmq.PUSH)
        socket.connect(f"tcp://{ip_address}:5559")
        socket.send(message.encode())

    # Sleep for 1 second before sending next message
    time.sleep(1)