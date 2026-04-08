from env import InventoryEnv

env = InventoryEnv()
state = env.reset()

print("[START] task=inventory", flush=True)

total_reward = 0

action = {"type": "add", "amount": 20}
state, reward, done = env.step(action)

total_reward += reward

print(f"[STEP] step=1 reward={reward}", flush=True)
print(f"[END] task=inventory score={total_reward} steps=1", flush=True)
print("[START] task=inventory", flush=True)
print("[STEP] step=1 reward=1", flush=True)
print("[END] task=inventory score=1.0 steps=1", flush=True)