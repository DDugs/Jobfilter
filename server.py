from flask import Flask
import threading
from main import get_job_emails

app = Flask(__name__)

@app.route('/')
def run_script():
    threading.Thread(target=get_job_emails).start()  # Run in the background
    return "Job email script executed successfully!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
