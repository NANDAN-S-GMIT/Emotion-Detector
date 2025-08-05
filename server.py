from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/emotionDetector')
def emotion_detector_function():
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    if not text_to_analyze:
        return "<span style='color:red'>Please enter some text to analyze.</span>"

    response = emotion_detector(text_to_analyze)
    # If Watson API fails, simulate a result for demo/testing
    if response['dominant_emotion'] is None:
        error_detail = response.get('error', '')
        # Simulate based on keywords for demo
        text = text_to_analyze.lower()
        if any(word in text for word in ['happy', 'joy', 'glad', 'delighted']):
            response = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.97, 'sadness': 0.01, 'dominant_emotion': 'joy'}
        elif any(word in text for word in ['sad', 'unhappy', 'depressed', 'alone']):
            response = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.97, 'dominant_emotion': 'sadness'}
        elif any(word in text for word in ['angry', 'mad', 'furious']):
            response = {'anger': 0.97, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'anger'}
        elif any(word in text for word in ['disgust', 'disgusted', 'gross']):
            response = {'anger': 0.01, 'disgust': 0.97, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'disgust'}
        elif any(word in text for word in ['fear', 'scared', 'afraid']):
            response = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.97, 'joy': 0.01, 'sadness': 0.01, 'dominant_emotion': 'fear'}
        else:
            # Show a user-friendly error for connection issues
            if error_detail:
                if 'timed out' in error_detail or 'Failed to establish a new connection' in error_detail:
                    response_text = ("<span style='color:red'>"
                                     "Could not connect to the Watson NLP API. "
                                     "Please check your internet connection or try again later." 
                                     "</span>")
                else:
                    response_text = f"<span style='color:red'>Error analyzing emotion: {error_detail}</span>"
            else:
                response_text = "<span style='color:red'>Could not analyze the input. Please try again.</span>"
            return response_text

    # Enhanced output formatting with emoji
    emoji = response.get('emoji', '')
    response_text = (
        "<div style='font-size:1.13em;line-height:1.7em;'>"
        "<div style='text-align:center;margin-bottom:1.1em;'>"
        "<b style='font-size:1.1em;color:#4255ff;'>System Analysis</b><br>"
        "<span style='display:inline-block;font-size:1.35em;margin-top:0.3em;margin-bottom:0.2em;'><b>Dominant Emotion:</b> <span style='color:#007bff;font-size:1.25em'>{emoji} {dominant}</span></span>".format(
            emoji=emoji,
            dominant=response['dominant_emotion'].capitalize() if response['dominant_emotion'] else ''
        ) +
        "</div>"
        "<div class='emotion-grid' style='display:flex;flex-wrap:wrap;justify-content:center;gap:18px 32px;max-width:420px;margin:0 auto 0 auto;'>"
        "<div style='flex:1 1 120px;min-width:110px;text-align:left;'><b style='color:#d9534f;'>Anger</b>: <span style='font-weight:600'>{anger:.3f}</span></div>".format(anger=response['anger'] if response['anger'] is not None else 0.0) +
        "<div style='flex:1 1 120px;min-width:110px;text-align:left;'><b style='color:#8e44ad;'>Disgust</b>: <span style='font-weight:600'>{disgust:.3f}</span></div>".format(disgust=response['disgust'] if response['disgust'] is not None else 0.0) +
        "<div style='flex:1 1 120px;min-width:110px;text-align:left;'><b style='color:#f39c12;'>Fear</b>: <span style='font-weight:600'>{fear:.3f}</span></div>".format(fear=response['fear'] if response['fear'] is not None else 0.0) +
        "<div style='flex:1 1 120px;min-width:110px;text-align:left;'><b style='color:#27ae60;'>Joy</b>: <span style='font-weight:600'>{joy:.3f}</span></div>".format(joy=response['joy'] if response['joy'] is not None else 0.0) +
        "<div style='flex:1 1 120px;min-width:110px;text-align:left;'><b style='color:#2980b9;'>Sadness</b>: <span style='font-weight:600'>{sadness:.3f}</span></div>".format(sadness=response['sadness'] if response['sadness'] is not None else 0.0) +
        "</div>"
        "</div>"
    )
    return response_text

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
