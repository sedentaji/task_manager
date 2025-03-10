# Django Task Manager

A task management web application built with Django that allows users to create, update, delete and track tasks.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation Steps

1. **Clone the repository**
  
   git clone https://github.com/sedentaji/task_manager.git
   cd task_manager
 

2. **Create and activate a virtual environment**
  
   # Windows
   python -m venv venv
   venv\Scripts\activate

 
3. **Install dependencies**
 
      pip install django

4. **Apply migrations**

   python manage.py migrate

5. **Create a superuser**
   python manage.py createsuperuser

6. **Run the development server**
   python manage.py runserver

7. **Access the application**
   - Open the browser and navigate to: http://127.0.0.1:8000/
   - Admin interface available at: http://127.0.0.1:8000/admin/

## Usage

- Add new tasks by clicking the "Add Task" button
- View all my tasks on the dashboard
- Click on any task to view details, edit, or delete

## Features

- Create, read, update and delete tasks

## Project Structure

TASK_MANAGER/
├── task_manager/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __pycache__/
│   ├── migrations/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── templates/tasks/
│   │   ├── base.html
│   │   ├── task_confirm_delete.html
│   │   ├── task_detail.html
│   │   ├── task_form.html
│   │   └── task_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── urls.py