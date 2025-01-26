class Calculator:
    
    calculation_type = "Arithmetic Operations"
    
    # Using the static method
    @staticmethod
    def add(a, b):
        return a + b
    
    # Using the class method
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return  a * b 

