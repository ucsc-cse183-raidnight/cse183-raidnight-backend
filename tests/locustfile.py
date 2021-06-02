import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_session(self):
        self.client.get("/sessions/1")

    def on_start(self):
        self.client.get("/index")
