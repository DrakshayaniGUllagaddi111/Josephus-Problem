from flask import Flask, jsonify, render_template, request
import google.generativeai as genai
import os

# Flask app initialization
app = Flask(__name__)

# Set and configure the API key for Google Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyCVz5MeOFQpZX-Vb4IrDB7gL1-vCfqzgLg"  # Replace with your actual key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/')
def home():
    return render_template("chatbot.html")  # This should match your HTML filename in the templates folder

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({"response": "Please send a valid message."}), 400

        # Call Gemini
        response = model.generate_content(user_message)

        if response and response.text:
            ai_reply = response.text.strip()
        else:
            ai_reply = "No response received from Gemini."

        return jsonify({"response": ai_reply}), 200

    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
