# Sending an SMS using the Twilio API
from twilio import rest

# put your own credentials here
account_sid = "ACaf877765944a5bd7a55c53011d66ce1e"# your sid here
auth_token = "636da8b8dbadffe6e66beb6359f3e313" # auth token from twilio
client = rest.Client(account_sid, auth_token)
client.messages.create(
    to="+918233813183",
    from_="+12283258038",
    body="Hey!!! Niranjan",
    media_url="https://climacons.herokuapp.com/clear.png")

print('done')
