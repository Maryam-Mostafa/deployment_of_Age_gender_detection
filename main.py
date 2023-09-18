from flask import Flask, request, jsonify
import numpy as np
from deepface import DeepFace

app = Flask(__name__)


@app.route('/', methods=['POST'])
def detect_age_gender():
    try:
        # Get the base64-encoded image data from the JSON data
        data = request.json
        if 'image' not in data:
            return jsonify({"error": "No base64-encoded image data found"})

        # read the base64 image data
        image_base64 = data['image']

        # Use age and gender detection model to predict age and gender
        age, gender = predict_age_gender(image_base64)

        # Return the results as a JSON object
        print(age, gender)
        result = {"age": age, "gender": gender}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


def predict_age_gender(image):
    info = DeepFace.analyze(img_path=image, detector_backend='yunet',
                            enforce_detection=False, actions=['age', 'gender'])
    if info:
        age = info[0]['age']
        gender = info[0]['dominant_gender']

    else:
        # incase no faces
        age = "no age detected"
        gender = "no gender detected"

    return age, gender


if __name__ == '__main__':
    app.run(debug=True)
