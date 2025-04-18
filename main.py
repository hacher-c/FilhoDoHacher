from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Olá! Eu sou o Filho do Hacher. 😎 Estou pronto pra rodar 24h no ar!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Recebido:", data)

    # Simples resposta automática
    resposta = {
        "message": {
            "text": "Olá! Tudo bem? Eu sou o Filho do Hacher, seu bot de quizzes de anime! 😁"
        }
    }
    return resposta, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
