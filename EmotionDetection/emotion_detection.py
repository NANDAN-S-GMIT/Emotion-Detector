import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Input text is empty or invalid.'
        }

    text = text_to_analyze.lower()
    # Enhanced keyword-based logic with emoji
    if any(word in text for word in ['happy', 'joy', 'glad', 'delighted', 'joyful', 'pleased', 'excited']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.97, 'sadness': 0.01, 'dominant_emotion': 'joy', 'emoji': '😀'}
    elif any(word in text for word in ['sad', 'unhappy', 'depressed', 'alone', 'cry', 'down']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.97, 'dominant_emotion': 'sadness', 'emoji': '😢'}
    elif any(word in text for word in ['angry', 'mad', 'furious', 'rage', 'irritated']):
        return {'anger': 0.97, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'anger', 'emoji': '😠'}
    elif any(word in text for word in ['disgust', 'disgusted', 'gross', 'nausea', 'revolted']):
        return {'anger': 0.01, 'disgust': 0.97, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'disgust', 'emoji': '🤢'}
    elif any(word in text for word in ['fear', 'scared', 'afraid', 'terrified', 'frightened']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.97, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'fear', 'emoji': '😨'}
    elif any(word in text for word in ['love', 'loved', 'loving', 'adore', 'adorable']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.97, 'sadness': 0.01, 'dominant_emotion': 'love', 'emoji': '😍'}
    elif any(word in text for word in ['amuse', 'amused', 'amusing', 'funny', 'hilarious', 'laugh', 'lol']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.97, 'sadness': 0.01, 'dominant_emotion': 'amusement', 'emoji': '😂'}
    elif any(word in text for word in ['confused', 'confusing', 'confusion', 'puzzled', 'uncertain']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'confusion', 'emoji': '😕'}
    elif any(word in text for word in ['neutral', 'ok', 'fine', 'okay', 'normal', 'average']):
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'neutral', 'emoji': '😐'}
    else:
        # Neutral or unknown
        return {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'neutral', 'emoji': '😐'}
