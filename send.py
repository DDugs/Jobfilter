from twilio.rest import Client

#Twilio credentials (Replace with your actual credentials)
TWILIO_SID = "your_credentials_here"
TWILIO_AUTH_TOKEN = "your_credentials_here"
WHATSAPP_NUMBER = "whatsapp:twilio_number"
YOUR_NUMBER = "whatsapp:+91_your_number"

def send_whatsapp_message(job_alert):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=WHATSAPP_NUMBER,
        body=job_alert,
        to=YOUR_NUMBER
    )
    print(f"✅ WhatsApp Message Sent! SID: {message.sid}")

