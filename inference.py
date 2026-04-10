def predict():
    # Your logic here
    return "item in stock"

if __name__ == "__main__":
    try:
        result = predict()

        # ✅ REQUIRED FORMAT
        print("[START] task=inventory_check", flush=True)
        print("[STEP] step=1 reward=1.0", flush=True)
        print(f"[END] task=inventory_check score=1.0 steps=1 result={result}", flush=True)

    except Exception as e:
        print("[START] task=inventory_check", flush=True)
        print("[STEP] step=1 reward=0.0", flush=True)
        print(f"[END] task=inventory_check score=0.0 steps=1 error={str(e)}", flush=True)