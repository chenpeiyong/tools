import pytest
from src.calculator import Calculator

class TestCalculator:
    
    def test_add(self):
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0
    
    def test_subtract(self):
        assert Calculator.subtract(10, 5) == 5
        assert Calculator.subtract(0, 5) == -5
    
    def test_multiply(self):
        assert Calculator.multiply(3, 4) == 12
        assert Calculator.multiply(-2, 3) == -6
    
    def test_divide(self):
        assert Calculator.divide(10, 2) == 5
        assert Calculator.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            Calculator.divide(5, 0)