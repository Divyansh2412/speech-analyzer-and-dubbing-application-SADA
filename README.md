# 🎙️ Speech Analyzer and Dubbing Application (SADA)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat)](../../issues)

## 📌 Overview
**SADA** is an AI-powered application that analyzes speech, transcribes it, and provides dubbing in multiple languages.  
It can process audio from microphone input or pre-recorded files, perform speech-to-text conversion, translate the text into a chosen language, and synthesize speech for dubbing.


## 🚀 Features
- **Speech Recognition** – Converts spoken audio into text.
- **Language Translation** – Supports multiple target languages.
- **Speech Synthesis (Dubbing)** – Generates high-quality audio output in the selected language.
- **Audio File Support** – Works with both live microphone input and uploaded audio files.
- **User-friendly Interface** – Simple and interactive design.
- **Modular Design** – Easy to extend with new languages or features.

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Divyansh2412/speech-analyzer-and-dubbing-application-SADA.git
cd speech-analyzer-and-dubbing-application-SADA
````

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the application:

```bash
python main.py
```

If the project has a web UI:

```bash
python app.py
```

Then open **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.

---

## 📂 Project Structure

```
SADA/
├── main.py                 # Main application logic
├── app.py                  # Flask web interface (if applicable)
├── modules/                # Supporting Python modules
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates for Flask
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📌 Requirements

Example dependencies (update based on actual imports in the project):

```
speechrecognition
pydub
gtts
pyaudio
googletrans==4.0.0-rc1
numpy
scipy
librosa
flask
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Author

**Divyansh Miyan Bazaz**

* GitHub: [@Divyansh2412](https://github.com/Divyansh2412)
* Email: [dmiyanbazaz@gmail.com](mailto:dmiyanbazaz@gmail.com)

````

---

## **📄 LICENSE (MIT License)**
Create a file named `LICENSE` and paste:
```text
MIT License

Copyright (c) 2025 Divyansh Miyan Bazaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
````

---

