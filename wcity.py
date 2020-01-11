
import requests
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
        if request.method == 'GET':
                index = request.args.get('index')
        if index == None or index == '':
                index = 'Mumbai'

        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ index +'&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1').json()
        print(req)

        description = req['weather'][0]['description'].upper()
        temperature = req['main']['temp']
        icon = req['weather'][0]['icon']
        icon = 'https://openweathermap.org/img/w/'+ icon +'.png'

        return render_template('index.html', index = index, description = description, temperature = temperature, icon = icon)
if __name__ == '__main__':
   app.run()
