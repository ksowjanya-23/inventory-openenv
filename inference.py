import os
from openai import OpenAI

# ===== START LOG =====
print("START")

# ===== ENV VARIABLES =====
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

# Optional (only if needed)
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

print("STEP: Environment variables loaded")

# ===== OPENAI CLIENT =====
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

print("STEP: OpenAI client initialized")

# ===== SIMPLE INVENTORY LOGIC =====
def run_agent():
    stock = 50

    for step in range(5):
        print(f"STEP: Current stock = {stock}")

        # simple logic (you can improve later)
        if stock < 20:
            action = {"type": "add", "amount": 10}
        elif stock > 80:
            action = {"type": "remove", "amount": 10}
        else:
            action = {"type": "add", "amount": 0}

        print(f"STEP: Action = {action}")

        # apply action
        if action["type"] == "add":
            stock += action["amount"]
        elif action["type"] == "remove":
            stock -= action["amount"]

    print(f"STEP: Final stock = {stock}")


# ===== RUN =====
run_agent()

# ===== END LOG =====
print("END")