# final submission version 2

import json

def predict():
    # 👉 Replace this with your actual logic if needed
    result = "item in stock"  # You can change this to your model output

    return result

if __name__ == "__main__":
    try:
        output = predict()

        # ✅ REQUIRED: Structured JSON output
        print(json.dumps({
            "prediction": output
        }))

    except Exception as e:
        # ✅ Always handle errors properly
        print(json.dumps({
            "error": str(e)
        }))