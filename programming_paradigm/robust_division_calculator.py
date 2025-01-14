def safe_divide(numerator, denominator):
    try:
        # convert input to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # perform division
        result =numerator / denominator
        return f"The result of the division is {result:.1f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
 
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
            