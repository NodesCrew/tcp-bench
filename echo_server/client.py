# coding: utf-8

from socket import *
import time


def benchmark(name, addr, messages):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(addr)
    t_start = time.time()
    for n in range(messages):
        sock.send(b'ping\n')
        resp = sock.recv(5)
        if resp != b'pong\n':
            break
    sock.send(b'exit\n')
    sock.close()

    sec = time.time() - t_start
    print("{:>9s} - {:.2f} sec [{:.2f} RPS]".format(name, sec, messages / sec))
    time.sleep(1.)


for i, name in enumerate(["tokio", "libuv", "asyncio"]):
    time.sleep(1.)
    benchmark(name, ("localhost", 50000 + i), 100000)
