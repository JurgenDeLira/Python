# wdts vdde ylzn bvic

from flask import Flask, request
import email
from email.message import EmailMessage
import ssl

# Librería del protoocolo SMTP
import smtplib

# Librería del protocolo IMAP
import imaplib

# Librería para decodificar el correo electrónico
from email.header import decode_header

# Nos permite enviar correos con otra estructura
from email.mime.multipart import MIMEMultipart

# Nos permite enviar correos en texto plano
from email.mime.text import MIMEText


# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
port = 465  # para SSL
email_sender = 'mailbotjose@gmail.com'
email_password = 'ridexgkcnjgutaoz' # <- Cambiar contraseña


# --------------------------------------------------------------------------
def enviar_correo(mailreciever, asuntomail, cuerpomail):

    email_reciever = mailreciever

    asunto = asuntomail

    cuerpo = cuerpomail

    email = EmailMessage()

    email['From'] = email_sender

    email['To'] = email_reciever

    email['Subject'] = asunto

    email.set_content(cuerpo)


    # Creamos un contexto seguro para el correo
    context = ssl.create_default_context()


        # Enviamos el correo electrónico encriptado
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, email.as_string())
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
def correo_respuesta(mailreciever, asuntomail):
    mensaje = MIMEMultipart('alternativo')

    mensaje['To'] = mailreciever
    mensaje['Subject'] = asuntomail + ' <> Respuesta a correo'
    mensaje['From'] = email_sender

    # Crear la versión en texto plano del mensaje
    texto_plano = MIMEText("Este es el mensaje en texto plano.", "plain")

    # Crear la versión en HTML del mensaje
    html = MIMEText("""
    <html>
        <body>
            <h1 style="color: red;">Respuesta</h1>
            <p>Este es el mensaje en <b>HTML</b>.</p>
        </body>
    </html>
    """, "html") 

    # Adjuntar ambas versiones al mensaje MIMEMultipart
    mensaje.attach(texto_plano)
    mensaje.attach(html)
   
    # Creamos un contexto seguro para el correo
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, mailreciever, mensaje.as_string())  
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
def leer_correos_no_vistos(): 
    imap_url = 'imap.gmail.com'
    # Conexión y autenticación
    mail = imaplib.IMAP4_SSL(imap_url)

    mail.login(email_sender, email_password)

    mail.select('inbox')  # selecciona la bandeja de entrada

    status, messages = mail.search(None, '(UNSEEN)')

    if status == 'OK':
        for num in messages[0].split():
            status, data = mail.fetch(num, '(RFC822)')
            if status == 'OK':
                # Decodificamos ese mensaje de bytes a String
                mensaje = email.message_from_bytes(data[0][1])

                # Decodificamos específicamente el asunto
                asunto = decode_header(mensaje['Subject'])[0][0]

                # Verificamos si el asunto viene en Bytes            
                if isinstance(asunto, bytes):
                    # si es un objeto bytes, decodifica a string
                    asunto = asunto.decode()
                # Obtenemos de donde viene ese correo
                destino = mensaje.get('From')
                print("Nuevo mensaje de:", destino.split()[1])
                print("Asunto:", asunto)

                correo_respuesta(destino.split()[1], asunto)
# --------------------------------------------------------------------------





app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola mundo</p>"

@app.route('/enviar_correo', methods=['POST'])
def enviar():

    entrada_json = request.get_json(force=True)

    enviar_correo(entrada_json['correo'], entrada_json['asunto'], entrada_json['cuerpo'])
    
    return f'Se envió el correo con al usuario: {entrada_json["correo"]}'

@app.route('/leer_correos')
def leer_correos():
    leer_correos_no_vistos()
    return 'Ve tu consola :D'

app.run(debug=True, port=5050)