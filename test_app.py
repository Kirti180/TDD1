from app import app
import json

def test_get_weather():
    client = app.test_client()

    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    assert response.get_json() == {'temperature': 14, 'weather': 'Cloudy'}

    response = client.get('/weather/Seattle')
    assert response.status_code == 200
    assert response.get_json() == {'temperature': 10, 'weather': 'Rainy'}

    response = client.get('/weather/Paris')
    assert response.status_code == 404
    assert response.get_json() == {'error': 'City not found'}

def test_add_weather():
    client = app.test_client()

    data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'}
    response = client.post('/weather', json=data)
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Weather data added successfully'}

    response = client.get('/weather/Chicago')
    assert response.status_code == 200
    assert response.get_json() == {'temperature': 18, 'weather': 'Cloudy'}

def test_update_weather():
    client = app.test_client()

    data = {'temperature': 25}
    response = client.put('/weather/New York', json=data)
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Weather data updated successfully'}

    response = client.get('/weather/New York')
    assert response.status_code == 200
    assert response.get_json() == {'temperature': 25, 'weather': 'Sunny'}

def test_delete_weather():
    client = app.test_client()

    response = client.delete('/weather/Austin')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Weather data deleted successfully'}

    response = client.get('/weather/Austin')
    assert response.status_code == 404
    assert response.get_json() == {'error': 'City not found'}
