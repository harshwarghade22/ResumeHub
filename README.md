
# ResumeHub

ResumeHub is a platform designed to assist users in building professional resumes, checking ATS (Applicant Tracking System) scores, and providing insights to enhance resume effectiveness. The goal is to simplify the resume creation process while ensuring compatibility with modern hiring systems.





## Features

- Resume Builder: Generates professional resumes with structured formatting.

- ATS Score Checker: Evaluates resumes for ATS compatibility and provides optimization suggestions.

- PDF Generation: Converts resumes into downloadable PDF formats.

- User Authentication: Secure signup and login functionality.

- User-Friendly Interface: Intuitive design for seamless resume creation.


## Tech Stack

**Client:** HTML/CSS

**Server:** Django

**Databases:** SQLite

**API Communication:** RESTful APIs for secure data exchange

**PDF Generation:** Python Libraries 




## 

What optimizations did you make in your code? E.g. refactors, performance improvements, accessibility


## Installation

Prerequisite for project
- Python and Django(Backend)
    
## Run Locally

### For Backend

Clone the project

```bash
  git clone https://github.com/harshwarghade22/ResumeHub
```

Create and Activate virtual environment 

```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
```

Go to the project directory

```bash
  cd server
```

Apply migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## Usage

- 

- The Django backend runs at http://localhost:8000/.

- Users can create resumes, check ATS scores, and download PDFs.


## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.


