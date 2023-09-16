import os
from requests import request
from flask import Flask, render_template
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from doby.stroman_src.team_srs_history_plots import team_plot_function 
import numpy as np
import io
import base64

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'doby.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #a simple page that says hello
    @app.route('/hello')
    def hello():
       return 'Hello, World!'

    # @app.route('/', methods=['GET', 'POST'])
    # @app.route('/index')
    # def index():
    #     if request.method == 'POST':
    #         # m = float(request.form['m'])
    #         # b = float(request.form['b'])
    #         # x = np.linspace(-10, 10, 100)
    #         # y = m * x + b
    #         team_id = int(request.form['team_id'])

    #         # # Plotting the graph
    #         # plt.plot(x, y)
    #         # plt.xlabel('x')
    #         # plt.ylabel('y')
    #         # plt.title('Graph of team_id: {}'.format(m))
    #         # plt.grid()

    #         # # Save the plot to a byte stream
    #         # img_stream = io.BytesIO()
    #         # plt.savefig(img_stream, format='png')
    #         # img_stream.seek(0)
    #         img_base64 = team_plot_function(team_id) 
    #         return render_template('index.html', plot=img_base64) 
    #     return render_template('index.html')

    from . import db
    db.init_app(app)


    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='navigation',) #breaks file?

    return app