from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure Database Connection
# Use Windows Authentication to connect to SQL Server (username:password isn't required)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://username:password@server/database?driver=SQL+Server'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@NITSL-NB-07/msshibli?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"connect_args": {"fast_executemany": True}}

db = SQLAlchemy(app)

class Banks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)


# This endpoint creates a new bank record in the database. It expects a JSON payload with name and location.
@app.route('/banks', methods=['POST'])
# Create a Bank Entry
def create_bank():
    data = request.get_json()
    if 'name' not in data or 'location' not in data:
        return jsonify({"error": "Missing required fields: 'name' and 'location'"}), 400
    new_bank = Banks(name=data['name'], location=data['location'])
    db.session.add(new_bank)
    db.session.commit()
    return jsonify({"message": "Bank created successfully"}), 201

# This endpoint returns a list of all banks with their id, name, and location.
@app.route('/banks', methods=['GET'])
# Read All Banks:
def get_banks():
    banks = Banks.query.all()
    return jsonify([{"id": bank.id, "name": bank.name, "location": bank.location} for bank in banks])

# This endpoint retrieves a bank by its id.
@app.route('/banks/<int:id>', methods=['GET'])
# Read a Specific Bank by ID:
def get_bank(id):
    bank = Banks.query.get(id)
    if bank:
        return jsonify({"id": bank.id, "name": bank.name, "location": bank.location})
    return jsonify({"error": "Bank not found"}), 404

# Update a Bank Entry:
@app.route('/banks/<int:id>', methods=['PUT'])
def update_bank(id):
    data = request.get_json()
    bank = Banks.query.get(id)
    if bank:
        bank.name = data.get('name', bank.name)
        bank.location = data.get('location', bank.location)
        db.session.commit()
        return jsonify({"message": "Bank updated successfully"})
    return jsonify({"error": "Bank not found"}), 404

# Delete a Bank Entry:
@app.route('/banks/<int:id>', methods=['DELETE'])
def delete_bank(id):
    bank = Banks.query.get(id)
    if bank:
        db.session.delete(bank)
        db.session.commit()
        return jsonify({"message": "Bank deleted successfully"})
    return jsonify({"error": "Bank not found"}), 404

# Main App
if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()  # This creates tables if they don't exist
        except Exception as e:
            print(f"Error initializing database: {e}")
    # app.run(debug=True)
    app.run(debug=True)


