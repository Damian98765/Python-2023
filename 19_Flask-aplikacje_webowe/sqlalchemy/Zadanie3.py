# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tagname

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(400), unique=False, nullable=False)

    def __repr__(self):
        return f'Notatka "{self.title}" rozpoczynająca się od "{self.content[:20]}"'

    tags = db.relationship("Tag",
                    secondary='notetag',
                    uselist=True,
                    backref='note',
                    lazy='select')

class NoteTag(db.Model):
    __tablename__ = "notetag"
    id = db.Column('id', db.Integer, primary_key=True)
    tag_id = db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    note_id = db.Column('note_id', db.Integer, db.ForeignKey('note.id'))



def get_tags(session):
    return session.query(Tag).all()

def create_tag(name, session):
    try:
        tag = Tag(tagname=name)
        session.add(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True

def remove_tag(name, session):
    try:
        tag = session.query(Tag).filter_by(tagname=name).one()
        session.delete(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True



def get_notes(session):
    return session.query(Note).all()

def create_note(title, content, session):
    try:
        note = Note(title=title, content=content)
        session.add(note)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True

def remove_note(id, session):
    try:
        note = session.query(Note).filter_by(id=id).one()
        session.delete(note)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True



@app.route('/')
def hello():
    return render_template('Zadanie3_form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Tagi", no_error=True)

@app.route('/add')
def add():
    args = request.args
    no_error = create_tag(args["tag"], db.session)
    if no_error:
        tytul = f'Dodano tag: {args["tag"]}.'
    else:
        tytul = f'Tag {args["tag"]} już istnieje!'

    return render_template('Zadanie3_form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           no_error=no_error, tytul=tytul)

# @app.route('/remove', methods=['POST'])
# def remove():
#     received = request.form  # a multidict containing POST data
#     print(received)
#     print(received['values'])
#     no_error = remove_tag(received['values'], db.session)
#     if no_error:
#         tytul = "Usunięto tag"
#     else:
#         tytul = "Coś złego się wydarzyło..."
#     return render_template('Zadanie3_form.html', data=get_tags(db.session), tytul="Usunieto pozycję do listy")

@app.route('/remove')
def remove():
    args = request.args
    print(args)
    no_error = remove_tag(args["values"], db.session)
    if no_error:
        tytul = f'Usunięto tag: {args["values"]}.'
    else:
        tytul = "Coś złego się wydarzyło..."
    return render_template('Zadanie3_form.html', data=get_tags(db.session), notes=get_notes(db.session), tytul=tytul)



@app.route('/addNote')
def addNote():
    args = request.args
    #print (args)
    no_error = create_note(args["title"], args["content"], db.session)
    if no_error:
        tytul = f'Dodano nową notatkę: {args["title"]}.'
    else:
        tytul = f'Notatka takiej nazwie {args["title"]} już istnieje!'
    return render_template('Zadanie3_form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           no_error=no_error, tytul=tytul)

@app.route('/removeNote')
def removeNote():
    args = request.args
    #print(args)
    no_error = remove_note(args["values"], db.session)
    print("1")
    if no_error:
        tytul = f'Usunięto notatkę: {args["values"]}.'
    else:
        tytul = "Coś złego wydarzyło się..."
    print("2")
    return render_template('Zadanie3_form.html', data=get_tags(db.session), notes=get_notes(db.session), tytul=tytul)

# @app.route('/join')
# def join():
#     args = request.args
#     joinTables (args["noteId"], args["tagId"], db.session)
#     return render_template('Zadanie3_form.html', data=get_tags(db.session), notes=get_notes(db.session), tytul=tytul)

# def joinTables (note_id, tag_id, session)
#     #połaczyć notatkę z tagiem
#     note = session.query(Note).filter_by(id=note_id).one()
#     tag = session.query(Tag).filter_by(id=tag_id).one()
#     note.tags.append(tag)
#     session.add(note)
#     session.commit()
