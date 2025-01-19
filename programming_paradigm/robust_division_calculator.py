# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try to convert numerator and denominator to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric input error
        return "Error: Please enter numeric values only."
