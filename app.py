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
    
    elif "empadronamiento" in user_input or "empadronar" in user_input:
        return jsonify({
            "response": (
               "Para empadronarte en Salamanca, acude a la Oficina de Atención Ciudadana en la Calle Íscar Peyra 24. "
               "Puedes pedir cita o más info en: https://www.aytosalamanca.es/es/tramitesgestiones/empadronamiento/"
            )
        })
    
    elif "autobús" in user_input or "bus" in user_input or "transporte" in user_input:
        return jsonify({
            "response": (
                "Puedes consultar los horarios y líneas de autobuses urbanos de Salamanca en: https://www.tussalamanca.es/"
            )
        })
    
    elif "hospital" in user_input or "urgencia" in user_input or "salud" in user_input:
        return jsonify({
            "response": (
                "El Hospital Universitario de Salamanca está en Paseo de San Vicente, 182. "
                "Para consultas o citas, visita: https://www.saludcastillayleon.es/"
            )
        })
    
    elif "votar" in user_input or "elecciones" in user_input:
        return jsonify({
            "response": (
                "Puedes consultar tu colegio electoral en la web del INE: https://sede.ine.gob.es/. "
                "O contacta con tu ayuntamiento para más detalles."
            )
        })
    elif "ayuntamiento" in user_input or "contactar" in user_input:
        return jsonify({
            "response": (
                "Puedes contactar con el Ayuntamiento de Salamanca en el 923 279 100 o en: https://www.aytosalamanca.es/"
            )
        })
    
    elif "ayuntamiento" in user_input or "contactar" in user_input:
        return jsonify({
            "response": (
                "Puedes contactar con el Ayuntamiento de Salamanca en el 923 279 100 o en: https://www.aytosalamanca.es/"
            )
        })

    






    return jsonify({
        "response": "Por ahora solo puedo informarte sobre farmacias de guardia. Pronto sabré más cosas."
    })

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
