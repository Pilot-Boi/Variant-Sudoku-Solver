"""PuzzleMadness Killer Sudoku — 2025-09-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-09-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/9/28'
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

    puzzle.add_killer_cage([(0, 0), (1, 0)], 9)
    puzzle.add_killer_cage([(0, 1), (0, 2)], 9)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 14)
    puzzle.add_killer_cage([(0, 3), (0, 4)], 12)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 10)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 8)], 14)
    puzzle.add_killer_cage([(1, 6), (1, 7), (2, 6), (2, 7)], 21)
    puzzle.add_killer_cage([(1, 3), (1, 4)], 12)
    puzzle.add_killer_cage([(1, 5), (2, 5), (3, 4), (3, 5), (3, 6), (3, 7), (4, 4), (4, 5)], 37)
    puzzle.add_killer_cage([(2, 8), (3, 8)], 13)
    puzzle.add_killer_cage([(4, 8), (5, 8)], 10)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 6)
    puzzle.add_killer_cage([(4, 6), (5, 6), (6, 6)], 17)
    puzzle.add_killer_cage([(6, 7), (7, 7)], 17)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 11)
    puzzle.add_killer_cage([(8, 7), (8, 8)], 3)
    puzzle.add_killer_cage([(7, 6), (8, 4), (8, 5), (8, 6)], 21)
    puzzle.add_killer_cage([(7, 4), (7, 5)], 9)
    puzzle.add_killer_cage([(5, 5), (6, 4), (6, 5)], 11)
    puzzle.add_killer_cage([(2, 0), (2, 1), (3, 0), (4, 0)], 22)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 5)
    puzzle.add_killer_cage([(3, 2), (3, 3), (4, 2)], 9)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4)], 17)
    puzzle.add_killer_cage([(5, 0), (5, 1), (6, 0)], 15)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1)], 33)
    puzzle.add_killer_cage([(4, 3), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3)], 30)
    puzzle.add_killer_cage([(7, 3), (8, 2), (8, 3)], 18)

    return puzzle
