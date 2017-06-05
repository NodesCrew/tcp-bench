# coding: utf-8

import time
import logging
from socket import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("tcp-client")


def benchmark(name, addr, rqty):
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.connect(addr)
    except ConnectionRefusedError:
        logger.warning("Unable to connect to %s / %s", name, addr)
        return

    ts = time.time()
    for n in range(rqty):
        sock.send(b'ping\n')
        resp = sock.recv(5)
        if resp != b'pong\n':
            break
    sock.send(b'exit\n')
    sock.close()

    sec = time.time() - ts
    logger.info("{:>9s} - {:.2f}s [{:.2f} RPS]".format(name, sec, rqty / sec))
    time.sleep(1.)


for i, name in enumerate(["tokio", "libuv", "asyncio", "trio"]):
    time.sleep(1.)
    benchmark(name, ("localhost", 50000 + i), 500000)
