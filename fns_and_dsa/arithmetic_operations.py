def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            operation_result = num1 + num2
        case "subtract":
            operation_result = num1 - num2
        case "multiply":
            operation_result = num1 * num2
        case "divide":
            if num1 == 0 or num2 == 0:
                print("Division by ZERO is undifined")
                operation_result = "undefined"
            else:
                operation_result = num1 / num2
    
    return operation_result
        