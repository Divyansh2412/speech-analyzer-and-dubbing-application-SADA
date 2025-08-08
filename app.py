# app.py

from flask import Flask, render_template, request, redirect, url_for
import speech_translation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():
    audio = speech_translation.record_audio()  # Record speech
    english_text = speech_translation.speech_to_text(audio)
    return redirect(url_for('result', text=english_text))

@app.route('/result')
def result():
    text = request.args.get('text', '')
    languages = {
        'Spanish': 'es', 'French': 'fr', 'German': 'de',
        'Chinese': 'zh-cn', 'Japanese': 'ja', 'Russian': 'ru',
        'Hindi': 'hi', 'Arabic': 'ar', 'Portuguese': 'pt', 'Italian': 'it'
    }
    return render_template('result.html', text=text, languages=languages)

@app.route('/translate', methods=['POST'])
def translate():
    language = request.form['language']
    text = request.form['text']
    speech_translation.translate_and_generate_speech(text, language)
    return redirect(url_for('result', text=text))

if __name__ == "__main__":
    app.run(debug=True)
