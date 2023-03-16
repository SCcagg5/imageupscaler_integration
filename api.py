import base64
import requests
from bottle import Bottle, request

app = Bottle()

@app.route('/upload', method='POST')
def upload():
    file_data = base64.b64decode(request.forms.get('myfile'))
    file_name = request.forms.get('fileName')
#     scale_radio = request.forms.get('scaleRadio')

    # Send a POST request to the Node.js endpoint with the binary data and scale radio
    response = requests.post('https://access.imglarger.com:8998/upload',
                             headers={
                                 'Content-Type': 'application/json'
                             },
                             json={
                                 'fileData': file_data,
                                 'fileName': file_name,
                                 'scaleRadio': 2
                             })

    # Return the response from the Node.js endpoint
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
