## Workers Records API

This project is a **Workers Records API** built with **Django** and **Django REST Framework**. It allows users to manage worker data through CRUD operations (Create, Read, Update, Delete). The project leverages **PostgreSQL** as the database and includes robust logging to track API requests.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete worker data.
- **Logging**: Tracks API requests and responses for debugging and monitoring.
- **Database Configuration**: Uses PostgreSQL for data storage and easy management.

## Technologies Used
- **Django**: Web framework for building the API.
- **Django REST Framework (DRF)**: For creating RESTful APIs.
- **PostgreSQL**: Database for storing worker data.
- **Python-Decouple**: For managing environment variables securely.

## Installation

### Requirements
- Python 3.9+
- Django 5.1.4
- Django REST Framework 3.15.2
- PostgreSQL 13+

### Setup Steps

1. **Clone the repository to your local machine**:
    ```bash
    git clone <repository-url>
    ```

2. **Navigate into the project directory**:
    ```bash
    cd <project-directory>
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the PostgreSQL database**:
    - Ensure PostgreSQL is installed and running.
    - Create a PostgreSQL database:
      ```sql
      CREATE DATABASE workers_db;
      ```
    - Configure PostgreSQL connection in `settings.py`: Update the `DATABASES` section with your PostgreSQL credentials.
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'workers_db',
              'USER': 'postgres',
              'PASSWORD': config('PASSWORD'),
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```

6. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

    The application will be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

  ### Project Structure
  
    workforce/
    ├── worker/
        │   ├── migrations/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── serializers.py
        |   ├── tests.py
        │   ├── views.py
        │   └── urls.py
        ├── workforce/
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        │   └── asgi.py
        ├── manage.py






## API Endpoints

- **GET /api/worker/**: Retrieve a list of all workers.
- **POST /api/worker/**: Create a new worker.
- **GET /api/worker/{id}/**: Retrieve a specific worker by ID.
- **PUT /api/worker/{id}/**: Update an existing worker.
- **DELETE /api/worker/{id}/**: Delete a worker.

### Example Requests

#### Create Worker (POST)
**URL**: `http://127.0.0.1:8000/api/worker/`  
**Method**: POST  
**Request Body**:
```json
{
    "name": "Aravinth",
    "email": "Aravinth@yahoo.com",
    "role": "Support"
}
```

#### Get All Workers (GET)
**URL**: `http://127.0.0.1:8000/api/worker/`  
**Method**: GET  
**Response**:
```json
[
    {
        "id": 1,
        "name": "Aravinth",
        "email": "aravinth@yahoo.com",
        "role": "Support"
    },
    {
        "id": 2,
        "name": "vijay",
        "email": "vijay@gmail.com",
        "role": "lead"
    }
]
```

#### Get Worker by ID (GET)
**URL**: `http://127.0.0.1:8000/api/worker/1/`  
**Method**: GET  
**Response**:
```json
{
    "id": 1,
    "name": "Aravinth",
    "email": "aravinth@yahoo.com",
    "role": "Support"
}
```

#### Update Worker (PUT)
**URL**: `http://127.0.0.1:8000/api/worker/1/`  
**Method**: PUT  
**Request Body**:
```json
{
    "name": "Aravinth",
    "email": "aravinth@yahoo.com",
    "role": "Developer"
}
```

#### Delete Worker (DELETE)
**URL**: `http://127.0.0.1:8000/api/worker/1/`  
**Method**: DELETE  
**Response**:
```json
{
    "message": "Worker deleted successfully"
}
```



### Logging Configuration
The application uses detailed logging for tracking API requests and responses. The logs will be saved to `worker_api.log`. Here’s the logging configuration:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'worker_api.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'worker': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

The verbose formatter will show detailed logs with the level, timestamp, module, and message. Logs will be written both to the console and to a log file (`worker_api.log`).

