"""PuzzleMadness Killer Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/16'
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

    puzzle.add_killer_cage([(0, 0), (1, 0)], 6)
    puzzle.add_killer_cage([(0, 1), (1, 1)], 12)
    puzzle.add_killer_cage([(1, 2), (1, 3)], 13)
    puzzle.add_killer_cage([(0, 2), (0, 3), (0, 4), (1, 4)], 20)
    puzzle.add_killer_cage([(0, 5), (0, 6), (1, 5)], 13)
    puzzle.add_killer_cage([(0, 7), (0, 8)], 8)
    puzzle.add_killer_cage([(1, 7), (2, 7)], 12)
    puzzle.add_killer_cage([(1, 8), (2, 8)], 12)
    puzzle.add_killer_cage([(1, 6), (2, 6), (3, 5), (3, 6)], 23)
    puzzle.add_killer_cage([(2, 4), (2, 5)], 9)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 14)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 16)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7), (6, 8)], 17)
    puzzle.add_killer_cage([(7, 8), (8, 8)], 17)
    puzzle.add_killer_cage([(7, 7), (8, 7)], 7)
    puzzle.add_killer_cage([(7, 5), (7, 6)], 9)
    puzzle.add_killer_cage([(7, 4), (8, 4), (8, 5), (8, 6)], 14)
    puzzle.add_killer_cage([(7, 3), (8, 2), (8, 3)], 15)
    puzzle.add_killer_cage([(8, 0), (8, 1)], 13)
    puzzle.add_killer_cage([(6, 0), (7, 0)], 13)
    puzzle.add_killer_cage([(6, 1), (7, 1)], 7)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 2), (7, 2)], 17)
    puzzle.add_killer_cage([(6, 3), (6, 4)], 14)
    puzzle.add_killer_cage([(3, 3), (3, 4), (4, 4), (5, 4), (5, 5)], 27)
    puzzle.add_killer_cage([(4, 5), (4, 6), (5, 6)], 16)
    puzzle.add_killer_cage([(2, 0), (2, 1), (2, 2), (2, 3)], 20)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 12)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 15)
    puzzle.add_killer_cage([(3, 2), (4, 2), (4, 3)], 14)

    return puzzle
