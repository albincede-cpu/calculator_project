from locust import HttpUser, task
import json

class CalculatorUser(HttpUser):

    def on_start(self):
        pass

    @task
    def add(self):
        add = {
            "operation": "add",
            "operand1": 1,
            "operand2": 1
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 2:
                response.failure(f"Expected result to be 2 but was {response_data['result']}")

if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
