# CRUD Application with Flask and SQL Server

This project is a basic CRUD application using Flask and Microsoft SQL Server to manage a database of banks. The application supports creating, reading, updating, and deleting (CRUD) bank records. 

## Features
- Add a new bank record (Create)
- List all bank records (Read)
- Retrieve details of a specific bank (Read)
- Update an existing bank record (Update)
- Delete a bank record (Delete)

## Technologies Used
- Python (Flask, SQLAlchemy)
- Microsoft SQL Server
- PyODBC

## Prerequisites
- Python 3.7 or higher
- Microsoft SQL Server
- `pyodbc` and `SQLAlchemy` libraries
- `Flask` for building the web application
- Install required libraries:
    pip install Flask pyodbc SQLAlchemy requests pytest flask_sqlalchemy

- Set up Microsoft SQL Server: Create a database
    database: `msshibli`
    If the `table` is not created in the `database` then our code will automatically create it as `banks(dbo.banks)`

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/MD-Shibli-Mollah/SH-Python-2024.git
cd SH-Python-2024

run app.py
Dibugger is enabled & the server will be Running on http://127.0.0.1:5000

## Testing APIs for the API Endpoints:

| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| POST   | /banks         | Create a new bank record  |
| GET    | /banks         | Get a list of all banks   |
| GET    | /banks/<id>    | Get a specific bank by ID |
| PUT    | /banks/<id>    | Update a specific bank    |
| DELETE | /banks/<id>    | Delete a specific bank    |
