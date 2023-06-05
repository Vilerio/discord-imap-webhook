import imaplib
import email
import time
import requests
import json


serveur_imap = 'imap.mail.com'
port_imap = 993
nom_utilisateur = 'email'
mot_de_passe = 'mot de passe'
webhook_url = 'url du webhook'


def envoyer_message_discord(contenu):
    data = {
        'content': '',
        'embeds': [{
            'title': 'Nouveau mail reçu',
            'description': contenu,
            'color': 16711680  
        }]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    

def verifier_nouveau_mail():
    mail = imaplib.IMAP4_SSL(serveur_imap, port_imap)
    mail.login(nom_utilisateur, mot_de_passe)
    mail.select('INBOX')
    result, data = mail.search(None, 'UNSEEN')  
    ids = data[0].split()

    if ids:
        latest_email_id = ids[-1]
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        sujet = msg['Subject']
        corps = ''

        if msg.is_multipart():
            for part in msg.get_payload():
                if part.get_content_type() == 'text/plain':
                    corps = part.get_payload()
                    break
        else:
            corps = msg.get_payload()

        contenu = f'**Sujet** : {sujet}\n\n**Contenu** : {corps}'
        envoyer_message_discord(contenu)

    mail.logout()


while True:
    verifier_nouveau_mail()
    time.sleep(60) 

