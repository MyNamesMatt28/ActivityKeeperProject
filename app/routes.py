from flask import Blueprint, url_for, render_template

home = Blueprint('home', __name__, template_folder='templates')


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/create_schedule")
def create_schedule():
    return render_template("create_schedule.html")


@home.route("/easy_pace")
def easy_pace():
    return render_template("easy_pace.html")


@home.route("/pace_conversion")
def pace_conversion():
    return render_template("pace_conversion.html")


