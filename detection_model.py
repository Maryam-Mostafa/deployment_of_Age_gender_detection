import numpy as np
from deepface import DeepFace


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

    return {"data": {"age": age, "gender": gender}, "state": "OK"}
