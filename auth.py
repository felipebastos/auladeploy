from flask import Blueprint, render_template

bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates_auth")


@bp.get("/")
def home():
    return render_template("auth.html")


@bp.get("/maisum")
def outra():
    return '<a href="/auth/">Sei onde tou não</a>'
