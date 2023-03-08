import requests

API_URL = 'http://api:8080'

def test_upscale_image():
    with open('test_image.png', 'rb') as f:
        response = requests.post(f'{API_URL}/upscale', files={'file': f})
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'image/png'
