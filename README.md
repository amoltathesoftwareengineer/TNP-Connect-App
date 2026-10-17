# TNP Connect App

A student placement management application designed to connect students, placement teams, and recruitment opportunities through a centralized platform.

## Overview

TNP Connect App organizes student profiles, job listings, eligibility information, applications, and recruitment updates.

The project demonstrates database-driven workflows and role-based application management.

## Key Features

- Student profile management
- Company and job listings
- Eligibility criteria
- Job application tracking
- Recruitment status updates
- Placement team dashboard
- Search and filtering
- Placement statistics
- Role-based access controls

## Technology Stack

- Python
- Flask
- MySQL
- HTML5 and CSS3
- Bootstrap
- JavaScript

## Proposed Database Tables

- `students`
- `companies`
- `job_postings`
- `applications`
- `users`
- `departments`

## Project Structure

```text
TNP-Connect-App/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── README.md
├── templates/
├── static/
└── tests/
```

## Installation

```bash
git clone https://github.com/amoltathesoftwareengineer/TNP-Connect-App.git
cd TNP-Connect-App
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the database using `database.sql`, configure credentials, and start the application:

```bash
python app.py
```

## Data Integrity and Security

- Enforce valid student and job relationships.
- Prevent duplicate applications where required.
- Validate job eligibility on the server.
- Protect student records using role-based permissions.
- Never store plain-text passwords.

## Future Enhancements

- Email and notification integration
- Resume management
- Interview scheduling
- Placement analytics dashboard
- Exportable reports
- Mobile-responsive interface

## Author

Amol Tathe

GitHub: https://github.com/amoltathesoftwareengineer

## License

Add an appropriate open-source license before permitting reuse.
