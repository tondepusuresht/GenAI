from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace YOUR_OPENAI_KEY
openai.api_key = "YOUR_OPENAI_KEY"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    return jsonify(response.choices[0].text.strip())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
