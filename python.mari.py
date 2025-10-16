from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Bem-vindo ao exemplo de HTML com Python!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)