import pytest
from test2 import BaseTestCalculator

class TestCalculator(BaseTestCalculator):
  
    @pytest.mark.parametrize( "a, b, expected", [(2, 2, 4), (3, 3, 6)])

    def test_add(self, a, b, expected):
        value = self.calculator.add(a,b)
        #assert value == 2 , "womp womp"
        assert value == expected, f"Expected {a} + {b} = {expected}, got {value}"


    def test_sub(self):
        value = self.calculator.subtract(4,1)
        assert value == 3 , "womp womp"

    def test_mult(self):
        value = self.calculator.multiply(2,1)
        assert value == 2 , "womp womp"

    def test_div(self):
        value = self.calculator.divide(6,2)
        assert value == 3 , "womp womp"
    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1, 0)