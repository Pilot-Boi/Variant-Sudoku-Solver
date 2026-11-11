"""PuzzleMadness Killer Sudoku — 2025-08-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-08-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/8/4'
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

    puzzle.add_killer_cage([(0, 0), (1, 0)], 14)
    puzzle.add_killer_cage([(2, 0), (3, 0), (4, 0)], 10)
    puzzle.add_killer_cage([(5, 0), (5, 1)], 10)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)], 29)
    puzzle.add_killer_cage([(6, 1), (6, 2), (7, 1), (7, 2)], 16)
    puzzle.add_killer_cage([(0, 1), (0, 2), (1, 1)], 12)
    puzzle.add_killer_cage([(1, 2), (2, 1), (2, 2)], 14)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 13)
    puzzle.add_killer_cage([(3, 2), (3, 3), (3, 4)], 13)
    puzzle.add_killer_cage([(1, 4), (2, 3), (2, 4)], 13)
    puzzle.add_killer_cage([(0, 3), (1, 3)], 16)
    puzzle.add_killer_cage([(0, 4), (0, 5)], 7)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8), (1, 8), (2, 8)], 27)
    puzzle.add_killer_cage([(1, 5), (1, 6), (1, 7), (2, 7), (3, 7)], 29)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 7)
    puzzle.add_killer_cage([(5, 7), (5, 8)], 6)
    puzzle.add_killer_cage([(4, 6), (4, 7), (5, 6)], 15)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 5), (3, 6)], 22)
    puzzle.add_killer_cage([(4, 5), (5, 5), (6, 5)], 11)
    puzzle.add_killer_cage([(6, 6), (6, 7), (7, 6)], 19)
    puzzle.add_killer_cage([(6, 8), (7, 7), (7, 8)], 12)
    puzzle.add_killer_cage([(8, 7), (8, 8)], 9)
    puzzle.add_killer_cage([(8, 4), (8, 5), (8, 6)], 22)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 4)
    puzzle.add_killer_cage([(7, 4), (7, 5)], 10)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (5, 4), (6, 4)], 27)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 3)], 18)

    return puzzle
