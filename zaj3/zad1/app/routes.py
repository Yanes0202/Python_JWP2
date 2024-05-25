from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Teacher

@app.route('/')
def index():
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers)

@app.route('/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        time = request.form['time']
        if name:
            new_teacher = Teacher(name=name, subject=subject, time=time)
            db.session.add(new_teacher)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_teacher.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_teacher():
    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        teacher = Teacher.query.get(teacher_id)
        if teacher:
            db.session.delete(teacher)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_teacher.html')