from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Replace with your real key or set it as environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You create complete HTML websites from user prompts."},
                {"role": "user", "content": f"Build a website based on: {prompt}"}
            ],
            max_tokens=1500,
            temperature=0.7
        )

        return jsonify({"result": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
