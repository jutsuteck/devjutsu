# System Architecture Document: Devjutsu

### 1. Introduction

#### 1.1. Purpose

Devjutsu is an agile project management tool designed to streamline secure software development for developers, especially those with limited software security experience. It aims to embed security into the software development lifecycle (SDLC) from the outset, ensuring robust application security and fostering a proactive security culture.

#### 1.2. Scope

Devjutsu offers basic project management features such as creating and managing projects, defining workflows, and assigning users to individual work items. Unique to Devjutsu is its security requirements mapping feature, which will utilize an NLP model in its commercial version. While the MVP focuses on core features, future iterations will integrate with platforms like GitHub and GitLab.

#### 1.3. Definitions, Acronyms, and Abbreviations

- **Workflows**: Represents the flow of work within a project. Can be ongoing (Kanban) or time-scoped (Sprint in Scrum).
- **Work Items**: Defined tasks for software developers, e.g., user stories or bugs.
- **Tasks**: Smaller units of work derived from work items.
- **Security Requirements**: Controls mapped to work items to ensure their security.

### **2. Architectural Representation**

Devjutsu adopts a microservices architecture. The primary services include the Auth Service, Project Service, and Dojo Service. Kong serves as the API Gateway.

### **3. Logical View**

#### 3.1. Overview

Devjutsu's architecture is modular, with distinct services handling different functionalities.

#### 3.2. Component Descriptions

- **Auth Service**:

  - **Purpose**: Manages user-related functionalities.
  - **Responsibilities**: Implements models, business logic, and API endpoints related to users, roles, permissions, tenants, and clans.
  - **Interactions**: Provides user ownership, assignment, and restriction details to the Project Service.

- **Project Service**:

  - **Purpose**: Central hub for all project management tasks.
  - **Responsibilities**: Implements models, business logic, and API endpoints for project management, including security controls from the AVS.
  - **Interactions**: Retrieves user details from the Auth Service.

- **Dojo Service**:
  - **Purpose**: Educational hub for users.
  - **Responsibilities**: Will offer articles, tutorials, and courses related to software security and development in future iterations.

### 4. Process View

(To be detailed further based on how processes or threads interact within and across services.)

### 5. Deployment View

(To be detailed further based on deployment strategy, hardware, cloud services, or containers involved.)

### 6. Implementation View

(To be detailed further based on codebase organization, naming conventions, and directory structures.)

### 7. Data View

(To be detailed further based on data storage, flow, and models.)

### 8. Security Architecture

(To be detailed further based on codebase organization, naming conventions, and directory structures.)

### 9. Quality

(To be detailed further based on quality assurance measures, testing strategies, and performance monitoring.)

### 10. Evolution Perspective

While the MVP of Devjutsu focuses on core project management and security features, future versions will expand to include integrations with popular platforms like GitHub and GitLab, as well as educational content through the Dojo Service.

### 11. Rationale

The decision to create Devjutsu stems from the pressing need to integrate security seamlessly into the SDLC. By providing developers with a tool that not only aids in project management but also emphasizes security from the start, Devjutsu aims to revolutionize the way developers approach secure coding.
