# SarvaSuvidhan - Backend API

This project is a backend system built with Django REST Framework (DRF) for managing form data. It integrates with a PostgreSQL database and exposes APIs for CRUD operations, tested using Postman.

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
           git clone https://github.com/PinjariAbdul/sarvasuvidhan-backend.git
           cd sarvasuvidhan-backend 

2.Create a virtual environment and activate:
   python -m venv apidevelopment
   apidevelopment\Scripts\activate  # On Windows

3.pip install -r requirements.txt



4.Set up PostgreSQL database and add credentials in settings.py:

 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
      }
     }


     
5.Run migrations and start server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
⚙️ Tech Stack
Backend: Django, Django REST Framework
Database: PostgreSQL
Testing: Postman



📡 APIs Implemented
Method	Endpoint	Description
GET	/api/form_data/	List all form entries
POST	/api/form_data/	Create new form entry
PUT	/api/form_data/<id>/	Update specific form
DELETE	/api/form_data/<id>/	Delete specific form
