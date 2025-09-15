from BE.calculator_helper import CalculatorHelper

class BaseTestCalculator():
    def setup_method(self):
        self.calculator = CalculatorHelper()

    def teardown_method(self):
        del self.calculator
