# Locust Project

Welcome to my Locust project! As a QA Engineer, I am researching and developing (RND) Locust to explore its capabilities for load and performance testing. This project serves as my playground for experimenting with Locust, learning its features, and applying them to real-world testing scenarios.

## Overview

Locust is an open-source load testing tool that allows you to define user behavior with Python code. In this project, you'll find a simple Locust test configuration that simulates basic user interactions.

## Project Structure

locust-project/ ├── Dockerfile ├── docker-compose.yml ├── locustfile.py └── README.md

markdown
Copy
Edit

- **Dockerfile:** Defines the container environment for running Locust.
- **docker-compose.yml:** Simplifies running Locust in a Docker container.
- **locustfile.py:** Contains the Locust test code with sample user behavior.
- **README.md:** Project documentation.

## How to Run the Project

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rabiul-Hasan-work/locust-project.git
   cd locust-project
Build and run the project using Docker Compose:

bash
Copy
Edit
docker-compose up --build
Access the Locust web UI:

Open your browser and navigate to http://localhost:8089.

Start testing:

Use the web interface to configure and start your load tests. Monitor the performance metrics as Locust simulates user behavior.

Customizing Your Tests
Edit locustfile.py:
Modify or add tasks to simulate more complex user interactions.
Environment Variables:
You can customize the target host and other settings using environment variables in the docker-compose.yml.
Contributing
Feel free to fork this repository and contribute with improvements, fixes, or additional test scenarios. Any suggestions to enhance this project are welcome!

License
This project is open source and available under the MIT License.
