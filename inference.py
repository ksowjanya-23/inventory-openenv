def run_agent():
    stock = 50
    total_steps = 5

    print("[START] task=inventory", flush=True)

    for step in range(total_steps):

        if stock < 20:
            reward = 1.0
            stock += 10
        elif stock > 80:
            reward = 0.5
            stock -= 10
        else:
            reward = 0.8

        print(f"[STEP] step={step+1} reward={reward}", flush=True)

    score = stock / 100
    print(f"[END] task=inventory score={score} steps={total_steps}", flush=True)


# 🔥 THIS LINE IS CRITICAL
run_agent()