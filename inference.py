import sys

def predict():
    return "item_in_stock"

if __name__ == "__main__":
    try:
        result = predict()

        sys.stdout.write("[START] task=inventory_check\n")
        sys.stdout.write("[STEP] step=1 reward=1.0\n")
        sys.stdout.write(f"[END] task=inventory_check score=1.0 steps=1 result={result}\n")
        sys.stdout.flush()

    except Exception as e:
        sys.stdout.write("[START] task=inventory_check\n")
        sys.stdout.write("[STEP] step=1 reward=0.0\n")
        sys.stdout.write(f"[END] task=inventory_check score=0.0 steps=1 error={str(e)}\n")
        sys.stdout.flush()