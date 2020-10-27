from flask import Flask, redirect, render_template, url_for
from forms import PostForm

app = Flask(__name__, instance_relative_config=False)
# app.config.from_object('config.Config')
app.config['SECRET_KEY'] = 'any secret string'

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.jinja2', title="index", template="index")

@app.route('/post', methods=['GET', 'POST'])
def post():
  form = PostForm()
  if form.validate_on_submit():
      return redirect(url_for('guestbook'))
  return render_template('form.html', form=form, template="form")
  # return render_template('index.html', form=form)
  # return render_template('form.jinja2', title="form", template="form")

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
  return render_template('contacts.jinja2', title="contacts", template="contacts")

@app.route('/courses', methods=['GET', 'POST'])
def courses():
  return render_template('courses.jinja2', title="courses", template="courses")

@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
  return render_template('teachers.jinja2', title="teachers", template="teachers")

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
  return render_template('guestbook.jinja2', title="guestbook", template="guestbook")