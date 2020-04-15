from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,
                    SubmitField)
from wtforms.validators import DataRequired

from application.utils.country_helper import CountryHelper
from application.utils.level_helper import LevelHelper
from application.utils.goals_helper import GoalsHelper

def tuple_form_dict():
    return [(c['code'],f"{c['code']} - {c['name']}") for c in CountryHelper.get_countries()]


class InfoForm(FlaskForm):

    nick = StringField('Nick:',validators=[DataRequired()])
    age = SelectField(u'Age:',validators=[DataRequired()],
                                choices=[(str(age), age)
                                        for age in range(16, 71)])
    level = SelectField(u'Level:',choices=[('be','Beginner'),
                                        ('in','Intermediate'),
                                        ('up','Upper-Intermediate'),
                                        ('ad','Advanced')])
    goal = SelectField(u'Goal:',choices=
                                [(f"{len(g)}", g) for g in GoalsHelper.get_goals()])
    country = SelectField(u'Level:',choices=tuple_form_dict())
    skype = StringField('Skype:',validators=[DataRequired()])
    submit = SubmitField('Submit')