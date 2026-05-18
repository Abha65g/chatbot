from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load dataset
df = pd.read_csv("medical_data.csv")

# Configure Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Search medical dataset
def get_medical_context(user_input):

    user_input = user_input.lower()

    for index, row in df.iterrows():

        question = str(row["Question"]).lower()

        if any(word in question for word in user_input.split()):

            return str(row["Answer"])

    return "No exact medical information found."


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

        # Get dataset context
        context = get_medical_context(user_input)

        # Generate AI response
        chat_completion = client.chat.completions.create(

            messages=[

                {
                    "role": "system",
                    "content": f"""
                    You are MediCare AI Assistant.

                    Use this medical information:

                    {context}

                    Instructions:
                    - Keep answers short
                    - Maximum 100 words
                    - Use bullet points
                    - Use simple English
                    - Add line breaks
                    - Avoid long paragraphs
                    - Mention doctor consultation for serious conditions
                    """
                },

                {
                    "role": "user",
                    "content": user_input,
                }

            ],

            model="llama-3.1-8b-instant",

            temperature=0.4,
            max_tokens=180

        )

        ai_message = chat_completion.choices[0].message.content

        return jsonify({"response": ai_message})

    except Exception as e:

        return jsonify({"error": str(e)})


# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)