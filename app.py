from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    user_input = request.form['userInput']
    with open('input.txt', 'w') as file:
        file.write(user_input)
    return 'Input saved to input.txt'

if __name__ == '__main__':
    app.run(debug=True)
