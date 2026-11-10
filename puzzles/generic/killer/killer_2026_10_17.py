"""PuzzleMadness Killer Sudoku — 2026-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2026-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2026/10/17'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (1, 3)], 32)
    puzzle.add_killer_cage([(0, 3), (0, 4)], 12)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 9)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], 37)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 11)
    puzzle.add_killer_cage([(3, 6), (3, 7)], 16)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 11)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 6)
    puzzle.add_killer_cage([(5, 8), (6, 8)], 5)
    puzzle.add_killer_cage([(6, 7), (7, 7)], 15)
    puzzle.add_killer_cage([(7, 5), (7, 6), (7, 8), (8, 6), (8, 7), (8, 8)], 34)
    puzzle.add_killer_cage([(8, 4), (8, 5)], 6)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 11)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 9)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (8, 0), (8, 1)], 41)
    puzzle.add_killer_cage([(2, 4), (2, 5), (3, 4), (4, 4), (5, 4), (6, 3), (6, 4)], 35)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 6)
    puzzle.add_killer_cage([(3, 5), (4, 5)], 8)
    puzzle.add_killer_cage([(5, 5), (6, 5), (6, 6)], 12)
    puzzle.add_killer_cage([(4, 3), (5, 3)], 16)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 3)], 18)
    puzzle.add_killer_cage([(1, 1), (2, 1)], 8)
    puzzle.add_killer_cage([(2, 0), (3, 0)], 4)
    puzzle.add_killer_cage([(4, 0), (5, 0)], 14)
    puzzle.add_killer_cage([(5, 1), (5, 2)], 14)
    puzzle.add_killer_cage([(3, 2), (4, 2)], 11)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 3)
    puzzle.add_killer_cage([(7, 2)], 1)

    return puzzle
