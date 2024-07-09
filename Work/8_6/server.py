# server.py

# (b) Wrapping a Socket

from socket import *
from select import select
from collections import deque
from gensocket import GenSocket

tasks = deque()
recv_wait = {}  # sock -> task
send_wait = {}  # sock -> task

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:    # wait for tasks
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
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
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    print('TCP server is running at %s:%s' % (address[0], address[1]))
    sock.listen(5)
    while True:
        client, addr = yield from sock.accept()     # type(client) == <class 'gensocket.GenSocket'>
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    '''
        client: python3 -m telnetlib localhost 25000
    '''
    print('Connection from', address)
    while True:
        data = yield from client.recv(1000)
        if not data:
            break
        yield from client.send(b'GOT:' + data)
    print('Connection closed')


if __name__ == '__main__':
    server_task = tcp_server(('localhost', 25000), echo_handler)
    tasks.append(server_task)
    run()
