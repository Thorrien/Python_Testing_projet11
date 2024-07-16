import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime

CLUBDOC = 'clubs.json'
COMPETITIONDOC = 'competitions.json'

def loadClubs():
    with open(CLUBDOC) as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open(COMPETITIONDOC) as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['GET', 'POST'])
def showSummary():
    if request.method == 'POST':
        email = request.form['email']
    else:
        email = request.args.get('email')

    club = next((club for club in clubs if club['email'] == email), None)
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        message = "Ce n'est pas le bon email."
        return render_template('index.html', message=message)

@app.route('/book/<competition>/<club>', methods=['GET','POST'])
def book(competition,club):
    foundClub =  [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    actualDate = datetime.now()
    if foundClub and foundCompetition:
        competition_date = datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S')
        if competition_date >= actualDate:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
        else: 
            flash("Réservation impossible sur les compétitions passées")
            return redirect(url_for('showSummary', email=foundClub['email']))
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired <= 12 :
        if placesRequired <= int(club['points']):
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club['points'] = int(club['points'])- placesRequired
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)
        else : 
            flash('Refus : Réservation de plus de place que vous avez de points')
            return render_template('welcome.html', club=club, competitions=competitions)
    else : 
        flash('Refus : Réservation de plus de 12 places impossible')
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/showClubs', methods=['GET'])
def showClub():
    return render_template('clubList.html', clubs=clubs)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

