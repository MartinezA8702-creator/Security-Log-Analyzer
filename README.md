#Security-Log-Analyzer 

Python based security log monitoring and analysis application that parses security events, detects suspicious login activity, stores events in a SQLite database, and provided a web based dashboard for monitoring and searching through security events. 

##Features
-Parse security log files using python
-Extracts timestamps, users, IP addresses, and event types
-Detects repeated failed login attempts
-Generates security alerts for potential brute force attacks
-Stores security events and alerts in SQLite
-Displays total events and security alerts
-Allows users to search seciurity events
-Displays recent security activity
-The application can identify repeated failed login attempts

##Technologies Implemented

-Python 3.11
-Flask
-SQLite
-HTML
-CSS
-Jinja2
-Git and GitHub

## Project Structure    

Security-Log-Analyzer/
│
├── dashboard/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── database/
│   └── database_manager.py
│
├── logs/
│   └── security.log
│
├── src/
│   └── log_parser.py
│
├── requirements.txt
└── README.md



