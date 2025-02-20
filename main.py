import sys
sys.stdout.reconfigure(encoding='utf-8')

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from send import send_whatsapp_message
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def authenticate_gmail():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds

def get_job_emails():
    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)
    query = 'from:srm@haveloc.com OR subject:"new job posted" -subject:"Haveloc Telegram personal channel invite"'

    results = service.users().messages().list(userId="me", q=query, maxResults=2).execute()
    messages = results.get("messages", [])
    
    if not messages:
        print("No job emails found.")
        return

    print(f"Found {len(messages)} job-related emails:\n")

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = msg_data["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown Sender")
        snippet = msg_data['snippet']
        snippet_trimmed = snippet[:900] + "..." if len(snippet) > 900 else snippet

        print(f"From: {sender}")
        print(f"Subject: {subject}")
        print(f"Snippet: {msg_data['snippet']}\n".encode("utf-8", "ignore").decode("utf-8"))
        print("=" * 50)

        job_alert = f"📢 *New Job Alert!*\n\n📩 *From:* {sender}\n📌 *Subject:* {subject}\n🔎 *Preview:* {snippet_trimmed}"
        send_whatsapp_message(job_alert) 

get_job_emails()
