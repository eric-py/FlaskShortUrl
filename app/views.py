from flask import Blueprint, render_template, request, flash
from .forms import ShortLinkForm
from .models import ShortLink, db
import secrets

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = ShortLinkForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        origin_url = form.long_url.data
        if origin_url:
            # Check if the original URL already exists in the database
            existing_url = ShortLink.query.filter_by(original_url=origin_url).first()
            if existing_url:
                url = request.url_root + existing_url.short_url
                flash('Link successfully shortened.', 'success')
                return render_template('index.html', form=form, short_url=url)
            else:
                # Create a new short link
                short_url = secrets.token_hex(6)
                new_url = ShortLink(original_url=origin_url, short_url=short_url)
                db.session.add(new_url)
                db.session.commit()
                url = request.url_root + short_url
                flash('Link successfully shortened.', 'success')
                return render_template('index.html', form=form, short_url=url)
        else:
            flash('Error creating short link. Please try again.', 'warning')
    elif request.method == 'POST':
        flash('Error creating short link. Please enter a valid URL.', 'warning')
    
    # If it's a GET request or form validation failed, just render the form
    return render_template('index.html', form=form)