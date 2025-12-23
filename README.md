# 🎬 CineScope – Movie Rating & Review Backend Platform

CineScope is a Django-based backend web application that allows users to register,
authenticate, and interact with a movie rating and review system.  
The project focuses on **backend business logic, database design, and scalable
application structure**, making it suitable for Software Development Engineer
(SDE) roles.

---

## 📌 Problem Statement

Most movie review platforms require structured handling of user data, ratings,
and reviews while ensuring authentication, data integrity, and performance.
CineScope addresses this by providing a backend-driven system that manages
movie-related interactions using a relational database.

---

## 🧠 Key Backend Features

- User authentication and authorization
- Backend logic for movie ratings and reviews
- CRUD operations for movies, reviews, and comments
- Relational database integration using Django ORM
- Role-based access to application features
- Clean separation of business logic and data models

---

## 🏗️ Architecture

The application follows the **MVC (Model–View–Controller) architecture** using Django:

- **Models**  
  Define database schema for users, movies, ratings, and reviews

- **Views**  
  Handle backend business logic and request processing

- **URLs**  
  Route requests to appropriate backend views

- **Templates**  
  Provide a simple frontend interface for interaction

This structure ensures maintainability and scalability of the application.

---

## 📂 Project Structure

CineScope/
├── app/
│ ├── models.py # Database models
│ ├── views.py # Backend business logic
│ ├── urls.py # URL routing
│ └── templates/ # HTML templates
├── static/ # Static files (CSS, Bootstrap)
├── manage.py # Django entry point
├── requirements.txt
└── README.md


---

## 🛠️ Tech Stack

- **Language:** Python  
- **Backend Framework:** Django  
- **Database:** MySQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **ORM:** Django ORM  
- **Tools:** Git, GitHub  

---

## ▶️ How to Run Locally

1. Clone the repository  
   ```bash
   git clone <repository-link>
   cd CineScope
2. Install dependencies
  pip install -r requirements.txt

3. Configure database settings in settings.py

4.Apply migrations
   python manage.py migrate

5.Start the server
  python manage.py runserver

6.Open in browser
  http://127.0.0.1:8000/
