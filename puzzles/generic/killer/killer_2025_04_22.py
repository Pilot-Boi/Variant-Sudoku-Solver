"""PuzzleMadness Killer Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/4/22'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 13)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 11)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 10)
    puzzle.add_killer_cage([(2, 1), (2, 2)], 11)
    puzzle.add_killer_cage([(0, 3), (0, 4), (1, 3)], 7)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 14)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7), (2, 6), (3, 6)], 32)
    puzzle.add_killer_cage([(1, 8), (2, 7), (2, 8)], 8)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 16)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 20)
    puzzle.add_killer_cage([(6, 6), (6, 7)], 10)
    puzzle.add_killer_cage([(7, 6), (7, 7)], 10)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 15)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 10)
    puzzle.add_killer_cage([(7, 5), (8, 4), (8, 5)], 10)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 9)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 15)
    puzzle.add_killer_cage([(5, 2), (6, 2), (7, 1), (7, 2), (8, 0), (8, 1)], 28)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 16)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 9)
    puzzle.add_killer_cage([(6, 0), (6, 1), (7, 0)], 14)
    puzzle.add_killer_cage([(3, 2), (4, 2)], 17)
    puzzle.add_killer_cage([(3, 3), (4, 3)], 7)
    puzzle.add_killer_cage([(2, 3), (2, 4)], 13)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 14)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5), (4, 4), (5, 3), (5, 4), (6, 3)], 39)
    puzzle.add_killer_cage([(6, 4), (6, 5)], 12)
    puzzle.add_killer_cage([(4, 5), (5, 5)], 7)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 8)

    return puzzle
