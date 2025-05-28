from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key =""

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    summary = data.get('summary', '')
    description = data.get('description', '')

    prompt = f"""You are a risk analyst.
Given this Jira issue summary and description, identify any technical or security risks.

Summary: {summary}
Description: {description}

Provide a one-paragraph risk analysis:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if enabled
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=200
        )
        risk_text = response['choices'][0]['message']['content']
        return jsonify({"risk": risk_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
