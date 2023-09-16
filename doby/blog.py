from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from doby.stroman_src.prediction_table import playoff_odds_calc, playoff_odds_print
from doby.stroman_src.team_srs_history_plots import team_plot_function as srs_plot
from doby.stroman_src.team_elo_history_plots import team_plot_function as elo_plot
from doby.stroman_src.info_table import results_table_function
from doby.stroman_src.plot_season_odds import plot_season_odds
from doby.auth import login_required
from doby.db import get_db
from datetime import datetime, timedelta

bp = Blueprint('blog', __name__)

@bp.route('/')
@bp.route('/navigation')
def navigation():
    return render_template('navigation.html')

@bp.route('/srs',methods=["GET","POST"])
def srs():
    if request.method == 'POST':
        team_id = int(request.form['team_id'])
        img_base64 = srs_plot(team_id)

        return render_template('blog/index.html', plot=img_base64)
    return render_template('blog/index.html')

@bp.route('/elo',methods=["GET","POST"])
def elo():
    if request.method == 'POST':
        team_id = int(request.form['team_id'])
        img_base64 = elo_plot(team_id)

        return render_template('blog/elo.html', plot=img_base64)
    return render_template('blog/elo.html')

@bp.route('/pred',methods=['GET','POST'])
@login_required
def pred_table():
    if request.method =='POST':
        season_year = 2023
        start_datetime = datetime(season_year,3,22)
        end_datetime = datetime.today()-timedelta(days=1)
        ratings_mode = str(request.form['ratings_mode'])
        results_table = playoff_odds_print(playoff_odds_calc(start_datetime, end_datetime, season_year, ratings_mode=ratings_mode),season_year=season_year)

        return render_template('blog/pred.html',table = results_table)
    return render_template('blog/pred.html')

@bp.route('/info',methods=['GET','POST'])
def info_table():
    if request.method =='POST':

        season_year = int(request.form['season_year'])
        start_datetime = datetime(season_year,3,22)
        end_datetime = datetime(season_year, 11,1)
        results_table = results_table_function(season_year, start_datetime, end_datetime)

        return render_template('blog/info.html',table = results_table)
    return render_template('blog/info.html')

@bp.route('/plot',methods=['GET','POST'])
def plot():
    if request.method =='POST':

        season_year = int(request.form['season_year']) #should be limited to between 1977
        division_name = request.form['division_name'] # should be adjusting drop down
        ratings_mode = request.form['ratings_mode'] # should be adjusting drop down
        img_base64 = plot_season_odds(season_year, division_name, ratings_mode)

        return render_template('blog/plot.html', plot=img_base64)
    return render_template('blog/plot.html')