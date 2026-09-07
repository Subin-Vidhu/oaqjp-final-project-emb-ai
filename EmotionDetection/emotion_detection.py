"""
This module contains a function to detect emotions in a given text
using the Watson NLP Emotion Predict function, and returns a formatted
dictionary of emotion scores along with the dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Sends the input text to the Watson NLP Emotion Predict API,
    parses the response, and returns a dictionary containing the
    scores for anger, disgust, fear, joy, sadness, and the dominant
    emotion.
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime'
           '.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
# """
# This module contains a function to detect emotions in a given text
# using the Watson NLP Emotion Predict function.
# """

# import requests


# def emotion_detector(text_to_analyze):
#     """
#     Sends the input text to the Watson NLP Emotion Predict API
#     and returns the raw response text.
#     """
#     url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime'
#            '.nlp.v1/NlpService/EmotionPredict')
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input_json = {"raw_document": {"text": text_to_analyze}}

#     response = requests.post(url, json=input_json, headers=headers, timeout=10)

#     return response.text