from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "YouTube API is working!"

# Vercel-এর জন্য নিচের অংশটি প্রয়োজন নেই (app.run)

