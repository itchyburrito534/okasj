import time
import requests
from flask import Flask
from threading import Thread
import sys
import os

TOKEN = str(sys.argv[1])
CHANNEL_ID = str(sys.argv[1]) 
token = os.getenv(TOKEN)
channel_id = os.getenv(CHANNEL_ID)
 
count = 0
url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
headers = {
  'authorization': token
}
 
 
app = Flask('')
 
@app.route('/')
def home():
	return ("Bot is up")
 
def run():
  app.run(
		host='0.0.0.0',
		port=8080
	)
 
def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
 
keep_alive()
while True:
	response = requests.request("POST", url, headers=headers)
	if response.status_code != 204:
		print(response.text)
		print("Failed")
	else:
		count += 1
		print(f"Sent - {count}")
	time.sleep(10)
