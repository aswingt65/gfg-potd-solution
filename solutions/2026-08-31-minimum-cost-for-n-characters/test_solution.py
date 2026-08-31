import unittest

from solution import Solution, minimum_cost


class MinimumCostTests(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(minimum_cost(9, 1, 2, 1), 5)

    def test_example_two(self):
        self.assertEqual(Solution().minimumCost(9, 10, 1, 1), 17)

    def test_empty_and_single_character(self):
        self.assertEqual(minimum_cost(0, 7, 3, 2), 0)
        self.assertEqual(minimum_cost(1, 7, 3, 2), 7)

    def test_insertion_can_be_cheaper_than_copying(self):
        self.assertEqual(minimum_cost(4, 2, 2, 100), 8)

    def test_overshoot_then_delete(self):
        # 1 -> 2 -> 4 -> 3 costs 10 + 1 + 1 + 1.
        self.assertEqual(minimum_cost(3, 10, 1, 1), 13)
        self.assertEqual(Solution().minCost(10, 10, 1, 1), 16)

    def test_large_power_of_two_boundary_case(self):
        # One insertion and nineteen doublings.
        self.assertEqual(minimum_cost(1 << 19, 100, 100, 1), 119)


if __name__ == "__main__":
    unittest.main()