# E-commerce Project

This is a comprehensive e-commerce platform built with Django. The platform includes features such as user authentication, product listing, cart management, order processing, and payment integration.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Project Screenshots](#project-screenshots)

## Features

- User authentication (login, signup, password reset)
- Product listing and categorization
- Shopping cart functionality
- Order processing
- Payment gateway integration
- Email notifications
- Admin panel for managing products, orders, and users

## Technologies

- Python 3.10+
- Django 4.0+
- Django REST Framework
- PostgreSQL
- Stripe (for payment processing)
- Bootstrap (for frontend styling)
- Docker (optional, for containerization)

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL
- Node.js and npm (for frontend dependencies, optional)
- Docker (optional)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YaminLamBappi/onlineshop
   cd onlineshop

    Create and activate a virtual environment:

    bash
   ```

python -m venv env
source env/bin/activate # On Windows use `env\Scripts\activate`

Install the dependencies:

bash

pip install -r requirements.txt

Install frontend dependencies (optional, if using npm):

bash

npm install

Set up the database:

Create a PostgreSQL database and configure the database settings in settings.py.

python

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'your_db_name',
'USER': 'your_db_user',
'PASSWORD': 'your_db_password',
'HOST': 'localhost',
'PORT': '5432',
}
}

Run migrations:

bash

python manage.py migrate

Create a superuser:

bash

python manage.py createsuperuser

Collect static files:

bash

    python manage.py collectstatic

Configuration
Environment Variables

Create a .env file in the project root and add the following environment variables:

plaintext

SECRET_KEY=your_secret_key
DEBUG=True # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1,[your_domain]
DATABASE_URL=postgres://your_db_user:your_db_password@localhost/your_db_name
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password

Static Files Configuration

Ensure that the STATIC_ROOT and MEDIA_ROOT settings are correctly configured in settings.py:

python

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

Usage

    Run the development server:

    bash

    python manage.py runserver

    Access the site: Open your browser and navigate to http://127.0.0.1:8000/.

    Access the admin panel: Navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials.

Running Tests

To run the tests, use the following command:

bash

python manage.py test

Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch for your feature or bugfix.
    Make your changes and commit them with clear messages.
    Push your changes to your fork.
    Open a pull request to the main repository.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Project Screenshots


  <li>Project Screenshot 1
    <img src="media/project_image/Screenshot.png" alt="Project Screenshot 1"><br><br>
    <video width="320" height="240" controls>
  <source src="media/project_image/project_demo.webm" type="video/mp4">
</video> 
  </li>
  
<video width="320" height="240" controls>
  <source src="media/project_image/project_demo.webm" type="video/mp4">
</video> 

