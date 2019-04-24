from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',no&units=metric&appid=2bb13bbb7d94a5f0e82e32c9d5691ed8')
    json_object = r.json()
    temp = float(json_object['main']['temp'])
    return render_template('temperature.html', temp=temp)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

