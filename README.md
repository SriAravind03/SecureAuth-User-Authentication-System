# SecureAuth — User Authentication System

**Simple. Secure. Reliable.**

SecureAuth is a Python-based web application that demonstrates user registration, login, session management, and logout functionality using Flask and SQLite. It provides a foundation for understanding how authentication works in web applications.

## Features

- **User Registration:** Register new users using an email address and password.
- **User Login:** Validate credentials against the user database.
- **Protected Dashboard:** Restrict dashboard access to authenticated users.
- **Session Management:** Maintain login sessions using Flask sessions.
- **Logout:** Clear the current session and return to the home page.
- **SQLite Database:** Store user account information in a local database.
- **Flash Messages:** Display feedback for registration, login, and logout operations.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| Flask | Web application framework |
| SQLite | Database management |
| HTML and CSS | Frontend interface |
| Flask Sessions | Session management |

## Project Structure

```text
SecureAuth/
├── app.py
├── database.py
├── requirements.txt
├── users.db
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
└── README.md
```

*Note: The template filenames above represent the expected structure based on the routes in the application. Include the corresponding HTML files in your project.*

## Prerequisites

- Python 3.10 or later recommended.
- pip package manager.
- A web browser.

## Installation and Setup

### 1. Clone the repository

Replace the example URL with your actual GitHub repository URL.

```bash
git clone https://github.com/YOUR_USERNAME/SecureAuth.git
cd SecureAuth
```

### 2. Create a virtual environment

**Windows — PowerShell:**

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
Flask
```

### 4. Initialize the database

Run the database initialization script:

```bash
python database.py
```

This creates the `users` table in `users.db` if it does not already exist.

### 5. Start the application

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5003

## How to Use

1. Open the application in your browser.
2. Navigate to the registration page.
3. Register using an email address and password.
4. Navigate to the login page.
5. Enter your registered credentials.
6. Access the dashboard after successful authentication.
7. Click logout to end your session.

## Database Design

SecureAuth uses SQLite to manage user accounts.

The `users` table contains the following fields:

| Field | Description |
|---|---|
| `id` | Unique user identifier |
| `email` | User's unique email address |
| `password` | Password field |

The database connection and table initialization logic are implemented in `database.py`.

## Security Considerations

This project is intended as a learning foundation. Before using it in a real application, implement the following improvements:

- **Password hashing:** Store passwords using a suitable password-hashing algorithm such as Werkzeug's password hashing utilities instead of storing plain-text passwords.
- **Strong secret key:** Set a unique, randomly generated `SECRET_KEY` through an environment variable.
- **Disable debug mode:** Turn off Flask debug mode before deployment.
- **CSRF protection:** Protect registration and login forms against cross-site request forgery.
- **Input validation:** Validate and normalize user input appropriately.
- **Session security:** Configure secure session cookie settings and use HTTPS in production.
- **Database protection:** Never commit real user data or sensitive database files to a public repository.

**Important:** The current implementation stores passwords in plain text. Do not use it to store real users' passwords until password hashing and the other necessary security measures have been implemented.

## Learning Objectives

This project helps demonstrate:

- Flask routing and HTTP methods.
- Handling HTML form submissions.
- User registration and authentication.
- SQLite database connections and queries.
- Session-based access control.
- Flash messages and redirects.
- Basic web application security practices.

## Future Enhancements

Possible improvements include:

- Password hashing and password-strength validation.
- Email verification.
- Password reset functionality.
- User profile management.
- Role-based access control.
- Login attempt limits and account lockout.
- Improved responsive UI.
- Automated unit and integration tests.

## License

Choose an appropriate open-source license before distributing the project. Without a license, others do not automatically receive permission to reuse, modify, or redistribute your code.

---

**SecureAuth — User Authentication System**

*A Flask and SQLite project for learning web authentication and session management.*
