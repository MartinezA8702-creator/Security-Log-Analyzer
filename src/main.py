from log_parser import read_logs
from detector import detect_bruteforce
from database_manager import(
    create_connection,
    create_tables,
    save_event,
    save_alert,
    show_events
)

# Create database connection
database = create_connection()

create_tables(database)

print("Database tables created successfully!")

print("Database created successfully!")


#location of security log file
log_file = "logs/security.log"


print("Starting security log analyzer...")


#read logs
logs = read_logs(log_file)


print("Number of logs found:", len(logs))


#analyze logs for threats
alerts = detect_bruteforce(logs)


print("\nSecurity Alerts:")
print("----------------")


#display detected threats
for alert in alerts:

    print("Severity:", alert["severity"])
    print("Threat:", alert["type"])
    print("IP Address:", alert["ip"])
    print("Details:", alert["message"])
    print()

    logs = read_logs(log_file)

    # Store every log event in the database
for log in logs:
    save_event(database, log)

    alerts = detect_bruteforce(logs)

    # Store every security alert in the database
for alert in alerts:
    save_alert(database, alert)

    # Display everything stored in the database.
show_events(database)