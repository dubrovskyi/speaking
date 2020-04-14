from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, session, redirect,url_for
from flask import request, make_response
from flask_wtf import FlaskForm
from flask_session import Session
import uuid
import os
import redis

from utils.common_helper import CommonHelper
from utils.redis_helper import RedisHelper
from models.InfoForm import InfoForm


app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = 'any secret string'
app.config['FLASK_RUN_HOST'] = '0.0.0.0'
rediis = redis.Redis('localhost')

@app.route('/',methods=['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['nick'] = form.nick.data
        session['age'] = form.age.data
        session['level'] = form.level.data
        session['goal'] = form.goal.data
        session['country'] = form.country.data
        session['skype'] = form.skype.data
        if not "iid" in session.keys():
            session['iid'] = CommonHelper.randomString(12)
        rediis.hset("sessions",session['iid'],str(dict(session)))
        return redirect(url_for('index'))

    sessions = RedisHelper.convert_redis_to_json(rediis, "sessions")
    print(sessions)
    resp = make_response(render_template("index.html", form=form, sessions=sessions))
    resp.set_cookie("key", "value", "key2", "value2")
    return resp


@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return make_response(render_template("page404.html"), 404)
