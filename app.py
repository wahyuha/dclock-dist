import os
from flask import Flask, render_template, send_from_directory

template_dir = os.path.abspath('build')
app = Flask(__name__, template_folder=template_dir, static_folder=os.path.join(template_dir, '_app'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/_app/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run()
