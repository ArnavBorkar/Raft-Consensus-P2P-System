import time

# set the file path
file_path = 'received_messages.txt'

while True:
    # open the file in write mode, which clears the existing content
    with open(file_path, 'w'):
        pass
    # wait for two seconds
    time.sleep(2)