"""PuzzleMadness Killer Sudoku — 2025-01-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/26'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (0, 3)], 18)
    puzzle.add_killer_cage([(1, 0), (1, 1), (1, 2), (2, 0)], 24)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3), (3, 3)], 19)
    puzzle.add_killer_cage([(0, 4), (1, 3), (1, 4)], 14)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 15)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8), (2, 7)], 25)
    puzzle.add_killer_cage([(2, 8), (3, 8), (4, 8)], 15)
    puzzle.add_killer_cage([(4, 7), (5, 6), (5, 7), (5, 8)], 19)
    puzzle.add_killer_cage([(2, 6), (3, 6), (3, 7), (4, 6)], 22)
    puzzle.add_killer_cage([(1, 5), (1, 6), (2, 5)], 15)
    puzzle.add_killer_cage([(2, 4), (3, 4)], 9)
    puzzle.add_killer_cage([(3, 5), (4, 3), (4, 4), (4, 5), (5, 3)], 15)
    puzzle.add_killer_cage([(5, 4), (6, 4)], 17)
    puzzle.add_killer_cage([(5, 5), (6, 5), (6, 6), (6, 7)], 23)
    puzzle.add_killer_cage([(6, 8), (7, 6), (7, 7), (7, 8)], 25)
    puzzle.add_killer_cage([(8, 5), (8, 6), (8, 7), (8, 8)], 11)
    puzzle.add_killer_cage([(7, 4), (7, 5), (8, 4)], 14)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (8, 0)], 23)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 18)
    puzzle.add_killer_cage([(6, 3), (7, 2), (7, 3)], 13)
    puzzle.add_killer_cage([(4, 2), (5, 1), (5, 2), (6, 2)], 21)
    puzzle.add_killer_cage([(3, 0), (3, 1), (3, 2), (4, 1)], 21)
    puzzle.add_killer_cage([(4, 0), (5, 0), (6, 0)], 9)

    return puzzle
