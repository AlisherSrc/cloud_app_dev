from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(1)
    def view_pins(self):
        self.client.get("/pins/")

    @task(2)
    def view_pin_detail(self):
        # Assuming you have pins with IDs 1 to 100
        pin_id = 1  # You can randomize this
        self.client.get(f"/pins/{pin_id}/")

    @task(1)
    def create_pin(self):
        pin_data = {
            'title': 'Load Test Pin',
            'description': 'This pin is created during load testing.',
            'contentUrl': 'http://example.com/image.jpg',
            'destinationLink': 'http://example.com',
        }
        self.client.post("/pins/", data=pin_data)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
