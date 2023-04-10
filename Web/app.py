from flask import Flask, render_template, request, send_file
from pymongo import MongoClient
from bson import ObjectId
import gridfs
from bson.son import SON

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['project']
posts = db['posts']
fs = gridfs.GridFS(db)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search_posts', methods=['POST'])
def search_posts():
    query = request.form.get('query')
    field = request.form.get('field')
    results = []

    if field == 'description':
        regex_query = { "$regex": ".*" + query + ".*", "$options": "i" }
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
    post = db.posts.find_one({ 'post_id': post_id })
    if post:
        filename = 'test/' + str(post_id) + '.jpg'
        image = fs.find_one({"filename": filename})
        if image:
            return render_template('post.html', post=post, image=image)
        else:
            return render_template('post.html', post=post)
    else:
        return "Post not found."


@app.route('/download_image/<image_id>')
def download_image(image_id):
    image = fs.get(ObjectId(image_id))
    return send_file(image, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)
