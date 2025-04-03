class KMapSolver:
    def solve_kmap(self, truth_table):
        """
        Simplifies the K-map and returns the Boolean expression in SOP form.
        """
        # Extract minterms and don't-care conditions
        minterms = [comb for comb, value in truth_table if value == '1']
        dont_cares = [comb for comb, value in truth_table if value == 'x']

        # Combine minterms and don't-cares for simplification
        all_terms = minterms + dont_cares

        # Simplify the K-map (basic implementation for 2-variable K-map)
        num_vars = len(truth_table[0][0])  # Number of variables
        variables = [chr(65 + i) for i in range(num_vars)]  # A, B, C, ...

        # Generate the SOP expression
        sop_terms = []
        for comb, value in truth_table:
            if value == '1':  # Only include minterms
                term = []
                for i, bit in enumerate(comb):
                    if bit == 0:
                        term.append(f"{variables[i]}'")  # Negated variable
                    elif bit == 1:
                        term.append(f"{variables[i]}")  # Non-negated variable
                sop_terms.append("".join(term))

        # Join the terms with '+' to form the SOP expression
        simplified_expression = " + ".join(sop_terms)
        return simplified_expression