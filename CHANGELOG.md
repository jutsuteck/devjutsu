# Changelog

All notable changes to the "jutsu" project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Project: Introduced Docker files for Python and PostgreSQL containers and ensured they can be built and run using docker-compose.

- Project Service: Defined all the models related to project management which includes Project, Epic, Workflow, WorkItem, Task, Label, ASVSSecurityRequirement, ASVSSecurityCategory, and ASVSSecuritySubCategory. Introduced the repository design pattern to separate business logic and database operations, and to facilitate easier testing.

- Auth Service: Started developing the auth service using the FastAPI users library for user management. This includes OAuth accounts and general authentication/authorization. This service uses three Docker containers - a Python container, a PostgreSQL container, and a Redis container for token management. Began experimenting with Alembic for database migrations.

- Auth Service Models: Defined the following models: OAuthAccount, Member, Tenant, Team, Role, and Permission.

## [0.0.1] - 2023-07-23

- Initial project setup and repository creation. The basic architecture for the microservices (auth-service and project-service) and frontend (jutsu-ui) have been setup.

## Project started on 2023-07-09
