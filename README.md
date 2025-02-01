
# ArogyaMann

ArogyaMann is a full-stack web application developed using Django and React to provide vital mental health resources. It integrates multiple features such as mood and sleep tracking, a 24/7 chatbot, suicide awareness education, and a community network to support individuals facing mental health challenges.

![image](https://github.com/user-attachments/assets/5db30ac8-f9ab-4ed2-b43c-ae2df40e4737)



## Features

- Mood & Sleep Tracking: Enables users to monitor their mental well-being over time.

- 24/7 Chatbot Support: Provides instant assistance and guidance for mental health concerns.

- Suicide Awareness Education: Educates users on warning signs, risk factors, and ways to seek help.

- Community Network: Allows users to engage in discussions and share experiences to reduce stigma.

- User Authentication: Secure signup and login functionality using JWT authentication.

- Accessibility Focus: Designed with an intuitive UI and accessibility considerations.


## Tech Stack

**Client:** React.js, Redux, Tailwind CSS

**Server:** Django, Django REST Framework

**Databases:** SQLite

**API Communication:** RESTful APIs for secure data exchange




## 

What optimizations did you make in your code? E.g. refactors, performance improvements, accessibility


## Installation

Prerequisite for project
- Node(For react)
- Python and Django(Backend)
    
## Run Locally

### For Backend

Clone the project

```bash
  git clone https://github.com/harshwarghade22/ArogyaMann
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
### For Frontend


Go to the project directory

```bash
  cd client
```

Install Dependencies

```bash
  npm i
```

Start the server

```bash
  npm run dev
```


## Usage

- Open http://localhost:3000/ to access the frontend.

- The Django backend runs at http://localhost:8000/.

- Users can sign up, track their mood, interact with the chatbot, and access mental health resources


## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

