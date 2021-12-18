from fastapi import FastAPI

from pydantic import BaseModel, Field

app = FastAPI()


class RequestSoundChannel(BaseModel):
    channel: str
    muteValue: int


def send(channel, muteValue):
    from pythonosc.udp_client import SimpleUDPClient

    ip = "192.168.1.167"
    port = 10023

    client = SimpleUDPClient(ip, port)  # Create client

    client.send_message("/ch/%s/mix/on" % channel, muteValue)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/sound")
async def setMute(options: RequestSoundChannel):
    send(options.channel, options.muteValue)
    return {"message": "ok"}
