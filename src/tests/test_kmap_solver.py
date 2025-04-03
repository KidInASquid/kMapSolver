import unittest
from solver.kmap_solver import KMapSolver

class TestKMapSolver(unittest.TestCase):

    def setUp(self):
        self.solver = KMapSolver()

    def test_solve_kmap_simple(self):
        input_data = "1, 1, 1, 0, 1, 0, 0, 0"  # Example input for a simple K-map
        expected_output = "A + B"  # Expected simplified expression
        self.assertEqual(self.solver.solve_kmap(input_data), expected_output)

    def test_solve_kmap_complex(self):
        input_data = "1, 1, 0, 0, 1, 1, 1, 0"  # Example input for a complex K-map
        expected_output = "A'B + AB'"  # Expected simplified expression
        self.assertEqual(self.solver.solve_kmap(input_data), expected_output)

    def test_solve_kmap_empty(self):
        input_data = "0, 0, 0, 0, 0, 0, 0, 0"  # No minterms
        expected_output = "0"  # Expected output for no minterms
        self.assertEqual(self.solver.solve_kmap(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()