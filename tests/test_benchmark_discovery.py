import unittest

from benchmarks.run_benchmarks import (
    discover_puzzles,
    classify_solving_method
)


class TestBenchmarkDiscovery(unittest.TestCase):

    def test_discovers_existing_puzzles(self):
        discovered = discover_puzzles()

        self.assertGreaterEqual(len(discovered), 4)

        for name, create_puzzle in discovered.items():
            self.assertIsInstance(name, str)
            self.assertTrue(callable(create_puzzle))

    def test_discovered_puzzles_can_be_created(self):
        discovered = discover_puzzles()

        for name, create_puzzle in discovered.items():
            with self.subTest(puzzle=name):
                puzzle = create_puzzle()
                self.assertIsNotNone(puzzle)


    def test_propagation_only_classification(self):
        self.assertEqual(
            classify_solving_method(0),
            "Propagation Only"
        )

    def test_search_classification(self):
        self.assertEqual(
            classify_solving_method(1),
            "Propagation + Search"
        )

        self.assertEqual(
            classify_solving_method(100),
            "Propagation + Search"
        )


if __name__ == "__main__":
    unittest.main()