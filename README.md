# Take Job Documentation

This documentation provides an overview of the RESTful Flask application project based on the MVC (Model-View-Controller) architecture. The project consists of two main routes: one for extracting job data using bots and another for retrieving data directly from the database. The code follows best practices to ensure better readability and maintainability.

## Project Structure

The project is structured as follows:

- src/
    - async_app/
        - app.py
        - Dockerfile
    - sync_app/
        - bots/
            - takeJobs
        - controllers/
            - jobs_controller.py
        - models/
            - jobs_models.py
        - views/
            - home/
                - index.html
            - table_ws
                - index.html 
        - app.py
    

- The `app` directory contains the source code of the application.
- The `controllers` directory holds the controllers responsible for handling requests and managing the business logic.
- The `models` directory contains the data model definitions and database access operations.
- The `main.py` file serves as the entry point for the application, containing the configuration and route definitions.

## Endpoints

### 1. Home page
= **Endpoint** `/home`
- **HTTP**
- **Response**
  - Sucess: 200 OK
  - Not Found: Failed to load home page

 <img width="667" alt="Captura de Tela 2023-07-18 às 14 30 25" src="https://github.com/felipmateus/takeJobs/assets/76415936/9ea2f6fe-6d00-4424-9dc4-5d861389be89">
   



### 2. Extract Job Data

- **Endpoint**: `/jobs/<search>`
- **Websocket**:
- **Description**: Extracts job data using bots based on the provided search parameter.
- **Response**: 
  - Success: 200 OK
  - Failure: 500 Internal Server Error

<img width="1149" alt="Captura de Tela 2023-07-18 às 14 30 16" src="https://github.com/felipmateus/takeJobs/assets/76415936/bb8b4aef-9459-4099-8c94-1a634d850849">


### 3. Retrieve Job Data

- **Endpoint**: `/jobs/<search>/<page>/<limit>`
- **HTTP Method**: GET
- **Description**: Retrieves job data from the database based on the provided search, page, and limit parameters.
- **Response**: 
  - Success: 200 OK with the job data in JSON format
  - Not Found: 404 Not Found if the job data is not available

![Captura de Tela 2023-07-08 às 19 26 24](https://github.com/felipmateus/takeJobs/assets/76415936/1ba4ecf9-f75c-447d-8a0e-7cc0d6499581)

## Running the Application

To run the application, follow these steps:

1. Ensure that Python and the project dependencies are installed.
2. Execute the following commands in the terminal:

- pip install -r requirements.txt
- python main.py

3. Access the application at `http://localhost:3001`.

## Conclusion

This documentation provides a brief overview of the RESTful Flask application project, focusing on the available endpoints and their functionalities. The project follows the MVC architecture, providing separate components for controllers and models to handle requests and database operations, respectively.

