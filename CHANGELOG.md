# Changelog

All notable changes to the "jutsu" project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [Unreleased]

### Added

- Implemented project list page.
- Added functionality for creating a new project.
- Introduced a template for the board page that renders the workflow, states, and work items. Currently, only work items can be created with a name.
- Added login page, signup page, and password reset page in the frontend including the logic to handle verification after signup and requesting for a password reset.
- Introduced the `rbac_manager` in the auth service to handle role-based access control logic.
- Added a `seed_database.py` script to seed the database with default roles and permissions.
- Integrated the seeding script into the `startup.sh` to ensure the database is seeded upon service startup.
- Docker Security Scan Actions workflow: Introduced a new CI/CD workflow that automatically scans for security vulnerabilities using Trivy.
- Docker Build and Push GitHub Actions workflow: Introduced a new CI/CD workflow that automatically builds and pushes the Python Docker image to Docker Hub.
- Settings Configuration: Refactored the settings configuration in the project to improve the structure and ease of use.
- Environment Variables in Docker: Adjusted the Python Dockerfile to support dynamic assignment of the environment variable `ENVIRONMENT`.
- Project: Introduced Docker files for Python and PostgreSQL containers and ensured they can be built and run using docker-compose.
- Project Service: Defined all the models related to project management.
- Auth Service: Started developing the auth service using the FastAPI users library for user management.
- Auth Service Models: Defined the following models: OAuthAccount, Member, Tenant, Team, Role, and Permission.

### Changed

- Dockerfile and docker directories: Dockerfiles and related directories previously residing within individual services have been removed and centralized in the root directory of the project.
- Refactored the seeding process in the auth service to streamline the initialization of roles and permissions.

## [0.0.1] - 2023-07-23

- Initial project setup and repository creation. The basic architecture for the microservices (auth-service and project-service) and frontend (jutsu-ui) have been setup.

## Project started on 2023-07-09
