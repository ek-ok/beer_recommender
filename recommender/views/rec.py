from flask import Blueprint, render_template, request, redirect, url_for, flash
from recommender.models import Recommend
from recommender import db

rec = Blueprint('rec', __name__, template_folder='/../templates')

@rec.route('/')
def index():
    all_rec = Recommend.query.order_by(Recommend.id.desc()).all()
    return render_template('rec.html', all_rec=all_rec)


@rec.route('/add', methods=['POST'])
def add_todo():
    todo = Recommend(request.form['title'], request.form['description'])
    db.session.add(todo)
    db.session.commit()
    flash('New todo was added')
    return redirect(url_for('rec.index'))


@rec.route('/todo/<int:t_id>')
def show_todo(t_id):
    todo = Recommend.query.filter_by(id=t_id).first_or_404()
    return render_template('todo.html', todo=todo)


@rec.route('/todo/<int:t_id>/edit', methods=['POST'])
def edit_todo(t_id):
    changed_title = request.form['title']
    changed_description = request.form['description']
    todo = Recommend.query.filter_by(id=t_id).first_or_404()
    todo.title = changed_title
    todo.description = changed_description
    db.session.commit()
    flash('All changes were saved')
    return redirect(url_for('rec.index'))


@rec.route('/todo/<int:t_id>/delete', methods=['POST'])
def delete_todo(t_id):
    todo = Recommend.query.filter_by(id=t_id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    flash('Recommend successfully deleted')
    return redirect(url_for('rec.index'))
