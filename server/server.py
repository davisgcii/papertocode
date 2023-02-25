from flask import Flask, request

app = Flask(__name__)

@app.route('/api/paperurl', methods=['POST'])
def endpoint():
    text = request.get_data(as_text=True)
    return f"You sent: {text}"

if __name__ == '__main__':
    app.run(debug=True)
