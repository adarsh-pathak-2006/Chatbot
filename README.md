# About Me Chatbot - AI Backend

This is a Django REST Framework backend application that integrates with Google's Gemini AI to power an "About Me" chatbot. The chatbot uses a predefined knowledge base to answer questions specifically about the user (Adarsh).

## Features
- **User Authentication:** Registration and JWT-based authentication.
- **AI Integration:** Uses `google-genai` to communicate with Google's Gemini 2.5 Flash model.
- **Conversation History:** Stores user queries and AI responses in a database.
- **Robust Prompting:** Limits AI answers to only the provided knowledge base.
- **Deployment Ready:** Configured with `dj-database-url`, `whitenoise`, and `django-cors-headers` for seamless deployment on platforms like Render.

## Prerequisites
- Python 3.10+
- Google Gemini API Key

## Local Setup

1. **Clone the repository and navigate into the project:**
   ```bash
   git clone <repo_url>
   cd "About Me Chatbot/chatbot"
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Copy the `.env.example` file to `.env` and fill in your Gemini API key.
   ```bash
   cp .env.example .env
   ```
   *Make sure you provide a valid `GEMINI_API_KEY` in the `.env` file.*

5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://localhost:8000`.

## API Endpoints

- **`POST /register/`**: Register a new user account.
- **`POST /token/`**: Retrieve JWT access and refresh tokens.
- **`POST /token/refresh/`**: Refresh a JWT token.
- **`GET /api/chat/`**: Retrieve the authenticated user's chat history.
- **`POST /api/chat/`**: Send a new message to the AI chatbot. (Requires JWT Authentication)

## Deployment (e.g., Render)

This project is fully configured for cloud deployment. 

1. **Build Command:** Configure your deployment service to use the included build script:
   ```bash
   ./build.sh
   ```
   *(This installs dependencies, collects static files, and runs migrations)*

2. **Start Command:** Use Gunicorn to run the application:
   ```bash
   gunicorn chatbot.wsgi:application
   ```

3. **Environment Variables Required in Production:**
   - `SECRET_KEY`: Your Django secret key.
   - `DEBUG`: Set to `False`.
   - `ALLOWED_HOSTS`: Set to your production domain (e.g., `api.yourdomain.com`).
   - `DATABASE_URL`: The PostgreSQL connection string provided by your host.
   - `GEMINI_API_KEY`: Your Google AI Studio API key.

## Project Structure
- `chatbot/`: Main Django project configuration and settings.
- `core/`: Django app containing models, views, and serializers.
- `services/`: Business logic for prompt building and AI integration.
