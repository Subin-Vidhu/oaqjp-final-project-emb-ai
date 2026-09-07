"""
This module contains a function to detect emotions in a given text
using the Watson NLP Emotion Predict function, and returns a formatted
dictionary of emotion scores along with the dominant emotion. Handles
blank input by returning None values.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Sends the input text to the Watson NLP Emotion Predict API,
    parses the response, and returns a dictionary containing the
    scores for anger, disgust, fear, joy, sadness, and the dominant
    emotion. Returns all None values if the input is blank
    (status_code 400).
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime'
           '.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    emotion_scores = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores