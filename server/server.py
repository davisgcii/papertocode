from flask import Flask, render_template, request

app = Flask(__name__)

# Route to serve the HTML page with the text form
@app.route('/')
def form():
    return '''
        <!DOCTYPE html>
        <html>
          <head>
            <title>Text Form</title>
          </head>
          <body>
            <h1>Enter the Arxiv Paper's url</h1>
            <form action="/api/endpoint" method="post">
              <label for="text-input">url:</label><br>
              <input type="text" id="text-input" name="text"><br><br>
              <input type="submit" value="Submit">
            </form>
          </body>
        </html>
    '''

# Route to handle the form submission and send the text to the API endpoint
@app.route('/api/endpoint', methods=['POST'])
def process_text():
    text = request.form['text']
    # Send the text to the API endpoint
    # ...
    return f'Thanks for submitting: {text}'

if __name__ == '__main__':
    app.run(debug=True)
