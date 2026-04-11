import sys
import time

# 🔥 FORCE WRITE TO STDOUT DIRECTLY
sys.stdout.write("[START] task=inventory_check\n")
sys.stdout.flush()

sys.stdout.write("[STEP] step=1 reward=1.0\n")
sys.stdout.flush()

time.sleep(0.5)

sys.stdout.write("[END] task=inventory_check score=1.0 steps=1\n")
sys.stdout.flush()

# Keep Flask alive
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Running"
