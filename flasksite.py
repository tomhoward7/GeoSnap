from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from landmark_detect import landmark_lat
from landmark_detect import landmark_long
from landmark_detect import landmark_description
from wikipedia_summary import landmark_summary
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['GOOGLEMAPS_KEY'] = "AIzaSyD_5rBuCl_0SvNgSegLul0f1IrDUHJwwKg"
GoogleMaps(app)

app.config['MAX_CONTENT_LENGTH'] = 5000 * 5000
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.tiff', '.tif', '.jpeg', '.pdf', '.raw']
app.config['UPLOAD_FOLDER'] = '/uploads/images'

@app.route("/")
def upload_file():
    return render_template("home.html")

#@app.route('/upload')
#def upload_file():
#  return render_template('upload.html')

@app.route('/results', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
       f = request.files['file']
       f.save(secure_filename(f.filename))
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=landmark_lat,
        lng=-landmark_long,
        markers=[(landmark_lat, landmark_long)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=landmark_lat,
        lng=-landmark_long,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': landmark_lat,
             'lng': landmark_long,
             'infobox': "<img src='cat1.jpg' />"
          }
        ]
    )
    return render_template('results.html', landmark_description=landmark_description, landmark_summary=landmark_summary, mymap=mymap, sndmap=sndmap, lat=landmark_lat, long=landmark_long)

@app.route("/mapview")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=landmark_lat,
        lng=-landmark_long,
        markers=[(landmark_lat, landmark_long)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=landmark_lat,
        lng=-landmark_long,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': landmark_lat,
             'lng': landmark_long,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': landmark_lat,
             'lng': landmark_long,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('mapview.html', mymap=mymap, sndmap=sndmap, lat=landmark_lat, long=landmark_long)

if __name__ == "__main__":
    app.run(debug=True)