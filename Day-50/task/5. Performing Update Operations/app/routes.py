from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import User
from app.forms import EditUserForm
from flask import current_app
import logging

main = Blueprint('main', __name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@main.route('/user/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    form = EditUserForm(obj=user)  # Pre-fill form with user info

    if form.validate_on_submit():
        before = {'username': user.username, 'email': user.email}

        user.username = form.username.data
        user.email = form.email.data

        # Password change only if current password matches
        if form.current_password.data:
            if user.check_password(form.current_password.data):
                if form.new_password.data:
                    user.set_password(form.new_password.data)
                    flash('Password updated!', 'info')
                else:
                    flash('Provide a new password.', 'warning')
                    return render_template('edit_user.html', form=form)
            else:
                flash('Current password incorrect.', 'danger')
                return render_template('edit_user.html', form=form)

        db.session.commit()

        after = {'username': user.username, 'email': user.email}
        logger.info(f"User updated (ID: {user.id}): Before={before}, After={after}")

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('main.edit_user', id=user.id))

    return render_template('edit_user.html', form=form)
