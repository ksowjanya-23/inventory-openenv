import os

# 🔥 FORCE inference.py to run
os.system("python inference.py")

# Keep minimal app so HF doesn't crash
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Running"
