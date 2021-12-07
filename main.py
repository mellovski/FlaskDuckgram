from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)
address = "http://127.0.0.1:5000/"

webbrowser.open(address)

@app.route('/', methods=['GET', 'POST'])
def primeiro():
    return render_template('index.html')

@app.route('/feed', methods=['GET', 'POST'])
def segundo():
    return render_template('resposta.html', username=request.form['username'], password=request.form['password'])

@app.route('/shutdown', methods=['GET', 'POST'])
def terceiro():
    webbrowser.open("https://google.com")
    request.environ.get('werkzeug.server.shutdown')
    return 'Duckgram has too many ducks, try Google...'

if __name__ == "__main__":
    app.run()