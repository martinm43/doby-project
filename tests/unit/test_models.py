from doby.stroman_src.mlb_database.mlb_models import SRS, Ratings, Games, Teams

def test_srs_ratings():
    """
    Given a rating SRS model
    When a rating is selected
    Then the rating is between -20/20
    """
    x = SRS.select()
    ratings = [z.srs_rating for z in x if abs(z.srs_rating) > 20]
    assert len(ratings) == 0

    
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

