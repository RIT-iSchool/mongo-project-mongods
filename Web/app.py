from flask import Flask, render_template, request, send_file, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
import gridfs

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mongoproject']
posts = db['posts']
fs = gridfs.GridFS(db)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search_posts', methods=['GET', 'POST'])
def search_posts():
    query = request.form.get('query')
    field = request.form.get('field')
    results = []
    if field == 'description':
        regex_query = { "$regex": "\\b" + query + ".*\\b", "$options": "i" }
        results = list(db.posts.find({ "description": regex_query }))
    elif field == 'postLoc':
        lat, lng, distance_in_meters = [float(x) for x in query.split(',')]
        location_query = {
            "postLoc": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [lat, lng]
                    },
                    "$maxDistance": distance_in_meters
                }
            }
        }
        results = list(db.GeoPosts.find(location_query))

    return render_template('results.html', posts=results)


@app.route('/show_post/<post_id>')
def show_post(post_id):
    comments = db.comments.find({'post_id': post_id})
    post = db.posts.find_one({ 'post_id': post_id })
    if post:
        filename = 'images/test/' + str(post_id) + '.jpg'
        image = fs.find_one({"filename": filename})
        if image:
            return render_template('post.html', post=post, image=image, comments=comments)
        else:
            return render_template('post.html', post=post)
    else:
        return "Post not found."


@app.route('/download_image/<image_id>')
def download_image(image_id):
    image = fs.get(ObjectId(image_id))
    return send_file(image, mimetype='image/jpg')

@app.route('/add_comment/<post_id>', methods=['POST'])
def add_comment(post_id):
    username = request.form.get('username')
    comment_text = request.form.get('comment')
    comment = {'post_id': post_id, 'text': comment_text, 'username': username}
    db.comments.insert_one(comment)
    return redirect(url_for('show_post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
