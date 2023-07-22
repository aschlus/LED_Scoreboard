from flask import Flask, request

def start_server(server_socket):
    print("Starting Server...")
    app = Flask(__name__)

    @app.route("/data", methods=['GET'])
    def home():
        print("Received Post")
        return "Received Post"
    
    app.run(host='127.0.0.1', port=5000)
