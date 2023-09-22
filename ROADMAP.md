# Roadmap for Devjutsu

## Introduction

Secure software development isn't just a best practice—it should be the norm. Yet, security is frequently sidelined, often due to a lack of awareness or understanding among developers. Devjutsu is our answer to this challenge. Our mission is to bridge the divide between software security and software development, catering to developers across all expertise levels. This roadmap delineates our journey to craft Devjutsu into an intuitive tool, ensuring that every developer—regardless of their background or proficiency in software security—can embark on creating secure software.

## Vision

Devjutsu envisions itself as the premier project management tool, dedicated to empowering and educating software developers and teams in crafting secure software from inception. Our ambition extends beyond catering to individual developers or small teams; we aspire for Devjutsu to be embraced by large enterprises, becoming an integral part of their software development and security ecosystem.

## Current Status

**Current Status of Devjutsu**

Devjutsu is currently in its developmental phase and has not reached a release-ready state. While I've made significant strides, there's still a journey ahead:

- **Authentication & User Management**:

  - User signup, authentication, and authorization mechanisms are operational.
  - Users can update their basic data.
  - Roles and permissions have been established.

- **Project Management**:

  - Users can create new projects and view an overview of their projects.
  - A foundational template for the project board is in place, allowing for the creation and addition of new work items. However, this feature remains in its nascent stage and requires further enhancement.

- **Areas for Further Development**:
  - Many features await implementation or refinement.
  - Several design decisions are still under deliberation.
  - An onboarding process post-signup is in the pipeline.
  - Email transactions following signup are yet to be designed and integrated.
  - Comprehensive project management functionalities are still in the works.

I am committed to polishing these features and introducing new ones to ensure Devjutsu meets its envisioned potential.

Here's a refined version of your feature tasks:

---

## Devjutsu

### API Gateway

- [x] Integrate Kong for API Gateway
- [ ] Implement rate limiting

### Auth Service API

The `auth-service` manages user (member) creation, authentication, and authorization. It also oversees Clan (team) and Tenant Management, ensuring the right roles and permissions are defined.

- [x] Set up user registration
- [x] Establish user authentication
- [x] Integrate OAuth authentication
- [x] Enable user profile updates

### Project Service API

The `project-service` stands as Devjutsu's backbone, encompassing the essential business logic. This allows users to manage projects, design workflows, and create work items securely, while also addressing security requirements.

- [x] Facilitate project initiation
- [ ] Configure project security levels (ASVS compliance)
- [ ] Design workflow structures
- [ ] Define workflow states
- [ ] Facilitate work item (referred to as "issues") creation

---

This version maintains the essence of your original tasks while refining the language for clarity and consistency.
