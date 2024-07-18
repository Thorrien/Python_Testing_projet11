import pytest
from flask import Flask
from server import app
import server
from server import loadClubs, loadCompetitions


@pytest.fixture
def client(mocker):
    mocker.patch.object(server, 'CLUBDOC', "tests//testEnv//clubstests.json")
    mocker.patch.object(server, 'COMPETITIONDOC', "tests//testEnv//competitionstest.json")
    server.clubs = loadClubs()
    server.competitions = loadCompetitions()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
