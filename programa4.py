from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":  1, "name":"Anel", "enable": True},
    {"id":  2, "name":"Masita", "enable": False},
    {"id":  3, "name":"Rango", "enable": False},
    {"id":  4, "name":"Zero", "enable": False},
]

@app.route('/tasks' , methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)