import xkcd
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/getRandomXkcdLink')
def hello():
    random = xkcd.getRandomComic()
    response = { "imageLink": random.getImageLink(), "imageTitle": random.getTitle(), "altText": random.getAltText()}
    return json.dumps(response)

if __name__ == '__main__':
    app.run()
