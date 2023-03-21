import zmq
import time

context = zmq.Context()

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://10.8.1.45:5557")
i=0
while True:
    # Get current time stamp
    timestamp = time.time()
    # Create message with timestamp and string
    message = "Mac 1 --- {} --- This is message{}".format(timestamp, i)
    i+=1
    # Send message to receiver
    sender.send(message.encode())
    
    # Wait for 1 second before sending next message
    time.sleep(1)
#CLIENT