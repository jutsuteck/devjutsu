# Changelog

All notable changes to the "jutsu" project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Dockerfile and docker directories: Dockerfiles and related directories previously residing within individual services have been removed and centralized in the root directory of the project. The Python, PostgreSQL, and Redis Dockerfiles now act as base images for potential future Docker images. This restructuring facilitates easier management of Docker images and better supports the possibility of scaling and expanding the application in the future.

### Added

- Introduced the `rbac_manager` in the auth service to handle role-based access control logic.

- Added a `seed_database.py` script to seed the database with default roles and permissions.

- Integrated the seeding script into the `startup.sh` to ensure the database is seeded upon service startup.

- Refactored the seeding process in the auth service to streamline the initialization of roles and permissions.

- Docker Security Scan Actions workflow: Introduced a new CI/CD workflow that automatically scans for security vulnerabilities using Trivy. This automation will enhance the project's development and security processes.

- Docker Build and Push GitHub Actions workflow: Introduced a new CI/CD workflow that automatically builds and pushes the Python Docker image to Docker Hub. This automation will enhance the project's development and deployment processes.

- Settings Configuration: Refactored the settings configuration in the project to improve the structure and ease of use. The settings are now divided into several separate classes including `Base`, `PostgresSettings`, `RedisSettings`, `JWTSettings`, and `GithubSettings`. This division allows for better organization and individual handling of various settings based on their respective services.

- Environment Variables in Docker: Adjusted the Python Dockerfile to support dynamic assignment of the environment variable `ENVIRONMENT`. This allows the container to determine if it is running in a development or production environment. The `ENVIRONMENT` variable is also used in the refactored settings configuration to load appropriate values.

- Project: Introduced Docker files for Python and PostgreSQL containers and ensured they can be built and run using docker-compose.

- Project Service: Defined all the models related to project management which includes Project, Epic, Workflow, WorkItem, Task, Label, ASVSSecurityRequirement, ASVSSecurityCategory, and ASVSSecuritySubCategory. Introduced the repository design pattern to separate business logic and database operations, and to facilitate easier testing.

- Auth Service: Started developing the auth service using the FastAPI users library for user management. This includes OAuth accounts and general authentication/authorization. This service uses three Docker containers - a Python container, a PostgreSQL container, and a Redis container for token management. Began experimenting with Alembic for database migrations.

- Auth Service Models: Defined the following models: OAuthAccount, Member, Tenant, Team, Role, and Permission.

## [0.0.1] - 2023-07-23

- Initial project setup and repository creation. The basic architecture for the microservices (auth-service and project-service) and frontend (jutsu-ui) have been setup.

## Project started on 2023-07-09
