from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['project']
posts = db['posts']

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search_posts', methods=['POST'])
def search_posts():
    query = request.form.get('query')
    regex_query = { "$regex": ".*" + query + ".*", "$options": "i" }
    results = list(db.posts.find({ "description": regex_query }))
    return render_template('results.html', posts=results)

if __name__ == '__main__':
    app.run(debug=True)
