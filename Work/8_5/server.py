# server.py

# (b) Generators as Tasks Serving Network Connections
# The idea is that not only will each task yield, 
#   it will indicate a reason for doing so (receiving or sending).
# Depending on the reason, the task will move over to a waiting area.
# The scheduler then runs any available tasks or waits
# for I/O events to occur when nothing is left to do.

from socket import *
from select import select
from collections import deque

tasks = deque()
recv_wait = {}  # sock -> task
send_wait = {}  # sock -> task

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:    # wait for tasks
            # select: wait until one or more file descriptors
            #   are ready for some kind of I/O.
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        # print(tasks)
        task = tasks.popleft()
        try:
            # get a task from tcp server; resource == socket
            reason, resource = task.send(None)
            if reason == 'recv':
                recv_wait[resource] = task
            elif reason == 'send':
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown reason %r' % reason)
        except StopIteration:
            print('Task done')

def tcp_server(address, handler):
    # create a server socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        print('TCP server is running at %s:%s' % (address[0], address[1]))
        sock.bind(address)
        sock.listen(5)
        while True:
            yield 'recv', sock
            # create a client socket
            client, addr = sock.accept()
            tasks.append(handler(client, addr))     # global task list

def echo_handler(client, address):
    '''
        client: python3 -m telnetlib localhost 25000
    '''
    print('Connection from', address)
    while True:
        yield 'recv', client
        data = client.recv(1000)        # receive data from client
        if not data:                    # interrupt client (Ctrl-C)
            break
        yield 'send', client
        client.send(b'GOT:' + data)     # send data to client
    print('Connection closed')

# If it's working, you should see output being echoed back to you.
# if you connect multiple clients, they'll all operate concurrently.

# This tricky use of generators is not something that you would
# likely have to code directly.
if __name__ == '__main__':
    server_task = tcp_server(('localhost', 25000), echo_handler)
    tasks.append(server_task)
    run()

# === SERVER ===
# Connection from ('127.0.0.1', 56893)
# Connection closed
# Task done

# === CLIENT ===
# bash % python3 -m telnetlib localhost 25000
# Hello
# Got: Hello
# World
# Got: World

# === MANAGER ===
# print(tasks)
# deque([<generator object tcp_server at 0x000002437E5B5CF0>])      # server only
# deque([<generator object tcp_server at 0x000002437E5B5CF0>])
# deque([<generator object echo_handler at 0x000002437E8199A0>])    # client
# ...
