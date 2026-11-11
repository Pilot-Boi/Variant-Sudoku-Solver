"""PuzzleMadness Killer Sudoku — 2025-10-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-10-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/10/13'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 18)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 6)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 4)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3), (2, 4), (3, 3)], 27)
    puzzle.add_killer_cage([(0, 3), (1, 3)], 7)
    puzzle.add_killer_cage([(0, 4), (1, 4)], 13)
    puzzle.add_killer_cage([(0, 5), (0, 6), (1, 5)], 16)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7)], 20)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 6), (3, 7), (3, 8)], 35)
    puzzle.add_killer_cage([(2, 6), (2, 7)], 10)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5)], 14)
    puzzle.add_killer_cage([(3, 0), (3, 1), (3, 2), (4, 0), (4, 1)], 24)
    puzzle.add_killer_cage([(5, 0), (5, 1), (5, 2), (6, 0), (7, 0)], 30)
    puzzle.add_killer_cage([(7, 1), (7, 2), (8, 0), (8, 1)], 20)
    puzzle.add_killer_cage([(6, 1), (6, 2)], 6)
    puzzle.add_killer_cage([(7, 3), (8, 2), (8, 3)], 22)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 4)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 7)
    puzzle.add_killer_cage([(7, 6), (7, 7)], 11)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 14)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 11)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 6), (5, 7), (5, 8)], 21)
    puzzle.add_killer_cage([(5, 5), (6, 4), (6, 5), (6, 6), (6, 7)], 24)
    puzzle.add_killer_cage([(5, 3), (5, 4), (6, 3)], 15)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 26)

    return puzzle
