from flask import Flask, request, jsonify
from detection_model import predict_age_gender

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
        result = predict_age_gender(image_base64)

        # Return the results as a JSON object
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
