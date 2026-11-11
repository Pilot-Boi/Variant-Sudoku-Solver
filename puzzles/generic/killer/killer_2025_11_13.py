"""PuzzleMadness Killer Sudoku — 2025-11-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-11-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/11/13'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 17)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 15)
    puzzle.add_killer_cage([(0, 3), (1, 1), (1, 2), (1, 3)], 23)
    puzzle.add_killer_cage([(0, 4), (0, 5), (0, 6)], 13)
    puzzle.add_killer_cage([(0, 7), (1, 6), (1, 7)], 14)
    puzzle.add_killer_cage([(0, 8), (1, 8)], 11)
    puzzle.add_killer_cage([(2, 5), (2, 6), (2, 7), (2, 8)], 20)
    puzzle.add_killer_cage([(1, 4), (1, 5), (2, 4)], 9)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3)], 13)
    puzzle.add_killer_cage([(3, 0), (3, 1)], 13)
    puzzle.add_killer_cage([(3, 2), (3, 3)], 10)
    puzzle.add_killer_cage([(3, 4), (3, 5)], 7)
    puzzle.add_killer_cage([(3, 6), (4, 6)], 9)
    puzzle.add_killer_cage([(3, 7), (4, 7)], 8)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 14)
    puzzle.add_killer_cage([(5, 7), (5, 8)], 10)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 10)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 11)
    puzzle.add_killer_cage([(7, 5), (7, 6), (7, 7), (8, 5)], 25)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7)], 15)
    puzzle.add_killer_cage([(5, 5), (5, 6)], 12)
    puzzle.add_killer_cage([(4, 3), (4, 4), (4, 5)], 16)
    puzzle.add_killer_cage([(5, 3), (5, 4)], 11)
    puzzle.add_killer_cage([(6, 4), (7, 3), (7, 4)], 15)
    puzzle.add_killer_cage([(8, 2), (8, 3), (8, 4)], 15)
    puzzle.add_killer_cage([(7, 1), (7, 2), (8, 1)], 20)
    puzzle.add_killer_cage([(7, 0), (8, 0)], 8)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2), (6, 3)], 16)
    puzzle.add_killer_cage([(4, 0), (5, 0)], 8)
    puzzle.add_killer_cage([(4, 1), (5, 1)], 14)
    puzzle.add_killer_cage([(4, 2), (5, 2)], 3)

    return puzzle
