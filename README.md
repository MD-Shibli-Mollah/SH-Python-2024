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

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/MD-Shibli-Mollah/SH-Python-2024.git
cd SH-Python-2024

Step by Step Development:
Step 1:
Prerequisites: Install required libraries: pip install Flask pyodbc SQLAlchemy requests pytest

Step 2:
Set up Microsoft SQL Server: Create a database and a banks table with columns for id, name, and location.

Step 3:
1. Flask App with CRUD Operations
1.1 Setting Up Flask with SQLAlchemy : app.py
        pip install flask_sqlalchemy
    