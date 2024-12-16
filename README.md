## Overview

You have a Django-based project that already loads users from `data/users.csv` and exposes them at `/users/`. However, there’s a file `app/legacy_service.py` which contains messy, standalone logic for loading users, searching them, and serving them via a basic HTTP server. Your first task is to **refactor and integrate this legacy code into the Django application** in a clean, maintainable way.

After refactoring:

1. Ensure all data access and user queries are handled via Django models or a proper service layer.
2. Remove global state and improve code structure.
3. Replace the legacy HTTP logic with Django views and URLs.

**Then**, add a **daily notification pipeline** that:
- Uses OpenAI’s API to generate a daily health message for each user.
- Sends that message to a mock external endpoint (e.g., `http://localhost:5001/notifications`).
- Each user should receive one daily notification from one of three categories:
  - Daily health reminders
  - Personalized health insights
  - Educational tips

Your pipeline can be triggered by a management command (e.g. `python manage.py runpipeline`).

**Additional Requirements:**
- Write tests (unit and/or integration) for the notification pipeline and the refactored user lookup logic.
- Integrate tests into the provided CI workflow.
- Provide a Dockerfile and ensure the project can run in a container.
- Document your solution, design decisions, and instructions for running the code and tests in this README.

### Time Expectation
This exercise is scoped to about 6 hours. We do not expect a production-ready final product, but we want to see how you think and what trade-offs you make.

### Running the Base Project

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py load_users
python manage.py runserver



