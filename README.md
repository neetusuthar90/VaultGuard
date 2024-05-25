# VaultGuard

VaultGuard is a Flask-based web application to managing user account and password.

## Features

- Manage user accounts with features like account locking and password management.
- Generate strong and secure passwords with customizable characteristics.
- Simple and intuitive user interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/neetusuthar90/VaultGuard.git
    ```

2. Navigate to the project directory:

    ```bash
    cd vaultguard
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask application:

    ```bash
    flask run
    ```

7. Access the application in your web browser at `http://localhost:5000`.


## Usage

- Navigate to the homepage (`/`) to login and register.
- Use the navigation bar to access different sections of the application.
- Follow on-screen instructions to perform various actions, such as generating passwords, managing accounts, and logging out.

## Dependencies

- Flask: Web framework for Python
- WTForms: Form validation and rendering library
- Flask-Login: User session management extension for Flask

