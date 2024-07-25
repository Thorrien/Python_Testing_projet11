from locust import HttpUser, task, TaskSet


class appPerfTest(TaskSet):
    
    @task(1)
    def A_index(self):
        self.client.get("/")

    @task(1)
    def B_login(self):
        valid_email = 'admin@irontemple.com'
        self.client.post('/showSummary', data={'email': valid_email})

    @task(1)
    def C_Club(self):
        self.client.get('/showClubs')

    @task(1)
    def D_book(self):
        competition_name = 'Fall Classic'
        club_name = 'Iron Temple'
        self.client.get(f'/book/{competition_name}/{club_name}')

    @task(1)
    def E_purchace_place(self):
        competition_name = 'Fall Classic'
        club_name = 'Iron Temple'
        self.client.post('/purchasePlaces', data={
        'competition': competition_name,
        'club': club_name,
        'places': 0 
        })
        
    @task(1)
    def F_Logout(self):
        self.client.get('/logout')


class Website(HttpUser):
    tasks = [appPerfTest]
    host = "http://127.0.0.1:5000"