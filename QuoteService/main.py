from flask import Flask
from flask import jsonify
import random

QUOTES_FILE = "./quotes.txt" # quote file
quotes = [] # stores all quotes

# a quote
class Quote(object):
    def __init__(self, quote, by):
        self.quote = quote
        self.by = by

# Loads quotes from a file
def loadQuotes():
    with open(QUOTES_FILE) as file:
        lines = file.readlines()
        lines = [x.strip() for x in lines] 
        for line in lines:
            quote, by = line.split("-")
            quotes.append(Quote(quote, by))
            
app = Flask(__name__)

# Gets a random quote 
@app.route("/api/quote")
def quote():
    q = random.choice(quotes) # selects a random quote from file
    return jsonify({"quote": q.quote, "by": q.by}) # return a quote

# 404 Erorr for unknown routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Resource not found"}), 404

if __name__ == '__main__':
    loadQuotes() # load quotes 
    app.run(host='0.0.0.0', port=5000, debug=True) # run application
    