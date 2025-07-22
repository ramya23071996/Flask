from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Post, Comment
from .forms import CommentForm

def register_routes(app):

    @app.route("/")
    def index():
        posts = Post.query.order_by(Post.id.desc()).all()
        return render_template("index.html", posts=posts)

    @app.route("/add_post", methods=["GET", "POST"])
    def add_post():
        if request.method == "POST":
            title = request.form.get("title")
            content = request.form.get("content")
            db.session.add(Post(title=title, content=content))
            db.session.commit()
            flash("Post added!", "success")
            return redirect("/")
        return render_template("post_form.html")

    @app.route("/comment/<int:post_id>", methods=["POST"])
    def comment(post_id):
        form = CommentForm()
        if form.validate_on_submit():
            c = Comment(content=form.content.data, post_id=post_id)
            db.session.add(c)
            db.session.commit()
            flash("Comment submitted!", "success")
        return redirect("/")