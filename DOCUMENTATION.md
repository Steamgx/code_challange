# Superheroes API Documentation

## Introduction
The Superheroes API is a RESTful API built with Flask that allows users to manage superheroes and their associated powers. This API supports CRUD operations for superhero records and their powers.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Steamgx/code_challange.git
   cd superheroes-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Start the Flask application:**
   ```bash
   python app.py
   ```

2. **Access the API:**
   The API will be running on `http://127.0.0.1:5555` or `http://127.0.0.1:5000` when using flask run
## API Documentation
### Endpoints
- **GET /heroes**
  - Description: Retrieve a list of all heroes.
  - Response: JSON array of hero objects.

- **POST /heroes**
  - Description: Create a new hero.
  - Request Body: JSON object with hero details (name, super_name).
  - Response: JSON object of the created hero.

- **GET /heroes/<id>**
  - Description: Retrieve a hero by ID.
  - Response: JSON object of the hero.

- **PUT /heroes/<id>**
  - Description: Update a hero by ID.
  - Request Body: JSON object with updated hero details.
  - Response: JSON object of the updated hero.

- **DELETE /heroes/<id>**
  - Description: Delete a hero by ID.
  - Response: Confirmation message.

## Database Schema
The application uses SQLite for the database. The following tables are created:

- **heroes**
  - id: Integer (Primary Key)
  - name: String (Not Null)
  - super_name: String (Not Null)

- **powers**
  - id: Integer (Primary Key)
  - name: String (Not Null)
  - description: String (Not Null)

- **hero_powers**
  - id: Integer (Primary Key)
  - strength: String (Not Null)
  - hero_id: Integer (Foreign Key referencing heroes.id)
  - power_id: Integer (Foreign Key referencing powers.id)

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.
