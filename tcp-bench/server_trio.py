""" Not loop testing, jff
    based on https://trio.readthedocs.io/en/latest/tutorial.html#an-echo-server-low-level-api
"""
import trio

PORT = 50003


async def echo_server(server_sock, ident):
    with server_sock:
        print("echo_server {}: started".format(ident))
        try:
            while True:
                data = await server_sock.recv(5)
                if data == b"ping\n":
                    await server_sock.sendall(b"pong\n")
                else:
                    break

        except Exception as exc:
            # Unhandled exceptions will propagate into our parent and take
            # down the whole program. If the exception is KeyboardInterrupt,
            # that's what we want, but otherwise maybe not...
            print("echo_server {}: crashed: {!r}".format(ident, exc))


async def echo_listener(nursery):
    with trio.socket.socket() as listen_sock:
        listen_sock.bind(("127.0.0.1", PORT))
        listen_sock.listen()
        print("echo_listener: listening on 127.0.0.1:{}".format(PORT))

        ident = 0
        while True:
            server_sock, _ = await listen_sock.accept()
            print("echo_listener: got new connection, spawning echo_server")
            ident += 1
            nursery.spawn(echo_server, server_sock, ident)


async def parent():
    async with trio.open_nursery() as nursery:
        print("parent: spawning echo_listener")
        nursery.spawn(echo_listener, nursery)


trio.run(parent)
