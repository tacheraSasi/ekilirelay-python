import requests
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("API_KEY")

  def send_email(api_key, to, subject, message, headers=''):
      url = "https://relay.ekilie.com/api/index.php"
      payload = {
          "apikey": api_key,
          "to": to,
          "subject": subject,
          "message": message,
          "headers": headers
      }
      try:
          response = requests.post(url, json=payload)
          return response.json()
      except Exception as e:
          return {"status": "error", "message": str(e)}
  
  # Usage
  response = send_email(
      API_KEY,
      "python@example.com",
      "Python Test",
      "Hello from Python!",
      "From: Python "
  )
  print(response)