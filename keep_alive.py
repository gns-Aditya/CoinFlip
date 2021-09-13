#this one's use to keep the bot alive and prevents it from going inactive
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
  return 'Yikes'

def run():
  app.run(host = '0.0.0.0',port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()
