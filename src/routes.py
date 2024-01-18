from flask import Flask, jsonify, request, redirect, render_template, flash, url_for, send_file
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import uuid
from datetime import datetime
from atlas import Atlas
from chart import Chart
from topo import locator, utc

from app import app, db, login_manager
from forms import EphemerisForm, LoginForm, RegisterForm
from models import User

# Atlas Initialization
atlas = Atlas()

@login_manager.user_loader
def load_user(user_id): # Load user function
    return db.session.get(User, int(user_id))

# Login Route
@app.route('/login' , methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit(): # If form is submitted
        user = User.query.filter_by(email=form.email.data).first() # If user exists
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
            
    return render_template('login.html', form=form)

# Logout Route
@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('login'))

# Register Route
@app.route('/register' , methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegisterForm()
    if form.validate_on_submit(): # If form is submitted
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email is None: # If user does not exist
            if form.password.data != form.confirm.data:
                flash('Passwords do not match', 'Error')
                return render_template('register.html', form=form)
            user = User(email = form.email.data, username = form.username.data, password = form.password.data)
            db.session.add(user)

            try: 
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                app.logger.error(f'Error (Login): {e}')
                flash('Error: Operation failed', 'Error')
        
            login_user(user)
            db.session.close()
            return redirect(url_for('home'))

    return render_template('register.html', form=form)

# Home Route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# Ephemeris Route
@app.route('/eph', methods=['GET', 'POST'])
def ephemeris():
    user_id = None
    form = EphemerisForm()
    atlas_data = {'celestial': {}, 'placidus': {}, 'lunar': {}}
    if form.validate_on_submit():
        date = form.date.data
        time = form.time.data
        city = form.location.data

        location = locator(city)
        t = datetime.combine(date, time)
        t = utc(t, location)
        
        placidus = atlas.placidus(t, location)
        celestial = atlas.celestial(t, location)
        lunar = atlas.lunar(t, location)
        atlas_data = {'placidus': placidus, 'celestial': celestial, 'lunar': lunar}

        if current_user.is_authenticated:
            user_id = current_user.id
        else:
            user_id = str(uuid.uuid4())

        Chart(placidus, {**celestial, **lunar}, id=user_id).create_chart(show=False)

    return render_template('eph.html', form=form, atlas_data=atlas_data, user_id=user_id)

# Profile Route
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

@app.route('/chart')
def chart(t, location):
    placidus = atlas.placidus(t, location)
    celestial = atlas.celestial(t, location)
    lunar = atlas.lunar(t, location)

    Chart(placidus, {**celestial, **lunar})

    return send_file(f'static/images/{datetime.now()}.png', mimetype='image/png')
