from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from utils.country_helper import CountryHelper
from utils.level_helper import LevelHelper


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html', countries_list=CountryHelper.get_countries()
                                        , levels_list=LevelHelper.get_levels())

if __name__ == '__main__':
    app.run(debug=True)
