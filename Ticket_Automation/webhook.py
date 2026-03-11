from flask import Flask, request
import requests
import json

# Initialize Flask application
app = Flask(__name__)

# Jira authentication and project configuration
email = "********"
api_token = "********"
domain = "********"
key = "********"

# Webhook endpoint that receives alerts from Splunk
@app.route("/splunk-alert", methods=["POST"])
def splunk_alert():

    # Extract JSON payload sent by Splunk alert
    data = request.json
    result = data.get("result", {})

    # Extract relevant fields from the alert
    attacker_ip = result.get("src_ip", "unknown")
    user = result.get("user", "unknown")
    host = result.get("host", "unknown")
    count = result.get("count", "unknown")

    # Construct Jira issue payload
    payload = {
        "fields": {
            "project": {"key": key},
            "summary": f"RDP Brute Force Detected from {attacker_ip}",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {"type": "paragraph", "content": [
                        {"type": "text", "text": f"Host: {host}\nUser: {user}\nFailed Attempts: {count}"}
                    ]}
                ]
            },
            "issuetype": {"name": "Task"}
        }
    }

    # Send POST request to Jira REST API to create a ticket
    url = f"{domain}/rest/api/3/issue"
    r = requests.post(
        url,
        auth=(email, api_token),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    # Check if ticket creation was successful
    if r.status_code == 201:
        return "Ticket created", 201
    else:
        return f"Error creating ticket: {r.text}", 400


if __name__ == "__main__":
    # Run Flask server and allow external connections
    app.run(host="0.0.0.0", port=5000)


