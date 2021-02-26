# Piscine Python-Django de l'école 42

## Installation de l'environnement virtuel python

```shell
python3 -m venv env

source env/bin/activate
```
## Installation de Django dans l'environnement virtuel

```shell
pip install django
```

## Installation des bibliothèques avec fichier requirement.txt

```shell
pip install -r requirement.txt
```

## Démarrage du server postgres
```shell
pg_ctl -D <le chemin vers>/.brew/var/postgres start
```