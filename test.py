import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC5bcf11960bd1e8138953d123023da040'
auth_token = 'cae32879efca4f451c84f99ce4093ed5'
client = Client(account_sid, auth_token)

token = client.tokens.create()

print(token.ice_servers)
