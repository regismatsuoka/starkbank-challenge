
from flask import Flask
from flask_cors import CORS
from controllers import starkbank_api_controller, webhook_controller

app = Flask(__name__)
CORS(app)

app.register_blueprint(webhook_controller.webhook_bp)
app.register_blueprint(starkbank_api_controller.starkbank_api_bp)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(e)
