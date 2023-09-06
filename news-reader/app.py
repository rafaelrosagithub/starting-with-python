import imaplib
import credentials

host = "imap.gmail.com"
port = 993
user = credentials.user
password = credentials.password

server = imaplib.IMAP4_SSL(host, port)
server.login(user, password)
server.select("Deschamps")
