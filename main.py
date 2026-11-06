import socket

from fastapi import FastAPI

app = FastAPI()


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # no packet is sent; it just picks the internet-facing interface
        return s.getsockname()[0]
    finally:
        s.close()


@app.get("/")
def root():
    return {"message": "it works !"}


@app.get("/greeting")
def greeting(name: str):
    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": socket.gethostname(),
        "IP": get_ip(),
    }