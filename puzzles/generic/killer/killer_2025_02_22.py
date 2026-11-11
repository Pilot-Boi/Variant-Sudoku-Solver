"""PuzzleMadness Killer Sudoku — 2025-02-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-02-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/2/22'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0)], 15)
    puzzle.add_killer_cage([(1, 1), (1, 2), (2, 0), (2, 1)], 23)
    puzzle.add_killer_cage([(0, 3), (1, 3), (1, 4)], 10)
    puzzle.add_killer_cage([(0, 4), (0, 5)], 12)
    puzzle.add_killer_cage([(0, 6), (0, 7), (1, 5), (1, 6)], 19)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 19)
    puzzle.add_killer_cage([(1, 7), (2, 6), (2, 7), (3, 6), (4, 6)], 24)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 10)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 15)
    puzzle.add_killer_cage([(6, 7), (6, 8), (7, 6), (7, 7)], 26)
    puzzle.add_killer_cage([(7, 8), (8, 6), (8, 7), (8, 8)], 16)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4), (3, 2)], 27)
    puzzle.add_killer_cage([(2, 5), (3, 5), (4, 5)], 17)
    puzzle.add_killer_cage([(3, 3), (3, 4), (4, 4), (5, 4), (5, 5)], 22)
    puzzle.add_killer_cage([(4, 3), (5, 3), (6, 3)], 18)
    puzzle.add_killer_cage([(5, 6), (6, 4), (6, 5), (6, 6)], 11)
    puzzle.add_killer_cage([(7, 4), (7, 5), (8, 5)], 18)
    puzzle.add_killer_cage([(8, 3), (8, 4)], 9)
    puzzle.add_killer_cage([(7, 2), (7, 3), (8, 1), (8, 2)], 20)
    puzzle.add_killer_cage([(4, 2), (5, 2), (6, 1), (6, 2), (7, 1)], 35)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 16)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 9)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 14)

    return puzzle
