import time
import csv
import os
from twilio.rest import Client

# Use environment variables for credentials
account_sid = os.getenv('ACCOUNT_SID', 'default_sid')
auth_token = os.getenv('AUTH_TOKEN', 'default_token')
client = Client(account_sid, auth_token)

responded_messages_file = "responded_messages.txt"
incoming_messages_log = "incoming_messages.csv"


def initialize_files():
    """Ensure necessary files exist at startup."""
    if not os.path.exists(responded_messages_file):
        open(responded_messages_file, 'a').close()

    if not os.path.exists(incoming_messages_log):
        with open(incoming_messages_log, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["From Number", "Incoming Message"])


def read_responded_messages():
    """Read message SIDs from the log of responded messages."""
    try:
        with open(responded_messages_file, "r", encoding='utf-8') as file:
            responded_messages = file.read().splitlines()
        return responded_messages
    except Exception as e:
        print(f"Error reading responded messages: {e}")
        return []


def write_responded_message(message_sid):
    """Log a message SID to the file of responded messages."""
    try:
        with open(responded_messages_file, "a", encoding='utf-8') as file:
            file.write(message_sid + "\n")
    except Exception as e:
        print(f"Error writing responded message SID: {e}")


def log_incoming_message(from_number, message_body):
    """Log incoming message details to a CSV file."""
    try:
        with open(incoming_messages_log, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([from_number, message_body])
    except Exception as e:
        print(f"Error logging incoming message: {e}")


def check_and_respond_to_messages():
    """Check for new messages, log, respond, and record them."""
    responded_messages = read_responded_messages()

    try:
        messages = client.messages.list(limit=20)
    except Exception as e:
        print(f"Error fetching messages from Twilio: {e}")
        messages = []

    for msg in messages:
        if msg.direction == "inbound" and msg.sid not in responded_messages:
            print(f"Processing message from {msg.from_}")
            log_incoming_message(msg.from_, msg.body)

            try:
                response = client.messages.create(
                    body="שלום מתאי טורס תאילנד, עברנו לווצאפ הרשמי: +66825504691",
                    from_=msg.to,
                    to=msg.from_
                )
                print(f"Sent response message: {response.sid}")
                write_responded_message(msg.sid)
            except Exception as e:
                print(f"Error sending response: {e}")


if __name__ == "__main__":
    initialize_files()
    while True:
        check_and_respond_to_messages()
        print("Waiting for new messages...")
        time.sleep(10)  # Adjust sleep time as needed