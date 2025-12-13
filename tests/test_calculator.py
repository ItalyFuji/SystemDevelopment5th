"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    return Calculator()
    
    

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        # calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        # calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        # calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        # calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        # calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        # calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        # calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_raises_error_for_too_large_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_add_raises_error_for_too_small_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(-1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_add_raises_error_for_too_large_b(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(1, 1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_add_raises_error_for_too_small_b(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(1, -1000001)
        assert "outside the valid range" in str(excinfo.value)
    
    def test_add_max_a(self, calc):
        # Arrange
        a = 1000000
        b = 3
        expected = 1000003

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_min_a(self, calc):
        # Arrange
        a = -1000000
        b = 3
        expected = -999997

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)   

    def test_add_max_b(self, calc):
        # Arrange
        a = 1
        b = 1000000
        expected = 1000001

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_min_b(self, calc):
        # Arrange
        a = 9
        b = -1000000
        expected = -999991

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)        

class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # TODO: Implement
         
        # Arrange
        # calc = Calculator()
        a = 11
        b = 2
        expected = 9

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
        
    def test_subtract_negative_numbers(self, calc):

        # Arrange
        a = 11
        b = -2
        expected = 13
        
        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_raises_error_for_too_large_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_subtract_raises_error_for_too_small_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(-1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_subtract_raises_error_for_too_large_b(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(1, 1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_subtract_raises_error_for_too_small_b(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(1, -1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_subtract_max_a(self, calc):
        # Arrange
        a = 1000000
        b = 7
        expected = 999993

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_min_a(self, calc):
        # Arrange
        a = -1000000
        b = 4
        expected = -1000004

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)   

    def test_subtract_max_b(self, calc):
        # Arrange
        a = 2
        b = 1000000
        expected = -999998

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_min_b(self, calc):
        # Arrange
        a = 3
        b = -1000000
        expected = 1000003

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected) 

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # TODO: Implement
        
        # Arrange
        # calc = Calculator()
        a = 10000
        b = 2
        expected = 20000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected       
        
    def test_multiply_negative_numbers(self, calc):
        
        # Arrange
        a = 3
        b = -2
        expected = -6

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected               

    def test_multiply_raises_error_for_too_large_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_multiply_raises_error_for_too_small_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(-1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_multiply_raises_error_for_too_large_b(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(1, 1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_multiply_raises_error_for_too_small_b(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(1, -1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_subtract_max_a(self, calc):
        # Arrange
        a = 1000000
        b = 31
        expected = 31000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_min_a(self, calc):
        # Arrange
        a = -1000000
        b = 41
        expected = -41000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)   

    def test_subtract_max_b(self, calc):
        # Arrange
        a = 90
        b = 1000000
        expected = 90000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_min_b(self, calc):
        # Arrange
        a = 4
        b = -1000000
        expected = -4000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected) 

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # TODO: Implement

        # Arrange
        # calc = Calculator()
        a = 100
        b = 25
        expected = 4

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected
        
    def test_divide_negative_numbers(self, calc):

        # Arrange
        a = 10
        b = -2
        expected = -5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_floats(self, calc):

        # Arrange
        a = 33
        b = 5
        expected = 6.6

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected


    def test_divide_with_zero(self, calc):
        # Arrange
        a = 1
        b = 0
        
        with pytest.raises(ValueError) as excinfo:
            calc.divide(a, b)

        assert str(excinfo.value) == "Cannot divide by zero"

    def test_divide_raises_error_for_too_large_a(self, calc):
        with pytest.raises(InvalidInputException) as excinfo:
            calc.divide(1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_divide_raises_error_for_too_small_a(self, calc):
        with pytest.raises(InvalidInputException)as excinfo:
            calc.divide(-1000001, 1)
        assert "outside the valid range" in str(excinfo.value)

    def test_divide_raises_error_for_too_large_b(self, calc):
        with pytest.raises(InvalidInputException)as excinfo:
            calc.divide(1, 1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_divide_raises_error_for_too_small_b(self, calc):
        with pytest.raises(InvalidInputException)as excinfo:
            calc.divide(1, -1000001)
        assert "outside the valid range" in str(excinfo.value)

    def test_divide_max_a(self, calc):
        # Arrange
        a = 1000000
        b = 1
        expected = 1000000

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_min_a(self, calc):
        # Arrange
        a = -1000000
        b = 4
        expected = -250000

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)   

    def test_divide_max_b(self, calc):
        # Arrange
        a = 2
        b = 1000000
        expected = 0.000002

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_min_b(self, calc):
        # Arrange
        a = 10
        b = -1000000
        expected = -0.00001

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected) 
