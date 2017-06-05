# coding: utf-8
import sys
import time
import asyncio
import logging
import contextlib
import asyncio.streams
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("tcp-server")

if sys.version_info.major < 3 or sys.version_info.minor < 5:
    logger.fatal("Python 3.5+ required")
    sys.exit(1)

try:
    import tokio
except ImportError:
    logger.warning("Unable to import tokio")
    tokio = None


try:
    import uvloop
except ImportError:
    logger.warning("Unable to import uvloop")
    uvloop = None


async def client_handler(reader, writer):
    data = None
    while True:
        with contextlib.suppress(asyncio.streams.IncompleteReadError):
            data = await reader.readexactly(5)
            if data == b"ping\n":
                writer.write(b"pong\n")
            else:
                await writer.drain()
                break

    logger.info("Close connection")
    writer.close()


def run_server(module, port):
    if module is None:
        return
    loop = module.new_event_loop()
    coro = asyncio.start_server(client_handler, "127.0.0.1", port, loop=loop)
    server = loop.run_until_complete(coro)

    logger.info("Serving with {}".format(module.__name__))

    try:
        loop.run_forever()
        server.close()
        loop.run_until_complete(server.wait_closed())

    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()


threads = [
    threading.Thread(target=run_server, args=(tokio, 50000)),
    threading.Thread(target=run_server, args=(uvloop, 50001)),
    threading.Thread(target=run_server, args=(asyncio, 50002))
]

try:
    logger.info("Starting threads")

    for t in threads:
        t.daemon = True
        t.start()

    while threading.active_count() > 0:
        threads = [t for t in threads if t.join(.01) or t.is_alive()]

except KeyboardInterrupt:
    logger.info("Stopping threads")
    for t in threads:
        t.join(0.01)
        t.is_alive()
    logger.info("Threads has been stopped")
    sys.exit(-1)

