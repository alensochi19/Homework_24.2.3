
import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding(self):
        assert self.calculator.adding(self, 48, 47) == 95

    def test_division(self):
        assert self.calculator.division(self, 528, 4) == 132

    def test_multiply(self):
        assert self.calculator.multiply(self, 31, 25) == 775

    def test_exponentiation(self):
        assert self.calculator.exponentiation(self, 16) == 256

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 75, 25) == 50

    def teardown(self):
        print('Выполнение метода Teardown')