# 🧠 Backend - Yendu Bi (Django REST API)

Ce dossier contient le backend de l'application **Yendu Bi**, un système de gestion pour un espace de jeux. Il est développé avec **Django** et **Django REST Framework** pour fournir une API robuste, sécurisée et performante.

---
## ⚙️ Fonctionnalités principales

- API RESTful pour la gestion des utilisateurs (clients, caissiers, admins)
- Gestion des paiements et consommations
- Génération et validation de QR codes clients
- Historique des activités
- Statistiques journalières
- Authentification et permissions selon les rôles

---

## 🛠️ Technologies utilisées

- [Python 3.10+](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- SQLite (en développement) / PostgreSQL (en production)

---
# 📁 APP & (Fonction)
- api (initialisation test)
- authapp (authentification)
- userpanel (interface utilisateur)

--- 

## 📁 Guide d'utilisation
- Appliquer les migrations et Lancer le serveur

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

