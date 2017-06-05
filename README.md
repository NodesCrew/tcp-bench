---

## Small asyncio eventloop and TCP frameworks benchmarks (for Python 3.6+)

- echo_server/server.py
- echo_server/server_trio.py
- echo_server/client.py



## Installation

- install Rust compiler (see https://github.com/PyO3/tokio)
- install Trio library (see https://trio.readthedocs.io/en/latest/index.html or next step)
- $ pip install -r requirement.txt


## Run benchmark
    > Terminal 1: Run server first
    $ python3 echo_server/server.py

    > Terminal 2: Run Trio server
    $ python3 echo_server/server_trio.py

    > Terminal 3: Run client
    $ python3 echo_server/client.py


## Result of benchmark

##### Python 3.6.1 (default, Mar 30 2017) [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin)
    >    tokio - 30.84 sec [16210.16 RPS]
    >    libuv - 21.81 sec [22923.41 RPS]
    >  asyncio - 31.58 sec [15830.79 RPS]
    >     trio - 25.72 sec [19439.32 RPS]

##### Python 3.5.3 (May 20 2017) [PyPy 5.7.1-beta0 with GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
    >  asyncio - 21.38 sec [23389.53 RPS]
    >     trio - 18.67 sec [26785.16 RPS]

