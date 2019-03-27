from twilio.rest import Client

# Autenticando conforme a sua conta Twilio
account_sid = "ACfc66b4b14d628083302caeddf357225a"
auth_token = "cebe604c62b4c1376238934eff72a378"
client = Client(account_sid, auth_token)

# Criando um método que leva multiplos argumentos
message = client.messages.create(
    to="+5511995672655",
    from_="+18062791930",
    body="Boa noite, segue a imagem de uma coruja, NÃOOO É O GEMIDAO !!!!"),
    media_url='https://demo.twilio.com/owl.png'

print(message.sid)
