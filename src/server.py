from flask import Flask, jsonify, request, render_template
from datetime import datetime
from atlas import Atlas
from topography import locator, utc
from forms import EphemerisForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mellon'
atlas = Atlas()

@app.route('/login' , methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register' , methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/eph', methods=['GET', 'POST'])
def ephemeris():
    form = EphemerisForm()
    atlas_data = {'placidus': {}, 'celestial': {}}
    if form.validate_on_submit():
        date = form.date.data
        time = form.time.data
        city = form.location.data

        location = locator(city)
        t = datetime.combine(date, time)
        t = utc(t, location)
        
        placidus = {key: object.to_dict() for key, object in atlas.placidus(t, location).items()}
        celestial = {key: object.to_dict() for key, object in atlas.celestial(t, location).items()}
        lunar = {key: object.to_dict() for key, object in atlas.lunar(t, location).items()}
        atlas_data = {'placidus': placidus, 'celestial': celestial, 'lunar': lunar}

    return render_template('eph.html', form=form, atlas_data=atlas_data)

if __name__ == '__main__':
    app.run(debug=True)
