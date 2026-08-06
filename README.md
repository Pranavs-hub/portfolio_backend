# 🌐 Django Portfolio Website

A modern and responsive **Personal Portfolio Website** developed using **Django**, **HTML**, **CSS**, and **JavaScript**. This project showcases my technical skills, projects, education, and contact information. It also includes a fully functional contact form that stores visitor messages in a SQLite database using the Django backend.

---

# 📸 Project Preview

## 🏠 Home

![Home](screenshots/home.png)

---

## 👨‍💻 About

![About](screenshots/about.png)

---

## 💡 Skills

![Skills](screenshots/skills.png)

---

## 🚀 Projects

![Projects](screenshots/projects.png)

---

## 📞 Contact

![Contact](screenshots/contact.png)

---

# ✨ Features

- Responsive Design
- Attractive User Interface
- Smooth Navigation
- Home, About, Skills, Projects & Contact Sections
- Contact Form with Django Backend
- SQLite Database Integration
- Django Admin Panel
- Resume Download Option
- Social Media Links
- Static File Management
- Mobile Friendly Design

---

# 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Django

### Database

- SQLite3

### Tools & Technologies

- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
portfolio_backend/
│
├── manage.py
├── db.sqlite3
│
├── portfolio/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── pdf/
│   ├── templates/
│   │   └── index.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── portfolio_backend/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

# 📋 Contact Form

The contact form allows visitors to:

- Enter their Name
- Email Address
- Phone Number
- Message

All submitted information is securely stored in the SQLite database and can be managed through the Django Admin Panel.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/portfolio.git
```

Move into the project folder

```bash
cd portfolio_backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install django
```

Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

Open in your browser:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

# 📈 Future Improvements

- Email Notifications
- Google reCAPTCHA
- Dark Mode
- Blog Section
- Project Filtering
- REST API Integration
- Deployment on Render or PythonAnywhere

---

# 👨‍💻 Author

**Pranav Rajagouda Patil**

Python Full Stack Developer

📧 Email: pranavrgpatil@gmail.com

🌐 GitHub: https://github.com/Pranavs-hub

💼 LinkedIn: https://www.linkedin.com/in/pranav-patil
---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub. Your support helps motivate further improvements and future open-source projects.

---

# 📄 License

This project is licensed under the MIT License.