import base64
import json
import os

import flask
from flask import request

import detection


app = flask.Flask(__name__)
def decode_b64(image):
    decoded_data = base64.b64decode(json.loads(image)["data"])
    return decoded_data
def encode_b64(image):
    with open(image, "rb") as f:
        encoded_data = base64.b64encode(f.read())
        f.close()
        return encoded_data

@app.route('/', methods=['GET'])
def handle_call():
    return "Successfully Connected"

@app.route('/getimage', methods=['POST'])
def process_image():

    # Try and get the Base64-encoded image data from the request body
    try:
        decoded_data = decode_b64(request.get_data())
        filename = 'decoded_image.jpg'
        test = 'final_image.jpg'
        with open(filename, 'wb') as f:
            f.write(decoded_data)
            f.close()
        detection.detect(detection.detection_graph, filename, test)

    # Throw exception if decoded_data is empty.
    except(decoded_data is None):
        print("Cannot process empty image data.")

    # If code runs with no issues, remove original image.
    else:
        print("Successfully decoded image from base64!")
        annotated_image = encode_b64(test)
        os.remove(filename)
        os.remove(test)
    return annotated_image

#this commands the script to run in the given port
if __name__ == "__main__":

    print('Starting the API')
    app.run(host="0.0.0.0", port=5000, debug=True)
