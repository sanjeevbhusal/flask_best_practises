from flask import Blueprint, render_template, request

page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
def home():
    return render_template("main.html")




