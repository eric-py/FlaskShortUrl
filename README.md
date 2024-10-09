# FLASK Shorturl

FLASK shorturl is a Flask-based web application that allows users to create shortened versions of long URLs. This project provides a simple and efficient way to manage and share links.

## Features

- Shorten long URLs to easily shareable links
- Store and retrieve shortened URLs
- Redirect users from short URLs to original long URLs
- Flash messages for user feedback

## Getting Started

### Installation

1. Clone the repository:
    - git clone
    - `cd flask-shorturl`

2. Set up a virtual environment (optional but recommended):
    - `python -m venv venv`
    - `source venv/bin/activate`  # On `Windows use venv\Scripts\activate`

3. Install the required packages:
    - `pip install -r requirements.txt`

4. Run the application:
    - `python run.py`

## Usage

1. Enter a long URL in the input field on the home page.
2. Click the "Shorten" button.
3. If successful, you'll see a flash message with the shortened URL.
4. Use the shortened URL to redirect to the original long URL.

## Project Structure

- `app/`: Main application package
  - `__init__.py`: Application factory and configuration
  - `models.py`: Database models
  - `forms.py`: Form definitions
  - `views.py`: Route handlers
  - `error_handlers.py`: Custom error pages
  - `templates/`: HTML templates
  - `static/`: CSS, JavaScript, and other static files
- `run.py`: Application entry point