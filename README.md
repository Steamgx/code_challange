# Superheroes API

## Description
This project is a Flask-based API for managing superheroes and their powers. It allows users to create, read, update, and delete superhero records, as well as manage their associated powers.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone 
   cd superheroes-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask application:
   ```bash
   python app.py
   ```

2. The API will be running on `http://127.0.0.1:5555`.

## API Endpoints
- **GET /heroes**: Retrieve a list of all heroes.
- **POST /heroes**: Create a new hero.
- **GET /heroes/<id>**: Retrieve a hero by ID.
- **PUT /heroes/<id>**: Update a hero by ID.
- **DELETE /heroes/<id>**: Delete a hero by ID.

## Database Setup
The application uses SQLite for the database. The database file will be created automatically when the application is run for the first time.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.
