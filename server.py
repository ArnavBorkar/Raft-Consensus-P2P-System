import zmq
import time

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5557")

# Open file for writing messages
f = open("received_messages.txt", "a")

while True:
    # Wait for next message from the network
    message = receiver.recv()
    
    # Get current time stamp
    timestamp = time.time()
    
    # Write message and timestamp to file
    f.write("{}\n".format(message))
    f.flush()
    
    # Print message to terminal
    print("{}\n".format(message))
    