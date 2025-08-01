# Coplur-Assessment
Built a Flask web app with MySQL that lets students register and admins manage users. It has login, logout, password hashing, and role-based access. Admins can add/delete users, students get a welcome page. Clean UI, secure backend, and fully working auth system.

# Role-Based User Management Web App
Hey there! This is a simple and functional web app built using **Flask (Python)** and **MySQL**. It supports user login, registration, role-based access control, and a full admin dashboard to manage users.  

## What This App Does
-  Login & logout functionality  
-  Students can register themselves  
-  Admin is created automatically when the app starts  
-  Admin can view all users, create new users, and delete existing ones  
-  Role-based access — only admins can do admin things  
-  Unauthorized access? Boom! Blocked with a 403 Forbidden  

## Roles
- **Student:** Can register and see a welcome page  
- **Admin:** Has full control over users (like a boss)

## Tech Stack
- **Backend:** Flask + SQLAlchemy  
- **Database:** MySQL  
- **Frontend:** Jinja2 templating (HTML)  
- **Security:** Flask-Login, Flask-Bcrypt for hashed passwords
  
## How to Run
1. Clone this repo  
2. Set up a virtual environment  
   `python3 -m venv env && source env/bin/activate`  
3. Install dependencies  
   `pip install -r requirements.txt`  
4. Make sure MySQL is running, and update DB credentials in `app.py`  
5. Create the database manually in MySQL or run the SQL file if provided  
6. Start the app  
   `python app.py`  
7. Open browser and go to `http://localhost:5000`
   
## Default Admin Credentials
- **Username:** `admin`  
- **Password:** `admin123`  
*(You can change this in the code after the first login)*

## Features in Action
- Role selection before login  
- Dynamic dashboard based on role  
- Smooth routing and session handling  
- Handles duplicate users, bad logins, and blocked pages
  
##  Team Credits
Big shoutout to the amazing team who made this project possible:
-  **Shivani** — Our sharp and steady **Team Leader**, who made sure we stayed on track even when the code got chaotic.  
-  **Preety** — Always ready with ideas and testing every edge case like a pro.  
-  **Ariba** — Quietly awesome, handled tasks and bugs like a champ.  

This project was a team effort, and each one of us added our own spark to it 

## Note
This project is for learning/demo purposes. Not production-ready. But hey, it works like a charm for a portfolio or interview project ✨

## Want to Contribute?
Fork, clone, or open an issue if you find bugs — or if you just wanna say hi.

Made by Nikita and team.  
