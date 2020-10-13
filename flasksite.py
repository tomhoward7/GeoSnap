from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import landmark_detect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['GOOGLEMAPS_KEY'] = "AIzaSyD_5rBuCl_0SvNgSegLul0f1IrDUHJwwKg"
GoogleMaps(app)

app.config['MAX_CONTENT_LENGTH'] = 5000 * 5000
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.tiff', '.tif', '.jpeg', '.pdf', '.raw']
app.config['UPLOAD_FOLDER'] = 'uploads/images'

@app.route("/")
def upload_file():
    return render_template("home.html")

@app.route('/results', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
       f = request.files['file']
       print(secure_filename(f.filename))
       f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
       location_hash = landmark_detect.location(secure_filename(f.filename))
       print(location_hash)
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=location_hash['lat'],
        lng=location_hash['long'],
        markers=[(location_hash['lat'], location_hash['long'])],
        style="height:100%;width:100%;top:0;left:0;position:absolute;z-index:200;"
    )
    return render_template('results.html', landmark_description=location_hash['description'], landmark_summary=location_hash['summary'], mymap=mymap, lat=location_hash['lat'], long=location_hash['long'])

if __name__ == "__main__":
    app.run(debug=True)