# We use this to search and extract information from text.
import re
def parse_log_line(line):   # creates a function that handles one line of a log
    parts = line.split()


    # Check that we have exactly 5 pieces.
    # If not, this is not a valid log format.
    if len(parts) != 5:
        return None


    # Store each part in a variable.
    timestamp = parts[0] + " " + parts[1]

    #store the event type
    event = parts[2]

    user = parts[3].replace("user=", "")

    ip = parts[4].replace("ip=", "")


    # Return the information as a dictionary.
    return {
        "timestamp": timestamp,
        "event": event,
        "user": user,
        "ip": ip
    }
def read_logs(filename):    # this opens the entire log file and reads every line

    events = []                         # Create an empty list.
                                        # We will store all detected log events here.

    with open(filename, "r") as file:       # Open the file in read mode ("r").
                                            # The "with" statement automatically closes
                                            # the file when we finish reading it.
        for line in file:  

            event = parse_log_line(line.strip())

            if event: 
                events.append(event)

    return events                 # Return all collected log events.
    