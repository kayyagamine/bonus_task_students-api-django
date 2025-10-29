🎓 Django Students API

A simple Django REST Framework project to manage student data.
Includes a bonus endpoint to filter adult students.

✅ Features

Create, view, and manage students

RESTful API built using Django REST Framework

Filter students aged above 18 using /api/students/adults/

🔗 API Endpoints
Method	Endpoint	Description
GET	/api/students/	List all students
POST	/api/students/	Create a student
GET	/api/students/adults/	List students aged > 18
🛠️ Tech Stack

Python

Django

Django REST Framework

🚀 Setup Instructions
# Clone repository
git clone https://github.com/kayyagamine/bonus_task_students-api-django.git
cd bonus_task_students-api-django

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver

📎 Bonus Task

Implemented an API endpoint to return all students aged > 18 using a custom view and URL path.

👨‍💻 Author

Kay Yagamine
Student at BMSCE
Django + REST API Beginner Project 🔥
