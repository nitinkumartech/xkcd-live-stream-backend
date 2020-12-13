import xkcd
from flask import Flask
app = Flask(__name__)


@app.route('/getRandomXkcdLink')
def hello():
    random = xkcd.getRandomComic()
    response = { "imageLink": random.getImageLink(), "imageTitle": random.getTitle(), "altText": random.getAltText()}
    return response

if __name__ == '__main__':
    app.run()