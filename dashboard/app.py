from flask import Flask, render_template, request
import sqlite3

#create the flask application
app = Flask(__name__)

#Location of our SQlite database
DATABASE = "../database/security_events.db"

#function to connect to the database
def get_database():

    connection = sqlite3.connect(DATABASE)

    #allows us to access database columns by name
    connection.row_factory = sqlite3.Row

    return connection

#Main dashboard page
@app.route("/")
def dashboard():

       # Connect to database
    database = get_database()

  # Get search text from the webpage
    search = request.args.get("search", "")


    # Count how many log events exist
    total_events = database.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    #count how many security alerts exist
    total_alerts = database.execute(
        "SELECT COUNT(*) FROM alerts"
    ).fetchone()[0]

     # If the user searched something
    if search:

        events = database.execute(
            """
            SELECT *
            FROM events
            WHERE user LIKE ?
            OR ip LIKE ?
            OR event LIKE ?
            ORDER BY id DESC
            """,
            (
                "%" + search + "%",
                "%" + search + "%",
                "%" + search + "%"
            )

        ).fetchall()

    else:

    # Get the latest 10 security events
        events = database.execute(
    """
    SELECT *
    FROM events
    ORDER BY id DESC
    LIMIT 10
    """
    ).fetchall()

      # Get alerts
    alerts = database.execute(
        """
        SELECT *
        FROM alerts
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()

    #close database connection
    database.close()

    #sends data to the webpage
    return render_template(
        "index.html",
        total_events=total_events,
        total_alerts=total_alerts,
        alerts=alerts,
        events=events,
        search=search
    )

#start the server
if __name__ == "__main__":

    app.run(debug=True)
