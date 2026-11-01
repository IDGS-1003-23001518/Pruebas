from locust import HttpUser, task, between

class ClienteTienda(HttpUser):
    wait_time = between(1, 2)
    @task
    def realizar_compra(self):
        self.client.post(
            "/compra",
            json={
                "precio": 200,
                "descuento": 25
            }
        )