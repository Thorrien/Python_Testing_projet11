from tests.testEnv.conftest import client
import server


def test_login_and_show_clubs(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data  

    response = client.get('/showClubs')
    assert response.status_code == 200
    assert b"test1" in response.data

def test_login_and_purshace_place(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data  

    competition_name = 'Competitiontest2'
    club_name = 'test2'
    response = client.post('/purchasePlaces', data={
        'competition': competition_name,
        'club': club_name,
        'places': 1 
    })
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

def test_login_and_purshace_more_place_then_points(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data  

    competition_name = 'Competitiontest2'
    club_name = 'test2'
    response = client.post('/purchasePlaces', data={
        'competition': competition_name,
        'club': club_name,
        'places': 6 
    })
    assert response.status_code == 200
    assert b"Refus : R\xc3\xa9servation de plus de place que vous avez de points" in response.data

def test_login_and_purshace_more_than_12_place(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data  

    competition_name = 'Competitiontest2'
    club_name = 'test2'
    response = client.post('/purchasePlaces', data={
        'competition': competition_name,
        'club': club_name,
        'places': 15
    })
    assert response.status_code == 200
    assert b"Refus : R\xc3\xa9servation de plus de 12 places impossible" in response.data


def test_login_and_purchace_place_and_impact_points(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data  

    response = client.get('/showClubs')
    assert response.status_code == 200
    assert b"<td>test2</td>\n            <td>4</td>" in response.data

    competition_name = 'Competitiontest2'
    club_name = 'test2'
    response = client.post('/purchasePlaces', data={
        'competition': competition_name,
        'club': club_name,
        'places': 2
    })

    response = client.get('/showClubs')
    assert response.status_code == 200
    assert b"<td>test2</td>\n            <td>2</td>" in response.data


def test_login_and_purchace_place_and_impact_places(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Number of Places: 13\n" in response.data  

    competition_name = 'Competitiontest2'
    club_name = 'test2'
    response = client.post('/purchasePlaces', data={
        'competition': competition_name,
        'club': club_name,
        'places': 2
    })

    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Number of Places: 11\n" in response.data  

def test_login_and_purchace_place_passed_competition(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data

    competition_name = 'Competitiontest1'
    club_name = 'test2'
    response = client.get(f'/book/{competition_name}/{club_name}', follow_redirects=True)
    assert response.status_code == 200
    assert b"R\xc3\xa9servation impossible sur les comp\xc3\xa9titions pass\xc3\xa9es" in response.data


def test_login_and_purchace_place_competition(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data

    competition_name = 'Competitiontest2'
    club_name = 'test2'
    response = client.get(f'/book/{competition_name}/{club_name}', follow_redirects=True)
    assert response.status_code == 200
    assert b"How many places?" in response.data
