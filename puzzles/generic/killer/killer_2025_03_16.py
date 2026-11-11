"""PuzzleMadness Killer Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/3/16'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 21)
    puzzle.add_killer_cage([(1, 0), (1, 1)], 3)
    puzzle.add_killer_cage([(2, 0), (2, 1)], 7)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 24)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 10)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 21)
    puzzle.add_killer_cage([(5, 1), (6, 1), (7, 1)], 21)
    puzzle.add_killer_cage([(4, 1), (4, 2)], 10)
    puzzle.add_killer_cage([(2, 3), (3, 1), (3, 2), (3, 3)], 11)
    puzzle.add_killer_cage([(0, 3), (1, 2), (1, 3), (2, 2)], 23)
    puzzle.add_killer_cage([(0, 4), (1, 4), (1, 5)], 14)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 18)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 13)
    puzzle.add_killer_cage([(1, 7), (2, 7), (3, 7)], 21)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 15)
    puzzle.add_killer_cage([(4, 6), (4, 7)], 10)
    puzzle.add_killer_cage([(5, 5), (5, 6), (5, 7), (6, 5)], 15)
    puzzle.add_killer_cage([(6, 6), (7, 5), (7, 6), (8, 5)], 19)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 9)
    puzzle.add_killer_cage([(7, 7), (7, 8)], 13)
    puzzle.add_killer_cage([(6, 7), (6, 8)], 12)
    puzzle.add_killer_cage([(7, 3), (7, 4), (8, 4)], 16)
    puzzle.add_killer_cage([(6, 2), (6, 3), (7, 2)], 11)
    puzzle.add_killer_cage([(4, 3), (5, 2), (5, 3)], 10)
    puzzle.add_killer_cage([(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)], 28)
    puzzle.add_killer_cage([(3, 5), (3, 6), (4, 5)], 16)
    puzzle.add_killer_cage([(1, 6), (2, 5), (2, 6)], 14)

    return puzzle
