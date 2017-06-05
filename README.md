---

## TCP echo-servers benchmarking (for Python 3.6+)

## Installation

- install Rust compiler (see https://github.com/PyO3/tokio)
- install requirements:

```{r, engine='bash', install}
mkvirtualenv tcp-bench -p python3.6
pip install -r requirement.txt
```


## Connection handler pseudo-code

```{r, engine='python', algo}
while True:
    data = socket.read(5)
    if data == b"ping\n":
        socket.write(b"pong\n")
    else:
        break
```



## Run benchmark
    > Terminal 1: Run server first
    $ python3 tcp-bench/server_asyncio.py

    > Terminal 2: Run Trio server
    $ python3 tcp-bench/server_trio.py

    > Terminal 3: Run client
    $ python3 tcp-bench/client.py


## Last results (MacBookPro, i7-6820HQ CPU @ 2.70GHz)

| Test    | Interpreter      | Time   | RPS      |
|---------|------------------|--------|----------|
| trio    | pypy 5.7.1-beta0 | 19.82s | 25230.85 |
| asyncio | pypy 5.7.1-beta0 | 21.17s | 23618.00 |
| libuv   | python3.6        | 22.24s | 22481.92 |
| trio    | python3.6        | 26.46s | 18894.47 |
| tokio   | python3.6        | 31.14s | 16054.65 |
| asyncio | python3.6        | 32.98s | 15158.57 |