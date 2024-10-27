# Coding Task for Validata Developers (Python)
# PART 2: CRUD Application with Flask and SQL Server

This project is a basic CRUD application using Flask and Microsoft SQL Server to manage a database of banks. The application supports creating, reading, updating, and deleting (CRUD) bank records. 

## Features
- Add a new bank record (Create)
- List of all bank records (Read)
- Retrieve the details of a specific bank (Read)
- Update an existing bank record (Update)
- Delete a bank record (Delete)

## Technologies Used
- Python: Core programming language.
- Flask: Web framework for building the application.
- SQLAlchemy: ORM (Object Relational Mapper) for database interaction.
- Microsoft SQL Server: Database server.
- PyODBC: Database driver for SQL Server.

## Prerequisites
- Python 3.7 or higher
- Microsoft SQL Server: `ODBC Driver 17 for SQL Server`
- Required Python libraries:
- `pyodbc` and `SQLAlchemy` libraries
- `Flask` for building the web application
- Install required libraries:
```bash
   pip install Flask SQLAlchemy pyodbc requests pytest flask_sqlalchemy
```
- Set up Microsoft SQL Server: Create a database named `msshibli`

The application will automatically create a `banks` table in the database if it does not exist.

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/MD-Shibli-Mollah/SH-Python-2024.git
cd SH-Python-2024/Coding_Task-for-Validata_Devs-(Python)-Shibli/Part_2-Python_CRUD_Application-Shibli
```

### Step 2: Configure Database Connection
Ensure your SQL Server is accessible and your connection string in `app.py` is correctly configured for your environment.
### Step 3: Run the Application
```bash
python app.py
```
The application will run on http://127.0.0.1:5000

### Step 3: Test the API Endpoints:
Use tools like `Postman` or `curl` to test the following endpoints:
| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| `POST`   | `/banks`         | Create a new bank record  |
| `GET`    | `/banks`        | Get a list of all banks   |
| `GET`    | `/banks/<id>`    | Get a specific bank by ID |
| `PUT`    | `/banks/<id>`    | Update a specific bank    |
| `DELETE` | `/banks/<id>`    | Delete a specific bank    |

### Running Tests
This project includes a `test_app.py` file to verify the functionality of the CRUD operations. The test suite checks that the API endpoints for creating, reading, updating, and deleting bank records work correctly.

#### Step 1: Install `pytest`
If not already installed, install `pytest` to run the test file:
```bash
pip install pytest
```
#### Step 2: Run the Tests
```bash
pytest test_app.py
```
This will run all the tests defined in `test_app.py` and provide feedback on the application's functionality. Ensure that the application server is running when you execute the tests.

## Notes
Debug mode is enabled in the app, which provides detailed error information and auto-reloads on code changes. This can be useful during development.
Ensure your SQL Server has necessary permissions set for `Windows Authentication`.