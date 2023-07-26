# Devjutsu

![Docker Build and Push](https://github.com/jutsuteck/devjutsu/actions/workflows/docker-build-push.yml/badge.svg)
![Docker Security](https://github.com/jutsuteck/devjutsu/actions/workflows/docker-trivy-scan.yml/badge.svg)

## Overview

Devjutsu is a powerful project management tool designed for software developers to streamline secure coding practices. In a world where data security is paramount, Devjutsu integrates globally recognized security standards into its framework, enabling developers to create more secure software applications with ease and precision.

## Features

#### Security Standards Mapping

One of Devjutsu's distinguishing features is the ability to map security standards to user stories. By integrating recognized security protocols into the development lifecycle from the earliest stage, our tool helps you ensure each user story is built on a solid, secure foundation.

#### Dojo - Learn and Grow

A Dojo for software developers is a unique feature of Devjutsu. The Dojo is a learning hub where developers can gain insights into the basics of software security, stay updated on the latest trends, and continue to hone their skills. The ultimate goal is to foster a culture of learning and continuous improvement, helping developers increase their proficiency in secure coding.

## Why Devjutsu?

In an age where security threats are constantly evolving, software developers need a tool that not only helps manage their projects but also assists them in adhering to the highest levels of security. Devjutsu does just that by:

- Ensuring software built is secure from the ground up
- Incorporating globally recognized security standards
- Providing an easy way to map these standards to user stories
- Facilitating continuous learning through the Dojo

## Roadmap

#### Back-End

- `[x]` **Project Service**: Houses the business logic for creating projects, workflows, states, and work items. Unit tests, integration tests, and some model modifications are pending.

  - `[x]` Business logic
  - `[ ]` Unit tests
  - `[ ]` Integration tests
  - `[ ]` Model definitions modifications
  - `[~]` Custom ASVS dataset (in progress)

- `[~]` **Member Service**: Responsible for member registration, authentication, and authorization. This service is currently in progress.

  - `[ ]` Business logic
  - `[ ]` Model definitions

- `[ ]` **Payment Service**: Will handle all the transactions in the application. Yet to be implemented.
- `[ ]` **Dojo Service**: Will manage the educational platform and the learning resources. Yet to be implemented.

#### Front-End

- `[ ]` **Next.js Application**: Front-end development using Next.js is planned.
