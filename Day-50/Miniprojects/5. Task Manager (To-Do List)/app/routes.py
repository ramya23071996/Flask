from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Task
from .forms import TaskForm

def register_routes(app):

    @app.route("/")
    def index():
        tasks = Task.query.order_by(Task.due_date.asc()).all()
        return render_template("index.html", tasks=tasks)

    @app.route("/add", methods=["GET", "POST"])
    def add_task():
        form = TaskForm()
        if form.validate_on_submit():
            task = Task(
                title=form.title.data,
                due_date=form.due_date.data,
                is_done=form.is_done.data
            )
            db.session.add(task)
            db.session.commit()
            flash("Task added!", "success")
            return redirect("/")
        return render_template("task_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_task(id):
        task = Task.query.get_or_404(id)
        form = TaskForm(obj=task)
        if form.validate_on_submit():
            task.title = form.title.data
            task.due_date = form.due_date.data
            task.is_done = form.is_done.data
            db.session.commit()
            flash("Task updated!", "success")
            return redirect("/")
        return render_template("task_form.html", form=form)

    @app.route("/delete_done")
    def delete_completed():
        Task.query.filter_by(is_done=True).delete()
        db.session.commit()
        flash("Completed tasks deleted!", "info")
        return redirect("/")