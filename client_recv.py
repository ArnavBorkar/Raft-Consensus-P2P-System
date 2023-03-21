import zmq

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5559")

# Open file for writing messages
f = open("data.txt", "a")

while True:
    # Wait for next message from the network
    message = receiver.recv()
    
    # Write message to file
    f.write(message.decode() + "\n")
    f.flush()