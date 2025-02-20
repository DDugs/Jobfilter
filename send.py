from twilio.rest import Client

#Twilio credentials (Replace with your actual credentials)
TWILIO_SID = "ACc60d246cecdf41e252dea408c7478e30"
TWILIO_AUTH_TOKEN = "ee98949b8f6b6a90ce5513af5e825c0d"
WHATSAPP_NUMBER = "whatsapp:+14155238886"
YOUR_NUMBER = "whatsapp:+919667195534"

def send_whatsapp_message(job_alert):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=WHATSAPP_NUMBER,
        body=job_alert,
        to=YOUR_NUMBER
    )
    print(f"✅ WhatsApp Message Sent! SID: {message.sid}")

