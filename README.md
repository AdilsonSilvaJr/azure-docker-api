# Python API Project

Welcome to the Python API project! This project is a simple Flask application structured to provide a RESTful API. Below are the details regarding the project setup, usage, and structure.

## Project Structure

```
python-api-project
├── src
│   ├── app.py                # Entry point of the application
│   ├── controllers           # Contains business logic
│   │   └── __init__.py
│   ├── models                # Defines data models or schemas
│   │   └── __init__.py
│   ├── routes                # Defines API routes
│   │   └── __init__.py
│   └── tests                 # Contains unit tests
│       ├── __init__.py
│       └── test_app.py
├── .github
│   └── workflows
│       └── build.yml         # GitHub Actions workflow for CI/CD
├── Dockerfile                 # Dockerfile for building the application image
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Docker

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-api-project
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application locally, execute the following command:
```
python src/app.py
```

### Running Tests

To run the unit tests, use:
```
pytest src/tests
```

### Docker

To build the Docker image, run:
```
docker build -t python-api-project .
```

To run the Docker container, use:
```
docker run -p 5000:5000 python-api-project
```

### CI/CD with GitHub Actions

This project includes a GitHub Actions workflow defined in `.github/workflows/build.yml` that automates the process of building the Docker image and pushing it to Azure Container Registry.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.