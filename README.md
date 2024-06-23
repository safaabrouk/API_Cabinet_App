# API_Cabinet_App

Si vous clonez ce projet vous devez suivre les étapes suivantes pour assurer le bonne fontionnement :

### 1. creer dans ce dossier un environnement virtuel par :

python -m venv NomEnvironnement

### 2. Installer les outils suivant :

- pip install django
- pip install djangorestframework
- pip install mysqlclient
- pip install coreapi
- pip install django-cors-headers
- pip install djangorestframework_simplejwt

### 3. Create MySql Database:

Date base should have as name cabinet-app.

### 4. Run application

For the first time we need create admin profil before runing the application with this commands :

```properties
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser
```

For run project

```properties
python manage.py runserver
```
