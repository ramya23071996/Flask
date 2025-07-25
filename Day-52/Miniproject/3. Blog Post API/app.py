from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

posts = {}  # Simulated in-memory DB

# Parser for validating input
post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help="Title is required")
post_parser.add_argument('content', type=str, required=True, help="Content is required")
post_parser.add_argument('author', type=str, required=False)

class PostListResource(Resource):
    def get(self):
        return list(posts.values()), 200

    def post(self):
        args = post_parser.parse_args()
        post_id = len(posts) + 1
        new_post = {
            "id": post_id,
            "title": args['title'],
            "content": args['content'],
            "author": args.get('author', "Anonymous")
        }
        posts[post_id] = new_post
        return new_post, 201

class PostResource(Resource):
    def get(self, post_id):
        post = posts.get(post_id)
        if not post:
            return {"message": "Post not found"}, 404
        return post, 200

    def put(self, post_id):
        post = posts.get(post_id)
        if not post:
            return {"message": "Post not found"}, 404
        args = post_parser.parse_args()
        post['title'] = args['title']
        post['content'] = args['content']
        post['author'] = args.get('author', post['author'])
        return post, 200

    def delete(self, post_id):
        if post_id not in posts:
            return {"message": "Post not found"}, 404
        del posts[post_id]
        return {"message": "Post deleted"}, 204

# Route registration
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')

# Optional 500 handler
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)