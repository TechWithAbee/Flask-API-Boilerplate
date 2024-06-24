# Flask API Boilerplate

This repository provides a boilerplate for creating a Flask API. It includes a structured project layout, configuration management, and various utility functions to get you started quickly.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.7 or higher
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TechWithAbee/Flask-API-Boilerplate.git
   cd Flask-API-Boilerplate
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**

   Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file to include your specific environment variables.

### Running the Application

To run the Flask application, use the provided shell script:

```bash
./run.sh
```

Alternatively, you can run the application using gunicorn:

```bash
gunicorn --logger-class=config.logger.GunicornLogger service.wsgi:app --bind 0.0.0.0:8000 --workers=1
```

## Project Structure

The project structure is organized as follows:

```
├── config
│   ├── logger.py
│   ├── monitoring.py
├── handler
│   ├── user
│       ├── user_routes.py
│       ├── user_service.py
├── helper
│   ├── api_types.py
├── service
│   ├── constants.py
│   ├── wsgi.py
├── .env.example
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
├── run.sh
```

- `config/`: Contains configuration files.
- `handler/`: Contains route handlers, organized by feature.
- `helper/`: Contains utility functions and helpers.
- `service/`: Contains business logic and service classes.
- `.env.example`: Example environment variables file.
- `.gitignore`: List of files and directories to ignore in Git.
- `main.py`: Entry point for the Flask application.
- `requirements.txt`: List of Python dependencies.
- `run.sh`: Shell script to run the application.

## Configuration

The configuration is managed through environment variables. The `.env.example` file provides a template. Copy this file to `.env` and customize it according to your needs.

Example `.env` file:

```
FLASK_ENV=development
DATABASE_URL=sqlite:///example.db
SECRET_KEY=your_secret_key
```

## Usage

- **Routes:** Add your API routes in the appropriate handler modules (e.g., `handler/user/user_routes.py`).
- **Services:** Implement your business logic in service modules (e.g., `handler/user/user_service.py`).

## License

This project is licensed under the MIT License.