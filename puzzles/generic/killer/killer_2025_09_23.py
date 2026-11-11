"""PuzzleMadness Killer Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/9/23'
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

    puzzle.add_killer_cage([(0, 0), (1, 0)], 10)
    puzzle.add_killer_cage([(0, 1), (1, 1)], 13)
    puzzle.add_killer_cage([(1, 2), (1, 3)], 8)
    puzzle.add_killer_cage([(0, 2), (0, 3), (0, 4), (1, 4)], 23)
    puzzle.add_killer_cage([(0, 5), (0, 6), (1, 5)], 11)
    puzzle.add_killer_cage([(0, 7), (0, 8)], 9)
    puzzle.add_killer_cage([(1, 7), (2, 7)], 14)
    puzzle.add_killer_cage([(1, 8), (2, 8)], 12)
    puzzle.add_killer_cage([(1, 6), (2, 6), (3, 5), (3, 6)], 16)
    puzzle.add_killer_cage([(2, 4), (2, 5)], 6)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 20)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 10)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7), (6, 8)], 22)
    puzzle.add_killer_cage([(7, 8), (8, 8)], 7)
    puzzle.add_killer_cage([(7, 7), (8, 7)], 11)
    puzzle.add_killer_cage([(7, 5), (7, 6)], 8)
    puzzle.add_killer_cage([(7, 4), (8, 4), (8, 5), (8, 6)], 24)
    puzzle.add_killer_cage([(7, 3), (8, 2), (8, 3)], 9)
    puzzle.add_killer_cage([(8, 0), (8, 1)], 8)
    puzzle.add_killer_cage([(6, 0), (7, 0)], 10)
    puzzle.add_killer_cage([(6, 1), (7, 1)], 13)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 2), (7, 2)], 24)
    puzzle.add_killer_cage([(6, 3), (6, 4)], 12)
    puzzle.add_killer_cage([(3, 3), (3, 4), (4, 4), (5, 4), (5, 5)], 22)
    puzzle.add_killer_cage([(4, 5), (4, 6), (5, 6)], 17)
    puzzle.add_killer_cage([(2, 0), (2, 1), (2, 2), (2, 3)], 23)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 12)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 14)
    puzzle.add_killer_cage([(3, 2), (4, 2), (4, 3)], 17)

    return puzzle
