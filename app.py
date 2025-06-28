from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

HF_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    resp = requests.post(HF_URL, headers=HEADERS, json={"inputs": user_msg})
    try:
        data = resp.json()
        # If response is a list, grab generated_text from first item
        reply = data[0]["generated_text"] if isinstance(data, list) else data.get("generated_text","দুঃখিত, বুঝতে পারিনি।")
    except:
        reply = "ওপস! কিছু একটা সমস্যা হয়েছে।"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
