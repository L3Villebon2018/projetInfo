# Comment installer GetBeaned sur votre propre infrastructure ?

## Prérequis

- Un serveur Ubuntu supporté avec une IPV4 publique
- Un client SSH (Putty sous windows, `ssh` sous unix)
- Python 3.6+ sur le serveur (utilisez `pyenv` au besoin)
- Postgres SQL avec un utilisateur, sa base associée et son mot de passe
- Un nom de domaine A -> IPV4 publique du serveur
- Gunicorn installé (CF [ce tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn))

> A noter : DigitalOcean propose aussi un serveur Django pré-configuré. Celui-ci peut faire l'affaire lors de l'installation

## Instalation des requirements

### Python

- Vérifiez la version de python installée, `python3 --version`
- Vérifiez la version de pip3 instalée `pip3 --version`

Les deux versions doivent etres ≥ 3.6 pour python et ≥ 10 pour PIP

- Installez les requirements `pip3 install -U -r requirements.txt`
- Activez un environnement python virtuel (VENV) si vous le shouaitez (conseillé, tutoriels sur le net)
- Si erreur d'installation, **vous n'avez pas activé de VENV**, utilisez `sudo !!` pour relancer la commande précédenteen tant que SU

### Nginx

- Installez nginx et creez un site web avec une configuration similaire à 

```nginx
upstream app_server {
    server unix:/home/django/gunicorn.socket fail_timeout=0;
}

server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    client_max_body_size 4G;
    server_name _;

    keepalive_timeout 5;

    # Your Django project's media files - amend as required
    location /media  {
        alias /home/django/django_project/charpaknetwork/ProjetInfoL3/media;
    }

    # your Django project's static files - amend as required
    location /static {
        alias /home/django/django_project/charpaknetwork/ProjetInfoL3/static;
    }

    # Proxy the static assests for the Django Admin panel
    #location /static/admin {
    #   alias /usr/lib/python3.6/dist-packages/django/contrib/admin/static/admin/;
    #}

    location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
            proxy_buffering off;

            proxy_pass http://app_server;
    }

}
```

Pensez à remplacer `/home/django/django_project/charpaknetwork/ProjetInfoL3/` en faisant pointer le chemin vers le répertoire ou vous avez téléchargé les fichiers du site sur votre serveur, et `/home/django/gunicorn.socket` par le chemin vers la socket Gunicorn 

### Gunicorn

Gunicorn devrait etre installé. Modifiez `unicorn.service` (de systemd) pour que la ligne de démarrage ressemble à:

`/usr/local/bin/gunicorn --name=PIL3 --pythonpath=/home/django/django_project/charpaknetwork --bind unix:/home/django/gunicorn.socket --config /etc/gunicorn.d/gunicorn.py ProjetInfoL3.wsgi:application`

En corrigeant si nécéssaire les chemins d'accés.

## Configuration

Dans le fichier `ProjetInfoL3/settings.py`, éditez les options suivantes :

- `ALLOWED_HOSTS = ["charpaknetwork.api-d.com", "localhost", "127.0.0.1"] + ip_addresses()` en remplacant `charpaknetwork.api-d.com` par votre nom de domaine
- Configurez la base de données en suivant le lien indiqué en commentaires. Vous devez faire figurer le port, l'utilisateur, le mot de passe et la base crée lors des prérequis
```python
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Lancement du site

- `systemctl daemon-reload`
- `service guinicorn restart`
- `service nginx restart`

### HTTPs

- Utilisez certbot, CF [la page de l'EFF](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx)


Tout devrait fonctionner, tentez un reboot pour redémarrer la machine

