"""PuzzleMadness Killer Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/10/3'
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

    puzzle.add_killer_cage([(0, 0), (1, 0)], 6)
    puzzle.add_killer_cage([(0, 1), (0, 2)], 4)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 15)
    puzzle.add_killer_cage([(0, 3), (0, 4)], 11)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 12)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 8)], 19)
    puzzle.add_killer_cage([(1, 6), (1, 7), (2, 6), (2, 7)], 18)
    puzzle.add_killer_cage([(1, 3), (1, 4)], 9)
    puzzle.add_killer_cage([(1, 5), (2, 5), (3, 4), (3, 5), (3, 6), (3, 7), (4, 4), (4, 5)], 37)
    puzzle.add_killer_cage([(2, 8), (3, 8)], 4)
    puzzle.add_killer_cage([(4, 8), (5, 8)], 16)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 6)
    puzzle.add_killer_cage([(4, 6), (5, 6), (6, 6)], 18)
    puzzle.add_killer_cage([(6, 7), (7, 7)], 13)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 10)
    puzzle.add_killer_cage([(8, 7), (8, 8)], 5)
    puzzle.add_killer_cage([(7, 6), (8, 4), (8, 5), (8, 6)], 24)
    puzzle.add_killer_cage([(7, 4), (7, 5)], 11)
    puzzle.add_killer_cage([(5, 5), (6, 4), (6, 5)], 12)
    puzzle.add_killer_cage([(2, 0), (2, 1), (3, 0), (4, 0)], 19)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 17)
    puzzle.add_killer_cage([(3, 2), (3, 3), (4, 2)], 15)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4)], 15)
    puzzle.add_killer_cage([(5, 0), (5, 1), (6, 0)], 16)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1)], 31)
    puzzle.add_killer_cage([(4, 3), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3)], 27)
    puzzle.add_killer_cage([(7, 3), (8, 2), (8, 3)], 15)

    return puzzle
