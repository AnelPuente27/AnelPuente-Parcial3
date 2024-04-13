from flask import Flask, jsonify, request
import pywhatkit

app = Flask(__name__)

tasks = [
    {"id":  1, "name":"Anel", "enable": True},
    {"id":  2, "name":"Masita", "enable": False},
    {"id":  3, "name":"Rango", "enable": False},
    {"id":  4, "name":"Zero", "enable": False},
]

@app.route('/whatapp-message', methods=['GET', 'POST'])
def whatsapp_example():
    # handle the POST request
    if request.method == 'POST':
        data = request.get_json()
        if 'message' in data:
            message = data['message']
            try:
                pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", message)
                return 'message sended sucessfully to group', 200
            except Exception as e:
                print("Error:", e)
                return 'Error sending message', 500
        else:
            return 'Message not found in request body', 400

if __name__ == '__main__':
    app.run(debug=True)