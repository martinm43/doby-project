"""
Requirements we are testing against:
* SRS calculation does not blow up (ratings remain within 10 for all SRS, this is baseball)
* SRS ratings for several years (listed in test definition) are correct
* ELO calculation remains between 500 and 2500
* No games are stored without home_team_id or away_team_id in database
"""

from peewee import fn
from doby.stroman_src.mlb_database.mlb_models import SRS, Ratings, Games, Teams

def test_srs_rating_calculation_stability():
    """
    Given a rating SRS model
    When a rating is selected
    Then the rating is between -20/20
    """
    x = SRS.select()
    ratings = [z.srs_rating for z in x if abs(z.srs_rating) > 20]
    assert len(ratings) == 0

def test_srs_rating_calculation_accuracy():
    """
    Given a SRS calculation for the years (2017)
    When the calculation is performed
    Then the difference in ratings is no greater than .2 for 20% of the teams
    """
    tol = 0.2
    errcount = 6
    maxdatetime = SRS.select(fn.MAX(SRS.epochtime)).where(SRS.year==2017)
    maxSRS = SRS.select().where(SRS.epochtime==maxdatetime)
    calcSRSratings = [(x.team_abbreviation,x.srs_rating) for x in maxSRS]
    goodSRSratings = [('LAA', 0.1),
                        ('ARI', 0.8),
                        ('ATL', -0.7),
                        ('BAL', -0.3),
                        ('BOS', 0.8),
                        ('CHC', 0.6),
                        ('CHW', -0.5),
                        ('CIN', -0.7),
                        ('CLE', 1.5),
                        ('COL', 0.3),
                        ('DET', -0.8),
                        ('MIA', -0.5),
                        ('HOU', 1.2),
                        ('KCR', -0.4),
                        ('LAD', 0.9 ),
                        ('MIL', 0.1),
                        ('MIN', 0.2),
                        ('NYM', -0.9),
                        ('NYY', 1.3),
                        ('OAK', -0.4),
                        ('PHI', -0.7),
                        ('PIT', -0.4),
                        ('SDP', -1.3),
                        ('SEA', 0),
                        ('SFG', -0.9),
                        ('STL', 0.2),
                        ('TBR', 0.1),
                        ('TEX', 0) ,
                        ('TOR', -0.3),
                        ('WSN', 0.6)]
    calcSRSratings = sorted(calcSRSratings, key=lambda x: x[0])
    goodSRSratings = sorted(goodSRSratings, key=lambda x: x[0])
    differences=[]
    for i in range(len(goodSRSratings)):
        print(goodSRSratings[i][0],calcSRSratings[i][1]-goodSRSratings[i][1])
        differences.append(abs(calcSRSratings[i][1]-goodSRSratings[i][1])) #absolute diff
    
    errval = [x for x in differences if x > tol]
    assert len(errval) < errcount
    
def test_srs_rating_calculation_order():
    """
    Given a SRS calculation for the years (2017)
    When the calculation is performed
    Then the ratings are in order
    Editor's note: if this test fails the other (accuracy) test failed too
    """
    maxdatetime = SRS.select(fn.MAX(SRS.epochtime)).where(SRS.year==2017)
    maxSRS = SRS.select().where(SRS.epochtime==maxdatetime)
    calcSRSratings = [(x.team_abbreviation,x.srs_rating) for x in maxSRS]
    goodSRSratings = [('LAA', 0.1),
                        ('ARI', 0.8),
                        ('ATL', -0.7),
                        ('BAL', -0.3),
                        ('BOS', 0.8),
                        ('CHC', 0.6),
                        ('CHW', -0.5),
                        ('CIN', -0.7),
                        ('CLE', 1.5),
                        ('COL', 0.3),
                        ('DET', -0.8),
                        ('MIA', -0.5),
                        ('HOU', 1.2),
                        ('KCR', -0.4),
                        ('LAD', 0.9 ),
                        ('MIL', 0.1),
                        ('MIN', 0.2),
                        ('NYM', -0.9),
                        ('NYY', 1.3),
                        ('OAK', -0.4),
                        ('PHI', -0.7),
                        ('PIT', -0.4),
                        ('SDP', -1.3),
                        ('SEA', 0),
                        ('SFG', -0.9),
                        ('STL', 0.2),
                        ('TBR', 0.1),
                        ('TEX', 0) ,
                        ('TOR', -0.3),
                        ('WSN', 0.6)]
    calcSRSratings = sorted(calcSRSratings, key=lambda x: x[0])
    goodSRSratings = sorted(goodSRSratings, key=lambda x: x[0])
    assert [x[0] for x in calcSRSratings] == [x[0] for x in goodSRSratings]

def test_Elo_ratings():
    """
    Given an Elo model
    When a rating is selected
    Then the rating is between 500 and 2500 -- just a demonstration check
    """
    x = Ratings.select()
    oob_ratings = [z.elo_rating for z in x if (z.elo_rating < 500 or z.elo_rating > 2500)]
    zero_ratings = [z.elo_rating for z in x if (z.elo_rating == 0)]
    assert len(oob_ratings) == 0
    assert len(zero_ratings) == 0

def test_games():
    """
    Given a game model
    When it is stored in the database
    Team ids are stored correctly (no orphan games)
    """
    x = Games.select()
    blank_home_team_ids = [z.home_team_id for z in x if (z.home_team_id == 0 or z.home_team_id == None)]
    blank_away_team_ids = [z.away_team_id for z in x if (z.away_team_id == 0 or z.away_team_id == None)]
    assert len(blank_home_team_ids) == 0
    assert len(blank_away_team_ids) == 0

