from flask import Flask, request, jsonify, render_template
import os
import subprocess

app = Flask(__name__)

if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)

        file_details = {
            'filename': uploaded_file.filename,
            'content_type': uploaded_file.content_type,
            'size': os.path.getsize(file_path)
        }

        file_details['file_type'] = subprocess.getoutput(f'type {file_path}')

        os.remove(file_path)

        return render_template('index.html', file_details=file_details)
    else:
        return "No file uploaded", 400

if __name__ == '__main__':
    app.run(debug=True)
