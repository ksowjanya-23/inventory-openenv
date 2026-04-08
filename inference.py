def run_agent():
    stock = 50
    total_steps = 5

    print("[START] task=inventory", flush=True)

    for step in range(total_steps):

        if stock < 20:
            action = {"type": "add", "amount": 10}
            reward = 1.0
        elif stock > 80:
            action = {"type": "remove", "amount": 10}
            reward = 0.5
        else:
            action = {"type": "add", "amount": 0}
            reward = 0.8

        if action["type"] == "add":
            stock += action["amount"]
        elif action["type"] == "remove":
            stock -= action["amount"]

        print(f"[STEP] step={step+1} reward={reward}", flush=True)

    score = stock / 100

    print(f"[END] task=inventory score={score} steps={total_steps}", flush=True)


if __name__ == "__main__":
    run_agent()