# 🚀 Praevia - Automated Task Management Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Django 5.2](https://img.shields.io/badge/Django-5.2-green.svg)](https://docs.djangoproject.com/en/5.2/)
[![Docker](https://img.shields.io/badge/Docker-24.0.5-blue.svg?logo=docker)](https://www.docker.com/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Praevia (Automated Task Management Platform) is a robust and secure Django-based web application designed to streamline task and incident management within an organization. It provides secure two-factor authentication, intuitive role-based access control, and a user-friendly interface for efficient tracking, assignment, and monitoring of tasks and incidents.

![Platform Demo](static/img/praevia-logo.jpg)

---

## 🎯 Table of Contents

* [🌟 Features](#-features)
* [🚀 Getting Started](#-getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Configuration](#configuration)
    * [Running the Application](#running-the-application)
* [💻 Usage](#-usage)
* [📂 Project Structure](#-project-structure)
* [🧪 Running Tests](#-running-tests)
* [🤝 Contributing](#-contributing)
* [📜 License](#-license)
* [📞 Contact](#-contact)
* [🙏 Acknowledgements](#-acknowledgements)

---

## 🌟 Features

Praevia offers a comprehensive set of features to enhance your team's productivity and security:

* **Secure Two-Factor Authentication (2FA):** Implemented using `django-two-factor-auth` to provide an additional layer of security for all user logins.
* **Role-Based Access Control (RBAC):** Define and manage user roles (e.g., Admin, Agent, User) with distinct permissions and access levels.
* **Incident Tracking & Management:** Create, categorize, assign, update, and resolve incidents with a clear workflow.
* **Centralized Dashboard Overview:** A responsive dashboard provides real-time insights into active incidents, assigned tasks, and overall system status.
* **User Management:** Admin users can efficiently create, update, and deactivate user accounts, along with managing their associated roles.
* **Password Reset Functionality:** Secure and standard Django password reset flow is implemented.
* **Responsive Design:** Built with a modern frontend theme (SB Admin 2) ensuring optimal viewing and interaction across various devices.
* **reCAPTCHA Integration:** Protects public-facing forms (like login and registration) against automated bot attacks using Google's reCAPTCHA v2.

---

## 🚀 Getting Started

Follow these instructions to set up and run the praevia application on your local machine for development or via Docker for a production-like environment.

### Prerequisites

Ensure you have the following software installed on your system:

* **Python:** Version 3.12 or newer.
* **pip:** Python package installer (comes with Python).
* **Git:** Version control system.
* **Docker & Docker Compose:** (Required for production setup or Dockerized development).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/isaacaisha/praevia.git](https://github.com/isaacaisha/praevia.git)
    cd praevia_app
    ```

2.  **Set up a Python Virtual Environment (Recommended for Development):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Environment variables are used to manage sensitive data and settings.

1.  **Create `.env` file:** Copy the `.env.example` file to `.env` in your project root (`~/praevia`):
    ```bash
    cp .env.example .env
    ```

2.  **Edit `.env` file:** Open the newly created `.env` file and fill in your specific values.

    ```dotenv
    # Required Django Secret Key (generate a strong, random one)
    SECRET_KEY=your_super_secret_key_here_for_security

    # Set to False for production environments for security
    DEBUG=True 

    # Allowed hosts for your Django application (e.g., localhost, your_domain.com, your_server_ip)
    ALLOWED_HOSTS=localhost,127.0.0.1

    # Database Settings (PostgreSQL is recommended and used in Docker)
    DB_NAME=praevia_db
    DB_USER=praevia_user
    DB_PASSWORD=praevia_password
    DB_HOST=localhost # 'db' if using docker-compose for development, 'localhost' for local dev without docker db
    DB_PORT=5432

    # Google reCAPTCHA Keys (Obtain from [https://www.google.com/recaptcha/admin/](https://www.google.com/recaptcha/admin/))
    RECAPTCHA_PUBLIC_KEY=your_recaptcha_site_key_goes_here
    RECAPTCHA_PRIVATE_KEY=your_recaptcha_secret_key_goes_here

    # Email Settings (for password reset, 2FA setup, etc.)
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.your-email-provider.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_email_password
    DEFAULT_FROM_EMAIL=your_email@example.com
    ```
    **Security Note:** Never commit your actual `.env` file to version control. It contains sensitive credentials.

3.  **Run Database Migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a Superuser (Admin Account):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your administrative user account.

### Running the Application

#### Development (using Django's built-in server)

To quickly get the application running for development:

```bash
python manage.py runserver 0.0.0.0:8079
```
