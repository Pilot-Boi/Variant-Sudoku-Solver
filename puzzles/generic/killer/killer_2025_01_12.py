"""PuzzleMadness Killer Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/12'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0)], 12)
    puzzle.add_killer_cage([(1, 1), (2, 0), (2, 1), (3, 0)], 24)
    puzzle.add_killer_cage([(1, 2), (2, 2)], 17)
    puzzle.add_killer_cage([(0, 3), (1, 3), (2, 3)], 11)
    puzzle.add_killer_cage([(0, 4), (1, 4)], 10)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 10)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 5), (1, 6), (1, 7)], 31)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 8), (4, 8)], 10)
    puzzle.add_killer_cage([(5, 8), (6, 7), (6, 8), (7, 7)], 18)
    puzzle.add_killer_cage([(7, 8), (8, 6), (8, 7), (8, 8)], 26)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7), (5, 6), (5, 7)], 28)
    puzzle.add_killer_cage([(6, 6), (7, 6)], 8)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 18)
    puzzle.add_killer_cage([(3, 5), (3, 6)], 8)
    puzzle.add_killer_cage([(3, 3), (3, 4)], 12)
    puzzle.add_killer_cage([(3, 1), (3, 2), (4, 1), (5, 1), (6, 1)], 27)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 12)
    puzzle.add_killer_cage([(6, 5), (7, 5), (8, 5)], 7)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 13)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 11)
    puzzle.add_killer_cage([(7, 1), (7, 2), (7, 3), (8, 0), (8, 1)], 23)
    puzzle.add_killer_cage([(4, 0), (5, 0), (6, 0), (7, 0)], 21)
    puzzle.add_killer_cage([(5, 2), (5, 3)], 9)
    puzzle.add_killer_cage([(5, 4), (5, 5)], 12)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 27)

    return puzzle
