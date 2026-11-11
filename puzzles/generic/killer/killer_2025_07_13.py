"""PuzzleMadness Killer Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 7)
    puzzle.add_killer_cage([(0, 0), (0, 1)], 14)
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0)], 13)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 10)
    puzzle.add_killer_cage([(0, 2), (0, 3)], 11)
    puzzle.add_killer_cage([(0, 4), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)], 31)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 4)
    puzzle.add_killer_cage([(0, 7), (0, 8)], 9)
    puzzle.add_killer_cage([(1, 7), (1, 8), (2, 8)], 24)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 9)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 13)
    puzzle.add_killer_cage([(6, 6), (6, 7), (6, 8)], 13)
    puzzle.add_killer_cage([(7, 6), (7, 7), (7, 8)], 10)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 22)
    puzzle.add_killer_cage([(2, 1), (3, 1), (4, 1)], 22)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 2)], 12)
    puzzle.add_killer_cage([(3, 3), (4, 2), (4, 3)], 12)
    puzzle.add_killer_cage([(5, 1), (5, 2), (5, 3)], 8)
    puzzle.add_killer_cage([(2, 4), (3, 4)], 10)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 6)], 19)
    puzzle.add_killer_cage([(3, 5), (4, 5), (4, 6)], 11)
    puzzle.add_killer_cage([(5, 5), (5, 6), (5, 7)], 21)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 23)
    puzzle.add_killer_cage([(6, 5), (7, 5), (8, 5)], 18)
    puzzle.add_killer_cage([(6, 3), (7, 3), (8, 3)], 21)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2)], 14)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2)], 24)

    return puzzle
