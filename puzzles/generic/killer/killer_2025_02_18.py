"""PuzzleMadness Killer Sudoku — 2025-02-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-02-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/2/18'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0)], 15)
    puzzle.add_killer_cage([(0, 2), (0, 3), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)], 31)
    puzzle.add_killer_cage([(0, 4), (1, 3), (1, 4)], 13)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 16)
    puzzle.add_killer_cage([(0, 8), (1, 6), (1, 7), (1, 8)], 23)
    puzzle.add_killer_cage([(1, 5), (2, 5), (2, 6)], 18)
    puzzle.add_killer_cage([(2, 7), (2, 8), (3, 7)], 17)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 13)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 3)
    puzzle.add_killer_cage([(5, 8), (6, 7), (6, 8), (7, 6), (7, 7), (8, 5), (8, 6)], 36)
    puzzle.add_killer_cage([(7, 8), (8, 7), (8, 8)], 18)
    puzzle.add_killer_cage([(2, 2), (3, 2)], 11)
    puzzle.add_killer_cage([(2, 3), (2, 4)], 5)
    puzzle.add_killer_cage([(3, 3), (3, 4), (4, 4), (5, 4), (5, 5)], 29)
    puzzle.add_killer_cage([(3, 5), (3, 6)], 5)
    puzzle.add_killer_cage([(4, 5), (4, 6)], 7)
    puzzle.add_killer_cage([(5, 6), (6, 6)], 14)
    puzzle.add_killer_cage([(6, 4), (6, 5)], 11)
    puzzle.add_killer_cage([(7, 4), (7, 5), (8, 4)], 9)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 9)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2), (8, 0)], 28)
    puzzle.add_killer_cage([(6, 2), (6, 3), (7, 3)], 14)
    puzzle.add_killer_cage([(5, 1), (6, 0), (6, 1)], 18)
    puzzle.add_killer_cage([(5, 2), (5, 3)], 6)
    puzzle.add_killer_cage([(4, 2), (4, 3)], 17)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 15)
    puzzle.add_killer_cage([(4, 0), (5, 0)], 4)

    return puzzle
