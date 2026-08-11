from collections import defaultdict

#this function checks for repeated failed login attempts
def detect_bruteforce(events):

    failed_attempts = defaultdict(int)

    #store detected secuirty alerts here
    alerts = []

    #check every log event
    for event in events:
        
        #only look for failed login attempts
        if event["event"] == "LOGIN_FAILED":
            
            #get the IP address from the event
            ip = event ["ip"]

            #increase the failed login count
            failed_attempts[ip] += 1

            #if an IP fails 5 or more times
            #create a security alert
            if failed_attempts[ip] >=5:

                alerts.append({

                    "type": "Brute Force Attack",

                    "ip": ip,

                    "severity": "HIGH",

                    "message":
                    f"{failed_attempts[ip]} failed login attempts detected"
                })

    #return all detected threats
    return alerts

