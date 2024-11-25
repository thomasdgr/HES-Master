import pytest
from app import app

# see documentation under https://flask.palletsprojects.com/en/2.0.x/testing/


# the client here allow to use the app without running in live server
# see https://flask.palletsprojects.com/en/2.0.x/testing/
@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()
