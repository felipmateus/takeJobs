# RESTful Flask Application Project Documentation

This documentation provides an overview of the RESTful Flask application project based on the MVC (Model-View-Controller) architecture. The project consists of two main routes: one for extracting job data using bots and another for retrieving data directly from the database. The code follows best practices to ensure better readability and maintainability.

## Project Structure

The project is structured as follows:

- app/
    - controllers/
        - jobs_controller.py
    - models/
        - jobs_model.py
    - main.py

- The `app` directory contains the source code of the application.
- The `controllers` directory holds the controllers responsible for handling requests and managing the business logic.
- The `models` directory contains the data model definitions and database access operations.
- The `main.py` file serves as the entry point for the application, containing the configuration and route definitions.

## Endpoints

### 1. Extract Job Data

- **Endpoint**: `/jobs/<search>`
- **HTTP Method**: GET
- **Description**: Extracts job data using bots based on the provided search parameter.
- **Response**: 
  - Success: 200 OK
  - Failure: 500 Internal Server Error

### 2. Retrieve Job Data

- **Endpoint**: `/jobs/<search>/<page>/<limit>`
- **HTTP Method**: GET
- **Description**: Retrieves job data from the database based on the provided search, page, and limit parameters.
- **Response**: 
  - Success: 200 OK with the job data in JSON format
  - Not Found: 404 Not Found if the job data is not available

Please refer to the code and comments in the project files for more details about the implementation.

## Running the Application

To run the application, follow these steps:

1. Ensure that Python and the project dependencies are installed.
2. Execute the following commands in the terminal:

- pip install -r requirements.txt
- python main.py

3. Access the application at `http://localhost:5000`.

## Conclusion

This documentation provides a brief overview of the RESTful Flask application project, focusing on the available endpoints and their functionalities. The project follows the MVC architecture, providing separate components for controllers and models to handle requests and database operations, respectively.

