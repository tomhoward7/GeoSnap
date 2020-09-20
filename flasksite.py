from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet    

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

#@app.route("/")
#def home():
#    return render_template("home.html")

# File upload code

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()

    if form.validate_on_submit():
        
        filename = images.save(form.image.data)
        return f'Filename: { filename }'

    return render_template('home.html', form=form)

# /index file upload test page

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        
        filename = images.save(form.image.data)
        return f'Filename: { filename }'

    return render_template('index.html', form=form)