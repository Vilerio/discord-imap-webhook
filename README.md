# Script de notification Discord pour les nouveaux e-mails

Ce script utilise IMAP pour surveiller une boîte mail et envoie une notification Discord lorsqu'un nouvel e-mail non lu est reçu.

## Configuration

Assurez-vous d'avoir les dépendances suivantes installées :

- imaplib
- email
- time
- requests
- json

Avant d'exécuter le script, vous devez configurer les paramètres suivants :

- `serveur_imap`: L'adresse du serveur IMAP de votre fournisseur de messagerie (par exemple : `imap.mail.com`).
- `port_imap`: Le port IMAP utilisé par le serveur (par défaut : 993).
- `nom_utilisateur`: Votre nom d'utilisateur ou adresse e-mail.
- `mot_de_passe`: Votre mot de passe.
- `webhook_url`: L'URL du webhook Discord que vous avez créé pour recevoir les notifications.

## Utilisation

Une fois que vous avez configuré les paramètres, vous pouvez exécuter le script en utilisant Python. Il vérifiera périodiquement votre boîte aux lettres et enverra une notification Discord dès qu'un nouvel e-mail non lu est reçu.

Exécutez le script en utilisant la commande suivante :

```shell
python3 script.py
```