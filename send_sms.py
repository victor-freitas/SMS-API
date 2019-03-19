from twilio.rest import Client

# Autenticando conforme a sua conta Twilio
account_sid = "-- -- SEU SID -- --"
auth_token = "-- -- SEU TOKEN -- --"

client = Client(account_sid, auth_token)

# Criando um método que leva multiplos argumentos
message = client.messages.create(
    to="+5511995672655",
    from_="+18062791930",
    body=" -- -- ISIRA QUALQUER MENSAGEM AQUI -- -- ")

print(message.sid)
