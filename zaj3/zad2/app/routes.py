from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        context = request.form['context']
        if title:
            new_task = Task(title=title, context=context)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_task.html')



@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return '', 204



@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.context = request.form['context']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)
