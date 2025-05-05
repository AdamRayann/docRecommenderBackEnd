from flask import Flask, request, jsonify
from flask_cors import CORS
import docxToSen
from aiRecommendation import analyze_medical_text

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file or not file.filename.endswith('.docx'):
        return jsonify({'error': 'Invalid file'}), 400

    try:
        extracted_text = docxToSen.read_docx(file)
        gpt_reply = analyze_medical_text(extracted_text)
        return jsonify({'text': gpt_reply})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5050)