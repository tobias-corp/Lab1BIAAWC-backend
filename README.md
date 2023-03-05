# Flask Web App

A simple Flask web app for greeting users and serving static files of frontend.

## Getting Started

1. Clone the repository.
2. Install the requirements: `pip install -r requirements.txt`.
3. Run the app: `python app.py`.
4. Navigate to `http://localhost:5000` in your web browser to view the app.

## Routes

- `/`: Renders a simple greeting to the user.
- `/greet/<name>`: Renders a personalized greeting to the user.
- `/static/<path:path>`: Serves a static frontend file from the `static` directory.
