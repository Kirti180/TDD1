from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather', methods=['POST'])
def add_weather():
    data = request.get_json()
    city = data.get('city')
    temperature = data.get('temperature')
    weather = data.get('weather')

    if city and temperature and weather:
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        return jsonify({'message': 'Weather data added successfully'})
    else:
        return jsonify({'error': 'Invalid payload'}), 400

@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    if city in weather_data:
        data = request.get_json()
        temperature = data.get('temperature')
        weather = data.get('weather')

        if temperature:
            weather_data[city]['temperature'] = temperature
        if weather:
            weather_data[city]['weather'] = weather

        return jsonify({'message': 'Weather data updated successfully'})
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': 'Weather data deleted successfully'})
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run()
