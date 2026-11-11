"""PuzzleMadness Killer Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/7/1'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (0, 3)], 19)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7), (0, 8)], 17)
    puzzle.add_killer_cage([(1, 6), (1, 7)], 8)
    puzzle.add_killer_cage([(1, 8), (2, 8)], 10)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 10)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)], 41)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 8)
    puzzle.add_killer_cage([(0, 4), (1, 3), (1, 4), (1, 5)], 22)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 17)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1), (6, 0)], 20)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (8, 0)], 15)
    puzzle.add_killer_cage([(8, 1), (8, 2)], 7)
    puzzle.add_killer_cage([(6, 2), (6, 3), (7, 2)], 19)
    puzzle.add_killer_cage([(4, 2), (5, 2)], 15)
    puzzle.add_killer_cage([(4, 3), (5, 3)], 12)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4)], 12)
    puzzle.add_killer_cage([(6, 5), (6, 6), (7, 6)], 13)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 13)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 13)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 10)
    puzzle.add_killer_cage([(8, 6), (8, 7)], 7)
    puzzle.add_killer_cage([(6, 7), (7, 7), (7, 8), (8, 8)], 18)
    puzzle.add_killer_cage([(4, 7), (5, 7), (5, 8), (6, 8)], 22)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 8)], 15)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 10)
    puzzle.add_killer_cage([(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)], 20)
    puzzle.add_killer_cage([(4, 5), (5, 5)], 12)

    return puzzle
