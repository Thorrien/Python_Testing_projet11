from server import loadClubs, loadCompetitions
import server

def test_loadClub(): 
    data = loadClubs()
    assert data is not None


def test_loadClub_moké(mocker): 
    mocker.patch.object(server, 'CLUBDOC', "tests//testEnv//clubstests.json")
    data = loadClubs()
    assert data[0] == {'email': 'test1@test1.com', 'name': 'test1', 'points': '13'}
    assert data[1] == {'email': 'test2@test2.com', 'name': 'test2', 'points': '4'}
    assert data[2] == {'email': 'test3@test3.com', 'name': 'test3', 'points': '12'}


def test_loadcompetitions(): 
    data = loadCompetitions()
    assert data is not None


    
def test_loadcompetitions_moké(mocker): 
    mocker.patch.object(server, 'COMPETITIONDOC', "tests//testEnv//competitionstest.json")
    data = loadCompetitions()
    assert data[0] == {'date': '2020-03-27 10:00:00', 'name': 'Competitiontest1', 'numberOfPlaces': '25'}
    assert data[1] == {'date': '2024-10-22 13:30:00', 'name': 'Competitiontest2', 'numberOfPlaces': '13'}
