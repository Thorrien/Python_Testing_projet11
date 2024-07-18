from locust import HttpUser, task, TaskSet


class appPerfTest(TaskSet):
    
    @task(1)
    def index(self):
        self.client.get("/")


class Website(HttpUser):
    tasks = [appPerfTest]
    host = "http://127.0.0.1:5000"