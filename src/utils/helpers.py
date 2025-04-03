def parse_input(truth_table):
    # Convert the truth table into a format suitable for the KMapSolver
    parsed = []
    for combination, value in truth_table:
        if value.isdigit():
            parsed.append((combination, int(value)))  # Convert numeric values to integers
        elif value.lower() == 'x':
            parsed.append((combination, 'x'))  # Keep 'x' as is for don't-care conditions
        else:
            raise ValueError(f"Invalid value in truth table: {value}")
    return parsed

def format_output(simplified_expression):
    # Function to format the output of the simplified Boolean expression
    return f"Simplified Expression: {simplified_expression}"