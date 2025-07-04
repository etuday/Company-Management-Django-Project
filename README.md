# Company Management System 🏢

A full-stack Django web application to manage company profiles with logo uploads, CRUD operations, and responsive design.

## 🔧 Features

- ✅ Add, update, and delete company records
- 📂 Upload and display company logos
- 🔍 Search and paginate company list
- 🔐 Secure login/logout with session handling
- 🎨 Responsive UI using Bootstrap 5
- ☁️ Live deployment via Render

## 🌐 Live Demo

🔗 [https://company-management-django-project1.onrender.com](https://company-management-django-project1.onrender.com)

## 🛠 Tech Stack

- Python 3.10
- Django 5.2.1
- Bootstrap 5
- MySQL (or SQLite)
- Render for hosting

## ⚙️ Setup Instructions

```bash
git clone https://github.com/etuday/Company-Management-Django-Project.git
cd Company-Management-Django-Project
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
