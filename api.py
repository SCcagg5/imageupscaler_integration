import requests
import base64

# Décode le fichier en base64
def decode_base64_file(file):
    decoded_file = base64.b64decode(file)
    return decoded_file

def upscale(file):
    TOKEN = os.environ.get('TOKEN')

    # Créer un nom de fichier unique en utilisant uuid
    filename = f"test-{uuid.uuid4()}.png"

    # Enregistrer le fichier sur le disque
    with open(filename, 'wb') as f:
        f.write(decode_base64_file(file))

    with open(filename, 'rb') as f:
        response = requests.post(
            'https://imageupscaler.com/api/update_image.php?method=upscale-image-4x',
            files={'file_image': f},
            headers={'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'Mozilla/5.0'},
        )

    # Supprimer le fichier après l'avoir utilisé
    os.remove(filename)

    if response.status_code == requests.codes.ok and response.json()["success"] == True:
        url = response.json()["processes_image"]
        return url
    else:
        response.status = response.status_code
        return {"error": f"{response.status_code}: {json.dumps(response.json()['error'])}"}

app = Bottle()

@app.post('/upscale')
def upscale_image():
    # Lire le fichier en base64
    file = request.forms.get('file')
    result = upscale(file)
    if isinstance(result, bytes):
        response.set_header('Content-Type', 'image/png')
        response.set_header('Content-Length', len(result))
        response.set_header('Accept-Ranges', 'bytes')
        return result
    else:
        if 'error' in result:
            response.status = 500  # Internal Server Error
        return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
