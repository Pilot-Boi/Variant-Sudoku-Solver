"""PuzzleMadness Killer Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/8/15'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 12)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 7)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 15)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3), (2, 4), (3, 3)], 29)
    puzzle.add_killer_cage([(0, 3), (1, 3)], 10)
    puzzle.add_killer_cage([(0, 4), (1, 4)], 10)
    puzzle.add_killer_cage([(0, 5), (0, 6), (1, 5)], 19)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7)], 20)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 6), (3, 7), (3, 8)], 26)
    puzzle.add_killer_cage([(2, 6), (2, 7)], 11)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5)], 15)
    puzzle.add_killer_cage([(3, 0), (3, 1), (3, 2), (4, 0), (4, 1)], 21)
    puzzle.add_killer_cage([(5, 0), (5, 1), (5, 2), (6, 0), (7, 0)], 31)
    puzzle.add_killer_cage([(7, 1), (7, 2), (8, 0), (8, 1)], 17)
    puzzle.add_killer_cage([(6, 1), (6, 2)], 8)
    puzzle.add_killer_cage([(7, 3), (8, 2), (8, 3)], 22)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 9)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 10)
    puzzle.add_killer_cage([(7, 6), (7, 7)], 14)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 6)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 16)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 6), (5, 7), (5, 8)], 22)
    puzzle.add_killer_cage([(5, 5), (6, 4), (6, 5), (6, 6), (6, 7)], 28)
    puzzle.add_killer_cage([(5, 3), (5, 4), (6, 3)], 11)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 16)

    return puzzle
