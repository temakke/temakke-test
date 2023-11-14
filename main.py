import gnews
from gnews import GNews

from flask import Flask
from flask import jsonify

app = Flask(__name__)

google_news = GNews(language='pt', country='BR', period='7d', start_date=None, end_date=None, max_results=10)

s_m = google_news.get_news('sociedademilitar.com')

@app.route('/', methods=['GET'])
def view_news():
    return jsonify(s_m)