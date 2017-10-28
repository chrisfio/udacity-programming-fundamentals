from twilio.rest import Client

# Account Sid and Auth Token from twilio.com/user/account
account_sid = #twilio 
auth_token = #twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
    to=""#phonenumber,
    from_=""#twiliophonenumber,
    body="Hello, this is a test text")
print(message.sid)
