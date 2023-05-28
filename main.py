from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/<name>')
def main(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    sex = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    return render_template('index.html', name = name, age = age, sex = sex)

if __name__ == '__main__':
    app.run(debug = True)