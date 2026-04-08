# 🛒 Django E-Commerce Store

A full-featured e-commerce web application built with **Django 5.2** and **Bootstrap 5**. Browse products, manage your shopping cart, and checkout — all with a clean, responsive UI.

## ✨ Features

- **Product Catalog** — Browse all available products with images and descriptions
- **Shopping Cart** — Add/remove items with real-time quantity updates (AJAX)
- **Checkout** — Complete your order with a streamlined checkout flow
- **User Authentication** — Register, login, and logout with Django's built-in auth
- **Admin Panel** — Manage products and orders via Django admin
- **Responsive Design** — Looks great on desktop and mobile (Bootstrap 5 + Crispy Forms)

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Backend language |
| Django 5.2 | Web framework |
| SQLite | Database |
| Bootstrap 5 | Frontend styling |
| Crispy Forms | Beautiful form rendering |
| Pillow | Image handling |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/django-ecommerce.git
   cd django-ecommerce
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   - Store: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📁 Project Structure

```
ecommerce/
├── accounts/          # User authentication app
├── config/            # Django project settings
├── static/            # CSS, JS, and images
├── store/             # Main store app (models, views, urls)
├── templates/         # HTML templates
├── manage.py
└── requirements.txt
```

## 📸 Screenshots

_Coming soon!_

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
