from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para permitir acceso desde tu web

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()

    # Lógica simple
    if "farmacia" in user_input or "guardia" in user_input:
        return jsonify({
            "response": "La farmacia de guardia hoy en Salamanca es Farmacia Central (Calle Toro, 22). Abierta 24h."
        })
    elif "eventos" in user_input or "agenda" in user_input:
        return jsonify({
            "response": (
                "Aquí tienes algunas fuentes donde puedes consultar los eventos culturales "
                "en la provincia de Salamanca:\n\n"
                "🎭 Salamanca Vivela: https://salamancavivela.es/agenda/\n"
                "🎶 Salamancalia: https://www.salamancalia.es/\n"
                "📣 Facebook (alternativos): https://www.facebook.com/groups/392811704077155/\n\n"
                "Pronto te podré decir directamente qué hay hoy 😉"
            )
        })



    return jsonify({
        "response": "Por ahora solo puedo informarte sobre farmacias de guardia. Pronto sabré más cosas."
    })

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
