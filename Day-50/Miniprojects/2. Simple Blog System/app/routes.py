from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Post
from .forms import PostForm

def register_routes(app):

    @app.route("/")
    def index():
        posts = Post.query.order_by(Post.created_at.desc()).all()
        return render_template("index.html", posts=posts)

    @app.route("/add", methods=["GET", "POST"])
    def add_post():
        form = PostForm()
        if form.validate_on_submit():
            post = Post(
                title=form.title.data,
                content=form.content.data,
                author=form.author.data
            )
            db.session.add(post)
            db.session.commit()
            flash("Post created successfully!", "success")
            return redirect(url_for("index"))
        return render_template("post_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_post(id):
        post = Post.query.get_or_404(id)
        form = PostForm(obj=post)
        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            post.author = form.author.data
            db.session.commit()
            flash("Post updated!", "success")
            return redirect(url_for("index"))
        return render_template("post_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_post(id):
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!", "info")
        return redirect(url_for("index"))