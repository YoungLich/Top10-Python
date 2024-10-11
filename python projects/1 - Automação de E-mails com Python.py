import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(destinatarios, assunto, mensagem, anexo=None):
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))

    if anexo:
        with open(anexo, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={anexo}')
            msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(remetente, senha)
    
    for destinatario in destinatarios:
        msg['To'] = destinatario
        server.sendmail(remetente, destinatario, msg.as_string())

    server.quit()

enviar_email(
    ['destino1@exemplo.com', 'destino2@exemplo.com'],
    'Assunto importante',
    'Corpo do e-mail com anexo',
    'relatorio.pdf'
)
