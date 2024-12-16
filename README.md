## Overview

You have a legacy codebase (`user_service.py`) that loads user data from a CSV and provides user lookup functionality via a CLI and a simple HTTP endpoint. This code is currently in a single file, uses global state, and mixes responsibilities. We need you to:

1. **Refactor and improve the existing codebase** for maintainability, scalability, and testability.
2. **Introduce a daily notification pipeline feature** that sends one in-app notification per day to each user.
3. **Demonstrate your approach to infrastructure and testing.**

## Detailed Requirements

### Refactoring the Existing Code

- The provided `user_service.py` file is messy and not production-ready.
- Refactor it into a cleaner architecture. Consider separating:
  - Data access logic (loading and querying users)
  - Business logic (finding users by ID or name)
  - HTTP interface
  - CLI interface
- Remove global state and make the data source configurable.
- Add docstrings, comments, and follow best practices for Python code structure.
- You can introduce additional directories and files as needed.

### Notification Pipeline Feature

Your new feature: the app should send **one in-app notification per user per day**, chosen from three message categories:

- Daily health reminders
- Personalized health insights
- Educational tips

**Details:**

- Assume each user subscribes to all three types of messages.
- Each day, a pipeline should run that selects a message (the selection method is up to you—could be random, round-robin, or hard-coded for this exercise).
- The pipeline should then send the notification text to an external service. For simplicity, assume an external notification API endpoint is available at `http://localhost:5001/notifications`. In reality, you can mock or simulate this endpoint.
- The logic should be designed so that it can be scaled or replaced easily (e.g., make the notifier a separate component/class).
- The pipeline could be triggered by a CLI command or a simple Python script that you run once per day (`python pipeline.py` or similar).

### Testing

- Add unit tests for at least the user data access and notification sending logic.
- Consider integration tests for the pipeline.
- Use a testing framework of your choice (pytest recommended).
- Show how tests are run locally.

### Infrastructure & CI

- Provide a `Dockerfile` that can build and run the service.
- Provide a sample CI workflow (`.github/workflows/ci.yml`) that runs the tests.  
  *Note: It doesn’t have to be fully functional but should indicate how you'd integrate CI.*
- Document how to build and run the service and how to run tests in your README.

### Deliverables

- Refactored code in a clean structure.
- New modules/classes for the notification pipeline.
- At least a few tests covering core logic.
- A Dockerfile for building and running the service.
- A brief CI configuration file.
- A README explaining:
  - How to run the service (both locally and in Docker).
  - How to run tests.
  - How the daily notification pipeline works.
  - The reasoning behind your architectural decisions.

### Time Expectation

This exercise is scoped to a few hours (approx. 4-6 hours). We do not expect a production-ready final product, but we want to see how you think and what trade-offs you make.

---

## Getting Started

1. **Install dependencies**:  
   This project uses only standard Python libraries at the start. You are free to introduce new libraries (like `requests` for HTTP calls, `pytest` for testing, etc.).  
   
   **Note:** Create a `requirements.txt` if you add dependencies and update the Dockerfile accordingly.

2. **Run the existing service locally**:  
   ```bash
   cd src
   python user_service.py
