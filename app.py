from flask import Flask, render_template, request, jsonify
from chatbot import ask_question

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        question = request.json.get("question", "")
        answer = ask_question(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
