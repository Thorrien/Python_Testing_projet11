from tests.testEnv.conftest import client
import server

def test_acceuil_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200
	
def test_summary_status_code_ok(client):
    response = client.get('/showSummary')
    assert response.status_code == 200

def test_show_summary_with_invalid_email(client):
    invalid_email = "nonexistent@example.com"
    response = client.post('/showSummary', data={'email': invalid_email})
    assert response.status_code == 200
    assert b"Ce n&#39;est pas le bon email." in response.data


def test_show_summary_with_valid_email(client):
    valid_email = 'test2@test2.com'
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_showClubs_status_code_ok(client):
    response = client.get('/showClubs')
    assert response.status_code == 200

def test_logout_status_code_notok(client):
    response = client.get('/logout')
    assert response.status_code == 302

def test_booking_status_code_ok(client):
    response = client.get('/book/Competitiontest2/test2')
    assert response.status_code == 200



