Self-Learning Platform
A Django-based self-learning platform with REST API, JWT authentication, and PostgreSQL database.

Prerequisites
Python 3.8+
PostgreSQL
Git
Installation
Clone the repository:
bash

Copy
git clone <repository-url>
cd self_learning
Create a virtual environment and activate it:
bash

Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
bash

Copy
pip install -r requirements.txt
Configure the database in self_learning/settings.py:
python

Copy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'self_learning_db',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply migrations:
bash

Copy
python manage.py migrate
Create a superuser:
bash

Copy
python manage.py createsuperuser
Run the development server:
bash

Copy
python manage.py runserver
API Documentation
Access the Swagger UI at http://localhost:8000/swagger/.

Testing
Run tests with:

bash

Copy
python manage.py test
Project Structure
users/: User management and authentication.
courses/: Course content management (sections, materials, tests).
self_learning/: Project settings and URLs.
Show in sidebar