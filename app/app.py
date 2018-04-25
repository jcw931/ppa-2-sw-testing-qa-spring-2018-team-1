import logging
from flask import Flask, render_template, redirect, url_for, request, Blueprint
from .forms import gen_dist_form, gen_email_form
from .distance import calc_distance
from .email import verify_email

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        return 'Hello, bmi post!'
    else:
        return 'Hello, bmi!'


@main_blueprint.route('/distance', methods=['GET', 'POST'])
def distance():
    dist_form = gen_dist_form(request.form)
    if request.method == 'POST':
        distance = calc_distance(dist_form.x1.data, dist_form.y1.data, dist_form.x2.data, dist_form.y2.data)
        return render_template('distance.html', form=dist_form, distance=distance, post=1)
    else:
        return render_template('distance.html', form=dist_form, distance=0, post=0)


@main_blueprint.route('/email', methods=['GET', 'POST'])
def email():
    email_form = gen_email_form(request.form)
    if request.method == 'POST':
        email = verify_email(email_form.email_input.data)
        return render_template('email.html', form=email_form, email=email, post=True)
    else:
        return render_template('email.html', form=email_form, email="", post=0)


@main_blueprint.route('/retirement', methods=['GET', 'POST'])
def retirement():
    if request.method == 'POST':
        return 'Hello, retirement post!'
    else:
        return 'Hello, retirement!'


@main_blueprint.route('/tip', methods=['GET', 'POST'])
def tip():
    if request.method == 'POST':
        return 'Hello, tip post!'
    else:
        return 'Hello, tip!'


@main_blueprint.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


@main_blueprint.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('Someone tried to do something they were not supposed to do!.')
    return render_template('index.html')
