"""PuzzleMadness Killer Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/7'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)], 19)
    puzzle.add_killer_cage([(1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 33)
    puzzle.add_killer_cage([(1, 3), (2, 3), (3, 2), (3, 3)], 21)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 11)
    puzzle.add_killer_cage([(0, 4), (0, 5), (0, 6), (0, 7)], 23)
    puzzle.add_killer_cage([(0, 8), (1, 8)], 13)
    puzzle.add_killer_cage([(1, 6), (1, 7), (2, 5), (2, 6)], 11)
    puzzle.add_killer_cage([(2, 7), (3, 7)], 9)
    puzzle.add_killer_cage([(2, 8), (3, 8)], 9)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 12)
    puzzle.add_killer_cage([(4, 8), (5, 8)], 9)
    puzzle.add_killer_cage([(6, 6), (6, 7), (6, 8), (7, 6), (7, 7)], 33)
    puzzle.add_killer_cage([(7, 8), (8, 5), (8, 6), (8, 7), (8, 8)], 16)
    puzzle.add_killer_cage([(7, 0), (8, 0)], 12)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3), (8, 4)], 24)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 7)
    puzzle.add_killer_cage([(5, 5), (5, 6), (6, 5), (7, 5)], 26)
    puzzle.add_killer_cage([(3, 6), (4, 6)], 15)
    puzzle.add_killer_cage([(3, 5), (4, 3), (4, 4), (4, 5), (5, 3)], 21)
    puzzle.add_killer_cage([(5, 4), (6, 4)], 4)
    puzzle.add_killer_cage([(2, 4), (3, 4)], 9)
    puzzle.add_killer_cage([(6, 2), (6, 3), (7, 1), (7, 2)], 18)
    puzzle.add_killer_cage([(5, 1), (6, 1)], 5)
    puzzle.add_killer_cage([(5, 0), (6, 0)], 15)
    puzzle.add_killer_cage([(3, 0), (4, 0)], 10)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 6)
    puzzle.add_killer_cage([(4, 2), (5, 2)], 14)

    return puzzle
