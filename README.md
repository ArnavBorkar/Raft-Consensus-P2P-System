# Raft Consensus based P2P System
Project Goals: 

- A Fault-tolerant distributed P2P System where nodes exchange messages using ZeroMQ, which are stored in a distributed database

- A leader selection mechanism with heartbeat signals based on the Raft Consensus Algorithm



## Usage
This project can be run over any local network, where the nodes are able to ping each other. As of now, the project uses 3 nodes as a base, but number of nodes can be simply modified in the script.

### Requirements
- Python3 , ZeroMQ


### Commands
- To start the project first run client.py on all nodes
```
$ python3 client.py
```
- Then run server.py and server_help.py on one leader node
```
$ python3 server.py
$ python3 server_help.py

```
- Then run client_recv.py on all the nodes
```
$ python3 client_recv.py
```
- Finally leader_send.py on the leader node
```
$ python3 client_recv.py
```

## Results

- You can see the Raft Consensus based results in distributed database data.txt, the values are consistent accross all the systems.

- When all the values are sent to the leader, the leader chooses one of the value and then sends that to all the other nodes.

- The received_messages.txt is a temporary database in the leader, that chooses one of all the messages received by its peer



