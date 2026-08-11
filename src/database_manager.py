#Import pythons built in SQLite database library
import sqlite3

#location where our database file be created
DATABASE_PATH = "database/security_events.db"

#This function creates a connection to our database
def create_connection():

    #sqlite will automatically create the database
    connection =sqlite3.connect(DATABASE_PATH)

    return connection

def create_tables(connection):

     # Creates a cursor to execute SQL commands
    cursor = connection.cursor()

    # Create events table.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        event TEXT,

        username TEXT,

        ip TEXT

    )
    """)


    # Create alerts table.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        threat_type TEXT,

        ip TEXT,

        severity TEXT,

        message TEXT

    )
    """)


    # Save the changes.
    connection.commit()

# Saves a security event into the database.
def save_event(connection, event):

    cursor = connection.cursor()


    cursor.execute("""
    INSERT INTO events
    (timestamp, event, username, ip)

    VALUES (?, ?, ?, ?)
    """,
    (
        event["timestamp"],
        event["event"],
        event["user"],
        event["ip"]
    ))


    connection.commit()    

# Saves a detected threat alert into the database.
def save_alert(connection, alert):

    cursor = connection.cursor()


    cursor.execute("""
    INSERT INTO alerts
    (threat_type, ip, severity, message)

    VALUES (?, ?, ?, ?)
    """,
    (
        alert["type"],
        alert["ip"],
        alert["severity"],
        alert["message"]
    ))


    connection.commit()

    # Display all events stored in the database.
def show_events(connection):

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM events")

    events = cursor.fetchall()

    print("\nDatabase Events")
    print("----------------")

    for event in events:
        print(event)

