from flask import Flask, render_template, request, jsonify
from chatbot.model import generate_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.form.get("message", "").strip()

    if not user_text:
        return jsonify({"response": "Por favor escribe algo 😅"})

    system_prompt = (
        "Eres un asistente útil, claro y educado. "
        "Responde en español de forma concisa."
    )

    response = generate_response(
        user_text=user_text,
        system_prompt=system_prompt
    )

    return jsonify({"response": response})


# 🔹 SOLO se ejecuta en local
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
