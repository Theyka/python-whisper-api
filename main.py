from flask import Flask, request
from tempfile import NamedTemporaryFile
from hypercorn.config import Config
from hypercorn.asyncio import serve
import whisper
import asyncio


model = whisper.load_model("tiny")
app = Flask(__name__)


@app.route("/")
def index():
    return """
    
Use /whisper endpoint for api\nExample:

<pre>
import requests

with open('audio.mp3', 'rb') as f:
    r = requests.post('http://45.95.214.151/whisper', files={'audio': f})
    print(r.text)
</pre>
"""

@app.route('/whisper', methods=['POST'])
def whisper_api():
    if not request.files:
        return "{'error': 'audio file not found'}"

    handle = request.files['audio']
    temp = NamedTemporaryFile()
    handle.save(temp)
    result = model.transcribe(temp.name)

    return {'output': result['text']}


if __name__ == "__main__":
    config = Config()
    config.bind = "0.0.0.0:80"
    asyncio.run(serve(app, config=config))
