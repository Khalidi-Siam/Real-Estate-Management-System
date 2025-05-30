# Real Estate Management System

A comprehensive Django-based Real Estate Management System that provides a platform for property listings, auctions, agent management, and user interactions.


## Technology Stack

- **Backend**: Django 5.0.2
- **Database**: SQLite (development), easily configurable for PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Forms**: Django Crispy Forms with Bootstrap 5 styling
- **File Handling**: PIL (Pillow) for image processing
- **Payment**: Stripe integration
- **Environment**: django-environ for configuration management

## Project Structure

```
RealEstate/
├── manage.py                      # Django management script
├── RealEstate/                    # Main project configuration
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration
├── authentication/               # User authentication & profiles
├── property/                     # Property management
├── auction/                      # Auction system
├── Agents/                       # Agent management & bookings
├── Payment/                      # Payment processing
├── basic/                        # Basic pages & utilities
├── templates/                    # HTML templates
└── static/                       # Static files (CSS, JS, images)
```

## Installation Guide

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Real-Estate-Management-System.git
cd Real-Estate-Management-System
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create a `.env` file in the root directory (optional, for production):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=

DB_NAME=mydatabase
DB_USER=mydbuser
DB_PASSWORD=mysecretpassword
DB_HOST=host
DB_PORT=port_number

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "abc@gmail.com"
EMAIL_HOST_PASSWORD = "your password"

STRIPE_PUBLIC_KEY = 'private_secret_key'
STRIPE_SECRET_KEY = 'public_secret_key'
STRIPE_WEBHOOK_SECRET = ''
```

### Step 5: Database Setup

```bash
# Navigate to the Django project directory
cd RealEstate

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### Step 6: Collect Static Files

```bash
python manage.py collectstatic
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`


For detailed feature information, see `PROJECT_FEATURES.md`.

**Note**: This is a development version. For production deployment, ensure proper security configurations, use a production database, and configure appropriate environment variables.