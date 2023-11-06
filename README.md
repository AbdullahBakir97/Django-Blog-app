
# Django Blog App

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2%2B-brightgreen)](https://www.djangoproject.com/)

A feature-rich Django Blog app for managing and publishing articles.
## LinkedIn post : 
   https://www.linkedin.com/posts/abdullah-bakir-809065273_github-abdullahbakir97django-blog-app-activity-7114489198937559040-4YI9?utm_source=share&utm_medium=member_ios

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and registration.
- Create, edit, and delete blog posts.
- Categorize blog posts.
- Comment on blog posts.
- User-friendly admin panel.
- Responsive design for all devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AbdullahBakir97/Django-Blog-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django-Blog-app
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the admin panel at http://localhost:8000/admin/ to start managing your blog.

## Usage

- Visit the homepage to view and interact with blog posts.
- Log in or register to create your own blog posts and leave comments.
- Use the admin panel to manage users, blog posts, and categories.

## Configuration

- You can customize the app settings in the `settings.py` file.
- For production deployment, make sure to configure a secure Django `SECRET_KEY`, database, and set `DEBUG` to `False`.

## Contributing

Contributions are welcome! Please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
