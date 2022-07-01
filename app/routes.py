from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

msg = "of the crud app"


@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = Entry(title=title, description=description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return msg


@app.route('/update/<int:id>')
def update_entry(id_):
    if not id_ or id_ != 0:
        entry = Entry.query.get(id_)
        if entry:
            return render_template('update.html', entry=entry)

    return msg


@app.route('/update/<int:id>', methods=['POST'])
def update_entry_post(id_):
    if not id_ or id_ != 0:
        entry = Entry.query.get(id_)
        if entry:
            form = request.form
            title = form.get('title')
            description = form.get('description')
            entry.title = title
            entry.description = description
            db.session.commit()
        return redirect('/')

    return msg


@app.route('/delete/<int:id>')
def delete_entry(id_):
    if not id_ or id_ != 0:
        entry = Entry.query.get(id_)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return msg


@app.route('/turn/<int:id>')
def turn_entry(id_):
    if not id_ or id_ != 0:
        entry = Entry.query.get(id_)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return msg


@app.errorhandler(Exception)
def error_page(e):
    return msg
