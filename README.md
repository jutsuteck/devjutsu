<div align="center">

# Devjutsu - Security Meets Software Engineering

•
[Summary](#summary)
•
[Features](#features)
•
[Setup Instructions](#setup instructions)
•
[Screenshot](#screenshots)
•
[Roadmap](/ROADMAP.md)
•
[Changelog](/CHANGELOG.md)

## Summary

</div>

Devjutsu: An agile project management tool streamlining secure software development for all developers. Craft user stories, integrate security requirements, and produce secure code seamlessly.

![Docker Build and Push](https://github.com/jutsuteck/devjutsu/actions/workflows/docker-build-push.yml/badge.svg)
![Docker Security](https://github.com/jutsuteck/devjutsu/actions/workflows/docker-trivy-scan.yml/badge.svg)

## Features

**Security Requirements Mapping (In Development)**: Devjutsu stands out in the realm of project management tools with its pioneering feature of "Security Requirements Mapping". This unique capability empowers developers to seamlessly integrate security considerations directly into their software engineering workflow. By analyzing individual user stories, Devjutsu associates them with relevant security controls, ensuring that each development task incorporates the essential security measures. As we continue to refine this feature, users can look forward to a more intuitive and efficient way to embed security into every facet of their projects. Stay tuned for more general project management features that will complement this core functionality.

## Setup Instructions

### **Prerequisites**

Before you begin, ensure you have the following installed:

- **Docker**: Devjutsu uses Docker containers for its services. If you don't have Docker installed, you can get it from [Docker's official website](https://www.docker.com/get-started).
- **Node.js**: The frontend requires Node.js. If it's not installed, download and install it from [Node.js official website](https://nodejs.org/).

### **Getting Started**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jutsuteck/devjutsu.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd devjutsu
   ```

3. **Build and Run Docker Containers**:
   From the root directory, execute the following command to build and run all necessary containers, including databases and services:

   ```bash
   docker-compose build up
   ```

4. **Run the Frontend**:
   Navigate to the `jutsu-ui` directory and start the frontend development server:
   ```bash
   cd jutsu-ui
   yarn dev
   ```

Once you've followed these steps, Devjutsu should be up and running on your local machine!

## Screenshots

**ASVS Controls**
![Asvs](./docs/asvs-checklist.png)

**Creating a new project**
![create project](./docs/create-project.png)

**Project Board (In Development)**
![project board](./docs/project-board.png)
