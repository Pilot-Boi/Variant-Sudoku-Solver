"""PuzzleMadness Killer Sudoku — 2025-04-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-04-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/4/18'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0)], 24)
    puzzle.add_killer_cage([(1, 1), (2, 0), (2, 1), (3, 0)], 19)
    puzzle.add_killer_cage([(1, 2), (2, 2)], 11)
    puzzle.add_killer_cage([(0, 3), (1, 3), (2, 3)], 12)
    puzzle.add_killer_cage([(0, 4), (1, 4)], 16)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 3)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 5), (1, 6), (1, 7)], 24)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 8), (4, 8)], 11)
    puzzle.add_killer_cage([(5, 8), (6, 7), (6, 8), (7, 7)], 26)
    puzzle.add_killer_cage([(7, 8), (8, 6), (8, 7), (8, 8)], 14)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7), (5, 6), (5, 7)], 29)
    puzzle.add_killer_cage([(6, 6), (7, 6)], 14)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 21)
    puzzle.add_killer_cage([(3, 5), (3, 6)], 13)
    puzzle.add_killer_cage([(3, 3), (3, 4)], 6)
    puzzle.add_killer_cage([(3, 1), (3, 2), (4, 1), (5, 1), (6, 1)], 20)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 9)
    puzzle.add_killer_cage([(6, 5), (7, 5), (8, 5)], 19)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 5)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 12)
    puzzle.add_killer_cage([(7, 1), (7, 2), (7, 3), (8, 0), (8, 1)], 35)
    puzzle.add_killer_cage([(4, 0), (5, 0), (6, 0), (7, 0)], 18)
    puzzle.add_killer_cage([(5, 2), (5, 3)], 7)
    puzzle.add_killer_cage([(5, 4), (5, 5)], 13)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 24)

    return puzzle
