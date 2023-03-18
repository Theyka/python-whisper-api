## Prerequisites

* [Python 3.10](https://www.python.org/)
* [FFmpeg](https://ffmpeg.org/download.html)
* [Whisper](https://github.com/openai/whisper)

## Installation

1. Download [Python 3.10](https://www.python.org/), [FFmpeg](https://ffmpeg.org/download.html) and [Whisper](https://github.com/openai/whisper) ``pip install git+https://github.com/openai/whisper.git``

2. Clone the repo
   ```
   git clone https://github.com/Theyka/python-whisper-api.git
   ```
3. Install python libraries
   ```
   pip install -r requirements.txt
   ```
4. Start python code
   ```
   python main.py
   ```

## Usage

```
import requests

with open('audio.mp3', 'rb') as f:
    r = requests.post('http://localhost/whisper', files={'audio': f})
    print(r.text)
```
