# Flask Server Logs Parser
## Overview
- This Python Flask application is designed to parse server logs and calculate the total time duration recorded in those logs. The logs should be stored in the "server_logs" directory within the project.

## Prerequisites
- Make sure you have Python and Flask installed on your system. If not, you can install Flask using the following command:
```bash
 pip install Flask
```

## Usage
Clone the repository to your local machine:
```bash
git clone <repository-url>
```
Navigate to the project directory:
```bash
cd <project-directory>
```
Run the Flask application:
```bash
python app.py
```
Open your web browser and go to http://127.0.0.1:5000/ to access the application.
## Application Structure
- app.py: The main Flask application file.
- templates/homepage.html: HTML template for the home page.
- templates/time.html: HTML template for displaying the parsed time.

## How It Works
- The user visits the home page where a list of available log files is displayed.
- Upon selecting a log file and submitting the form, the application parses the selected log file and calculates the total time duration recorded in the log.
- The result is displayed on a new page showing the total time duration in hours and minutes.

## Important Note
Ensure that the log files are stored in the "server_logs" directory with the appropriate format. The parser function specifically looks for lines containing 'Time Log:' to start parsing.

Feel free to customize the application based on your specific log file format and requirements.
