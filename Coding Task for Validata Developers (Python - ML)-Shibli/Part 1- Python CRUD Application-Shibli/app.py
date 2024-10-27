from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure Database Connection
# Sets up the database URI with Windows Authentication for SQL Server using the specified driver.
# Database name: msshibli
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@localhost/msshibli?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"connect_args": {"fast_executemany": True}}

# Initialize SQLAlchemy to manage database operations
db = SQLAlchemy(app)

# Define a model for the 'Banks' table with columns 'id', 'name', and 'location'
class Banks(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key field for unique identification
    name = db.Column(db.String(50), nullable=False)  # Name of the bank, required
    location = db.Column(db.String(50), nullable=False)  # Location of the bank, required

# Endpoint to create a new bank record in the database
# Expects JSON input with 'name' and 'location' fields
@app.route('/banks', methods=['POST'])
def create_bank():
    data = request.get_json()
    if 'name' not in data or 'location' not in data:  # Validates presence of required fields
        return jsonify({"error": "Missing required fields: 'name' and 'location'"}), 400
    new_bank = Banks(name=data['name'], location=data['location'])
    db.session.add(new_bank)  # Add new bank record to session
    db.session.commit()  # Commit session to save changes
    return jsonify({"message": "Bank created successfully"}), 201

# Endpoint to retrieve all bank records in the database
@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Banks.query.all()  # Fetches all bank records
    # Converts bank objects to JSON format
    return jsonify([{"id": bank.id, "name": bank.name, "location": bank.location} for bank in banks])

# Endpoint to retrieve a specific bank record by ID
@app.route('/banks/<int:id>', methods=['GET'])
def get_bank(id):
    bank = Banks.query.get(id)  # Fetches bank record by ID
    if bank:
        # Returns bank data in JSON format if found
        return jsonify({"id": bank.id, "name": bank.name, "location": bank.location})
    return jsonify({"error": "Bank not found"}), 404  # Error message if bank is not found

# Endpoint to update an existing bank record by ID
# Expects JSON input with optional 'name' and 'location' fields
@app.route('/banks/<int:id>', methods=['PUT'])
def update_bank(id):
    data = request.get_json()
    bank = Banks.query.get(id)  # Fetches bank record by ID
    if bank:
        # Updates fields if new data is provided
        bank.name = data.get('name', bank.name)
        bank.location = data.get('location', bank.location)
        db.session.commit()  # Save changes to the database
        return jsonify({"message": "Bank updated successfully"})
    return jsonify({"error": "Bank not found"}), 404  # Error message if bank is not found

# Endpoint to delete a bank record by ID
@app.route('/banks/<int:id>', methods=['DELETE'])
def delete_bank(id):
    bank = Banks.query.get(id)  # Fetches bank record by ID
    if bank:
        db.session.delete(bank)  # Delete record from the session
        db.session.commit()  # Commit session to apply deletion
        return jsonify({"message": "Bank deleted successfully"})
    return jsonify({"error": "Bank not found"}), 404  # Error message if bank is not found

# Main function to start the application
if __name__ == '__main__':
    with app.app_context():
        try:
            # Initialize the database by creating tables if they don't exist
            db.create_all()
        except Exception as e:
            print(f"Error initializing database: {e}")
    # Run the Flask application with debugging enabled
    app.run(debug=True)