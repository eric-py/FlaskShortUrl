from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import ShortLinkForm
from .models import ShortLink, db
import secrets

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # show and send form on index files
    form = ShortLinkForm()
    return render_template('index.html', form=form)