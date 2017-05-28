---

## Echo server

- echo_server/server.py
- echo_server/client.py


## Installation

- install Rust compiler (see https://github.com/PyO3/tokio)
- $ pip install -r requirement.txt


## Run benchmark
    > Terminal 1: Run server first
    $ python3 echo_server/server.py
    
    > Terminal 2: Run client 
    $ python3 echo_server/client.py

    > Terminal 1: Press ctrl + c for servers stopping 


## Result of benchmark

### Python 3.6.1 (default, Mar 30 2017) [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin)

   tokio - 6.19 sec [16152.81 RPS] 
   libuv - 4.42 sec [22622.09 RPS]
 asyncio - 6.15 sec [16265.43 RPS]

