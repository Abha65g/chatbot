from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Groq client
client = Groq(
api_key=os.getenv("GROQ_API_KEY"))

# Home Route
@app.route('/')
def home():
    return render_template('chat.html')

# Chat Route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"error": "No input provided!"})

    try:
        # Generate AI response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.1-8b-instant",
        )

        ai_message = chat_completion.choices[0].message.content

        return jsonify({"response": ai_message})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)