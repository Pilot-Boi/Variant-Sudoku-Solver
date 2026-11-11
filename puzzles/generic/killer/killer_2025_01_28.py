"""PuzzleMadness Killer Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/28'
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

    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0)], 16)
    puzzle.add_killer_cage([(0, 1), (0, 2), (1, 1), (1, 2)], 16)
    puzzle.add_killer_cage([(1, 3), (2, 1), (2, 2), (2, 3)], 24)
    puzzle.add_killer_cage([(0, 3), (0, 4), (0, 5)], 18)
    puzzle.add_killer_cage([(1, 4), (1, 5), (1, 6), (1, 7)], 22)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8)], 15)
    puzzle.add_killer_cage([(1, 8), (2, 7), (2, 8)], 15)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 9)
    puzzle.add_killer_cage([(3, 4), (3, 5), (3, 6)], 20)
    puzzle.add_killer_cage([(3, 7), (4, 7), (5, 7)], 21)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 16)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 22)
    puzzle.add_killer_cage([(3, 1), (4, 1), (5, 1)], 12)
    puzzle.add_killer_cage([(3, 2), (3, 3)], 9)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 17)
    puzzle.add_killer_cage([(5, 5), (5, 6)], 9)
    puzzle.add_killer_cage([(5, 2), (5, 3), (5, 4)], 9)
    puzzle.add_killer_cage([(6, 0), (6, 1), (7, 0)], 10)
    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 12)
    puzzle.add_killer_cage([(7, 1), (7, 2), (7, 3), (7, 4)], 27)
    puzzle.add_killer_cage([(8, 3), (8, 4), (8, 5)], 11)
    puzzle.add_killer_cage([(7, 6), (7, 7), (8, 6), (8, 7)], 24)
    puzzle.add_killer_cage([(6, 8), (7, 8), (8, 8)], 11)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7), (7, 5)], 26)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 14)

    return puzzle
