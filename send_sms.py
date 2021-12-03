from twilio.rest import Client

# Autenticando conforme a sua conta Twilio
account_sid = "ACfc66b4b14d628083302caeddf357225a"
auth_token = "cebe604c62b4c1376238934eff72a378"
client = Client(account_sid, auth_token)

# Criando um método que leva multiplos argumentos
message = client.messages.create(
    to="telefone",
    from_="telefone",
    body=" Type ur message here =D")

print(message.sid)
