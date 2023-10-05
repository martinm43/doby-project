from doby import create_app
import os

def test_home_page_post_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Navigation" not in response.data

def test_home_page_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response has all the expected links
    """
    response = test_client.get('/')
    print(response.data)
    assert response.status_code == 200
    assert b"Plot Season Playoff Odds" in response.data
    assert b"Get Information About Season Between Dates" in response.data
    assert b"Generate Playoff Odds Prediction Table" in response.data
    assert b"Team Historical Elo" in response.data
    assert b"Team Historical SRS" in response.data

