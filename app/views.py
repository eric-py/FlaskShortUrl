from flask import Blueprint, render_template
from .forms import ShortLinkForm
from .models import ShortLink

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')