# URL Shortener

A simple URL shortener built with FastAPI, SQLAlchemy, and Docker. This application provides API endpoints to shorten URLs and redirect to the original URLs using a short code.

---

## Features:
- Shorten long URLs into short codes.
- Redirect to the original URL using the short code.
- Dockerized for easy deployment.
- SQLite and MariaDB support for testing and production environments.

---

## Prerequisites

- Python 3.10 or higher.
- Docker and Docker Compose installed.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Rishikesh0523/url_shortener.git
cd url_shortener
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add the following variables:
```env
project_name=URL Shortener
database_url=mysql+pymysql://root:{password}@db:3306/url_shortener
test_database_url=sqlite:///./test.db
secret_key=supersecretkey
```

---

## Usage

### 1. Run Locally
Start the application locally without Docker:
```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

---

### 2. Run with Docker
#### a. Build and Start Containers
```bash
docker-compose up --build
```

#### b. Access the Application
Visit `http://localhost:8000/docs` in your browser.

---

## API Endpoints

### 1. POST `/shorten`
Shorten a URL.
- **Request Body**:
```json
{
    "original_url": "https://example.com"
}
```
- **Response**:
```json
{
    "id": 1,
    "original_url": "https://example.com",
    "short_code": "abc123"
}
```

### 2. GET `/{short_code}`
Redirect to the original URL.
- **Response**: Redirects to the original URL.

---

## Running Tests
Run the tests using `pytest`:
```bash
$env:TESTING="TRUE"  # For PowerShell
pytest
```

---

## Folder Structure
```
URL_SHORTENER/
├── .pytest_cache/
├── app/
│   ├── __pycache__/
│   ├── api/
│   │   ├── __pycache__/
│   │   └── routes.py
│   ├── core/
│   │   ├── __pycache__/
│   │   └── config.py
│   ├── db/
│   │   ├── __pycache__/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   └── __init__.py
│   └── main.py
├── tests/
│   ├── __pycache__/
│   └── test_main.py
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Contributing
Feel free to fork the repository and submit a pull request. Contributions are always welcome!

---

## License
This project is licensed under the MIT License.