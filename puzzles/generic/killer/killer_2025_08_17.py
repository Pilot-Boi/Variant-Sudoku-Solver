"""PuzzleMadness Killer Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/8/17'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)], 23)
    puzzle.add_killer_cage([(0, 3), (0, 4), (0, 5), (1, 4)], 17)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8), (1, 5), (1, 6)], 28)
    puzzle.add_killer_cage([(1, 7), (1, 8), (2, 8)], 16)
    puzzle.add_killer_cage([(2, 7), (3, 7)], 11)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 12)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 5)
    puzzle.add_killer_cage([(5, 8), (6, 8)], 8)
    puzzle.add_killer_cage([(6, 7), (7, 7), (7, 8)], 16)
    puzzle.add_killer_cage([(8, 7), (8, 8)], 8)
    puzzle.add_killer_cage([(7, 6), (8, 6)], 13)
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0)], 22)
    puzzle.add_killer_cage([(2, 1), (3, 1)], 9)
    puzzle.add_killer_cage([(3, 0), (4, 0)], 6)
    puzzle.add_killer_cage([(5, 0), (6, 0)], 12)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1)], 13)
    puzzle.add_killer_cage([(8, 0), (8, 1)], 13)
    puzzle.add_killer_cage([(7, 2), (7, 3), (8, 2), (8, 3)], 17)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 4), (8, 4)], 35)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 15)
    puzzle.add_killer_cage([(2, 2), (2, 3)], 10)
    puzzle.add_killer_cage([(3, 2), (4, 2)], 10)
    puzzle.add_killer_cage([(3, 3), (4, 3)], 12)
    puzzle.add_killer_cage([(4, 1), (5, 1)], 12)
    puzzle.add_killer_cage([(4, 4), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)], 31)
    puzzle.add_killer_cage([(2, 4), (3, 4)], 7)
    puzzle.add_killer_cage([(2, 5), (2, 6)], 9)
    puzzle.add_killer_cage([(3, 5), (4, 5)], 5)
    puzzle.add_killer_cage([(3, 6), (4, 6)], 10)

    return puzzle
