from locust import HttpUser, task, between
import json

class CalculatorUser(HttpUser):

    wait_time = between(2, 4)

    def on_start(self):
        pass

    @task(4)
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

    @task(2)
    def subtract(self):
        subtract = {
            "operation": "subtract",
            "operand1": 2,
            "operand2": 1
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=subtract) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 1:
                response.failure(f"Expected result to be 1 but was {response_data['result']}")

    @task(2)
    def multiply(self):
        multiply = {
            "operation": "multiply",
            "operand1": 2,
            "operand2": 2
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=multiply) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 4:
                response.failure(f"Expected result to be 4 but was {response_data['result']}")

    @task(2)
    def divide(self):
        divide = {
            "operation": "divide",
            "operand1": 6,
            "operand2": 2
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=divide) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 3:
                response.failure(f"Expected result to be 3 but was {response_data['result']}")


if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
