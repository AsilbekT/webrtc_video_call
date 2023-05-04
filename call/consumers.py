# call/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CallConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        # response to client, that we are connected.
        self.send(text_data=json.dumps({
            'type': 'connection',
            'data': {
                'message': "Connected"
            }
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.my_name,
            self.channel_name
        )

    # Receive message from client WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

        eventType = text_data_json['type']

        if eventType == "store_user":
            name = text_data_json['name']
            print(name)
            self.my_name = name

            # Join room
            async_to_sync(self.channel_layer.group_add)(
                self.my_name,
                self.channel_name
            )

        if eventType == 'login':
            name = text_data_json['data']['name']
            print(name)
            self.my_name = name

            # Join room
            async_to_sync(self.channel_layer.group_add)(
                self.my_name,
                self.channel_name
            )

        if eventType == 'call':
            name = text_data_json['data']['name']
            print(self.my_name, "is calling", name)


            async_to_sync(self.channel_layer.group_send)(
                name,
                {
                    'type': 'call_received',
                    'name': self.my_name,
                    'data': text_data_json['data']['rtcMessage']['sdp']
                }
            )

        if eventType == 'create_answer':

            target = text_data_json['target']
            data = {"type": "answer", "sdp": text_data_json['data']['sdp']}
            async_to_sync(self.channel_layer.group_send)(
                target,
                {
                    'type': 'call_answered',
                    'data': {"rtcMessage": data}
                }
            )

        if eventType == 'ice_candidate':

            if 'target' in text_data_json.keys():

                user = text_data_json['target']

                async_to_sync(self.channel_layer.group_send)(
                    user,
                    {
                        'type': 'ice_candidate',
                        'data': text_data_json['data']
                    }
                )
            else:
                user = text_data_json['data']['user']
                async_to_sync(self.channel_layer.group_send)(
                    user,
                    {
                        'type': 'ice_candidate',
                        'data': text_data_json['data']['rtcMessage']
                    }
                )

    def call_received(self, event):

        print('Call received by ', self.my_name)
        self.send(text_data=json.dumps({
            'type': 'offer_received',
            'name': event['name'],
            'data': event['data']
        }))

    def call_answered(self, event):

        print(self.my_name, "'s call answered")
        self.send(text_data=json.dumps({
            'type': 'call_answered',
            'data': event['data']
        }))

    def ice_candidate(self, event):
        self.send(text_data=json.dumps({
            'type': 'ice_candidate',
            'data': event['data']
        }))
