from doby.stroman_src.mlb_database.mlb_models import SRS, Ratings

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
    ratings = [z.elo_rating for z in x if (z.elo_rating < 500 or z.elo_rating > 2500)]
    assert len(ratings) == 0
