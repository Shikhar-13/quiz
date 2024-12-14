# Quiz Application

This repository hosts a **Django-based Quiz Application**, allowing users to take quizzes, view results, and manage questions seamlessly. Designed with simplicity and scalability in mind, it leverages Django's powerful features and is deployable via [Vercel](https://vercel.com).

---

## Features

- **Interactive Quiz Interface**: Engage users with an intuitive UI.
- **Dynamic Question Management**: Add, update, or remove questions effortlessly.
- **Database-Backed**: Persistent storage using SQLite.
- **Responsive Design with Tailwind CSS**: Enhanced UI using modern, utility-first CSS framework.
- **Ready for Deployment**: Configured for hosting on Vercel.
- **API Endpoint for Questions**: Easily fetch quiz questions from the database.

---

## Requirements

Ensure the following dependencies are installed:

- Python 3.x
- Django 4.x
- Dependencies listed in `requirements.txt`
- Tailwind CSS CDN

---
## Assumptions
No User verification was needed as it was mentioned one user to take the quiz and thus no user database was created.

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shikhar-13/quiz.git
   cd quiz
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## API Endpoint

### Fetch Questions

Use the following API endpoint to retrieve questions from the database:

```bash
GET /api/questions/
```

This endpoint returns a list of quiz questions in JSON format. Ensure the server is running before making API calls.

---

## Deployment

The application is pre-configured for deployment on Vercel. Ensure the `vercel.json` configuration file is correctly set before deploying.

### Steps for Deployment:

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy the project:
   ```bash
   vercel
   ```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the Repository**.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature-name
   ```

3. **Commit Changes**:
   ```bash
   git commit -m "Description of changes"
   ```

4. **Push the Branch**:
   ```bash
   git push origin feature-name
   ```

5. **Submit a Pull Request**.

---

