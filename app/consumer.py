import json

from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):

    def receive(self, text_data=None, bytes_data=None):
        obj = json.loads(text_data)
        print("received: ", obj)

        json_string: str = json.dumps({
            "content": obj["content"],
            "user": obj["user"]
        })
        # self.send(f"You said: {text_data}")
        self.send(json_string)
