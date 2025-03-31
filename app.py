from flask import Flask
from database import db  # Import the db instance from database.py
from flask_migrate import Migrate
from models import HeroPower  # Ensure this is correctly imported

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'  # Using SQLite for now
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
# db = SQLAlchemy(app)  # Remove the old db initialization
migrate = Migrate(app, db)  # Initialize migrate with app and db

# Import routes (to avoid circular import issues)
from routes import *

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
