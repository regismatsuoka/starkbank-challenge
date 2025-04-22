import json
import starkbank
import os
from flask import jsonify, request
from flask import Blueprint
from datetime import datetime
from config import settings
from services.starkbank_webhook import starkbank_transfer


webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/api/webhook', methods=['POST'])
def webhook_receiver():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Nenhum dado recebido."}), 400
            
        credentials = settings.get_credentials()
        
        project = starkbank.Project(environment=credentials["environment"],
                                    id=credentials["id"],
                                    private_key=credentials["key"])
        starkbank.user = project 
        starkbank.language = "pt-BR"
        
        try:

            webhook_data = starkbank.event.parse(
                content=request.data.decode("utf-8"),
                signature=request.headers["Digital-Signature"],
            )

            log_data(data)

            if data["event"]["subscription"] == "invoice":
                starkbank_transfer(data)

            return jsonify({
                "status": "success",
                "message": "OK",
                "data": data
            }), 200
        except Exception as e:
            return jsonify({
                "status": "failed",
                "message": "Error processing webhook call",
                "data": data
            }), 500
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def log_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    log_directory = "logs"
    
    if not os.path.exists(log_directory):
            os.makedirs(log_directory) 
    
    filename = os.path.join(log_directory, f"webhook_data_{timestamp}.json")
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
