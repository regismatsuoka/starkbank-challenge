import starkbank
from flask import jsonify, request
from flask import Blueprint
from services.starkbank_api_service import generate_invoices
from models.invoice_model import Invoice
from config import settings
import json
from pydantic import ValidationError


starkbank_api_bp = Blueprint('starkbank_api', __name__)

@starkbank_api_bp.route('/api/invoice', methods=['POST'])
def send_invoice():
    credentials = settings.get_credentials()
    
    project = starkbank.Project(environment=credentials["environment"],
                                id=credentials["id"],
                                private_key=credentials["key"])
    starkbank.user = project 
    starkbank.language = "pt-BR"

    try:
        invoice_data = request.get_json()
        if not invoice_data:
            return jsonify({"error": "Dados para geração de invoice não foram fornecidos."}), 400
        
        valid, result = validate_data(invoice_data)
        if not valid:
             return jsonify({"error": result}), 400

        response = generate_invoices(result)

        return jsonify({"content" : str(response[0])}), 200
    
    except Exception as e:
        return jsonify({"error" :  str(e)}), 500


def validate_data(data):
    try:
        invoice_validada = Invoice(**data)
        if str(type(invoice_validada.due) == "list"): invoice_validada.due= invoice_validada.due[0]
        invoice_json = json.loads(json.dumps(invoice_validada.model_dump()))
        return True, invoice_json
    except ValidationError as e:
        return False, e