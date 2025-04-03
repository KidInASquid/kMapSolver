# This file is the entry point of the application. It initializes the K-map solver and handles user input/output.

from solver.kmap_solver import KMapSolver
from utils.helpers import parse_input, format_output
from itertools import product
import math

def print_kmap(truth_table, num_vars):
    # Determine the number of rows and columns for the K-map
    num_rows = 2 ** (num_vars // 2)
    num_cols = 2 ** (num_vars - num_vars // 2)
    
    # Generate row and column headers in Gray Code
    def to_gray_code(n):
        return n ^ (n >> 1)  # Convert binary to Gray Code

    row_headers = [format(to_gray_code(i), f"0{num_vars // 2}b") for i in range(num_rows)]
    col_headers = [format(to_gray_code(i), f"0{num_vars - num_vars // 2}b") for i in range(num_cols)]
    
    # Create a dictionary to map input combinations to their output values
    truth_dict = {"".join(map(str, comb)): value for comb, value in truth_table}
    
    # Print the K-map headers
    print("\n\nK-map:")
    print("   " + "  ".join(col_headers))  # Column headers with extra spacing
    for row in row_headers:
        row_values = []
        for col in col_headers:
            # Combine row and column to form the full input combination
            full_comb = row + col
            # Get the corresponding value from the truth table
            row_values.append(truth_dict.get(full_comb, "x"))  # Default to 'x' if not found
        # Print row header and values with proper spacing
        print(f"{row}  " + "  ".join(row_values))

def main():
    print("Welcome to the K-map Solver!")
    
    # Ask for the size of the truth table
    table_size = int(input("Enter the size of the truth table (number of rows): "))
    
    # Calculate the number of variables (columns) needed
    num_vars = math.ceil(math.log2(table_size))
    print(f"The truth table will have {num_vars} variables.")
    
    # Generate column headers
    headers = [chr(65 + i) for i in range(num_vars)]  # A, B, C, ...
    print("Enter values in the form:")
    print(f"{' '.join(headers)} | X")
    
    # Generate all possible combinations of inputs
    variable_combinations = list(product([0, 1], repeat=num_vars))
    truth_table = []
    
    # Prompt the user for each row of the truth table
    for i in range(table_size):
        combination = variable_combinations[i]
        combination_str = " ".join(map(str, combination))
        value = input(f"{combination_str} | ")
        truth_table.append((combination, value))
    
    # Parse the input data
    parsed_data = parse_input(truth_table)
    
    # Initialize the K-map solver
    solver = KMapSolver()
    
    # Solve the K-map
    simplified_expression = solver.solve_kmap(parsed_data)
    
    # Print the K-map
    print_kmap(truth_table, num_vars)
    # Format and display the output
    output = format_output(simplified_expression)
    print(f"\n\nSimplified Boolean Expression: {output}")
    

if __name__ == "__main__":
    main()
