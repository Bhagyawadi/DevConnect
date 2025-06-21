# 💼 DevConnect – A Professional Developer Portfolio Platform

DevConnect is a full-stack Django web application designed to showcase developer profiles, blog articles, and a collaborative Q&A forum — all in one platform. Built with Django, Bootstrap 5, and SQLite, it's perfect for personal portfolios, team knowledge sharing, or as a resume project.

---

## 🚀 Features

- ✅ Custom user authentication (sign up, login, logout)
- ✅ Developer profiles with bio, avatar, skills, GitHub & LinkedIn
- ✅ Edit profile with image upload
- ✅ Article posting with titles, slugs, and full content
- ✅ Q&A Forum (post questions, upvote/downvote, answer others)
- ✅ User Dashboard (view your posts & questions)
- ✅ Search and pagination for articles and questions
- ✅ Bootstrap 5 responsive UI

---

## 🧱 Built With

- **Backend**: Django 5
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Authentication**: Django’s custom user model
- **Hosting**: (You can add Render/Vercel/Heroku when deployed)

---

## 📸 Screenshots

![Home](screenshots/home.png)  
![Profile](screenshots/profile.png)  
![Dashboard](screenshots/dashboard.png)  
*(Add actual screenshot images in a `/screenshots/` folder in your repo.)*

---

## 📂 Folder Structure

```bash
DevConnect/
├── accounts/       # User auth & profiles
├── articles/       # Blog app
├── forum/          # Q&A forum
├── templates/      # Shared HTML templates
├── static/         # Bootstrap/static files
├── media/          # Uploaded avatars
├── core/           # Project settings
└── manage.py
