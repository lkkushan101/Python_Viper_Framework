import requests

def compareImages(file_sourcename, filedestination_name, api_key):

    r = requests.post(
        "https://api.deepai.org/api/image-similarity",
        files={
            'image1': open(file_sourcename, 'rb'),
            'image2': open(filedestination_name, 'rb'),
        },
        headers={'api-key': api_key}
    )
    return r.json()

