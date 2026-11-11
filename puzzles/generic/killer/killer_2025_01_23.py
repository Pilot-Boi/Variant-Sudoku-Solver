"""PuzzleMadness Killer Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/23'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (0, 3)], 22)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7), (0, 8)], 16)
    puzzle.add_killer_cage([(1, 6), (1, 7)], 11)
    puzzle.add_killer_cage([(1, 8), (2, 8)], 14)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 8)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)], 34)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 15)
    puzzle.add_killer_cage([(0, 4), (1, 3), (1, 4), (1, 5)], 15)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 17)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1), (6, 0)], 19)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (8, 0)], 19)
    puzzle.add_killer_cage([(8, 1), (8, 2)], 12)
    puzzle.add_killer_cage([(6, 2), (6, 3), (7, 2)], 9)
    puzzle.add_killer_cage([(4, 2), (5, 2)], 9)
    puzzle.add_killer_cage([(4, 3), (5, 3)], 6)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4)], 17)
    puzzle.add_killer_cage([(6, 5), (6, 6), (7, 6)], 17)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 15)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 15)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 7)
    puzzle.add_killer_cage([(8, 6), (8, 7)], 6)
    puzzle.add_killer_cage([(6, 7), (7, 7), (7, 8), (8, 8)], 18)
    puzzle.add_killer_cage([(4, 7), (5, 7), (5, 8), (6, 8)], 26)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 8)], 20)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 4)
    puzzle.add_killer_cage([(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)], 21)
    puzzle.add_killer_cage([(4, 5), (5, 5)], 13)

    return puzzle
