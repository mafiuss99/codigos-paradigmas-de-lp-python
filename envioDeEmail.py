from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
texto = "Texto da mensagem"

senha = "suaSenha
msg['From'] = "Seu email"
msg['To'] = "Email de destino"
msg['Subject'] = "Assunto da mensagem"

msg.attach(MIMEText(texto, 'plain'))

#Criação do servidor"
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da Mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')