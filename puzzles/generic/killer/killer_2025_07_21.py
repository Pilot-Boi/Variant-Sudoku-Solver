"""PuzzleMadness Killer Sudoku — 2025-07-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-07-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/7/21'
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

    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0)], 17)
    puzzle.add_killer_cage([(0, 1), (1, 1), (1, 2)], 13)
    puzzle.add_killer_cage([(2, 1), (3, 1), (3, 2)], 18)
    puzzle.add_killer_cage([(3, 0), (4, 0), (4, 1), (5, 0)], 13)
    puzzle.add_killer_cage([(3, 3), (4, 2), (4, 3), (5, 3)], 17)
    puzzle.add_killer_cage([(3, 6), (4, 4), (4, 5), (4, 6), (5, 6)], 27)
    puzzle.add_killer_cage([(3, 8), (4, 7), (4, 8), (5, 8)], 21)
    puzzle.add_killer_cage([(6, 8), (7, 7), (7, 8), (8, 8)], 17)
    puzzle.add_killer_cage([(7, 3), (7, 4), (7, 5), (7, 6)], 22)
    puzzle.add_killer_cage([(5, 1), (5, 2), (6, 1)], 16)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 17)
    puzzle.add_killer_cage([(7, 1), (7, 2), (8, 1)], 22)
    puzzle.add_killer_cage([(8, 2), (8, 3), (8, 4)], 12)
    puzzle.add_killer_cage([(8, 5), (8, 6), (8, 7)], 12)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 15)
    puzzle.add_killer_cage([(5, 4), (5, 5), (6, 5)], 12)
    puzzle.add_killer_cage([(5, 7), (6, 6), (6, 7)], 12)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5)], 18)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4)], 20)
    puzzle.add_killer_cage([(0, 2), (0, 3), (0, 4)], 16)
    puzzle.add_killer_cage([(1, 3), (1, 4), (1, 5), (1, 6)], 14)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 17)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8), (2, 8)], 25)
    puzzle.add_killer_cage([(2, 6), (2, 7), (3, 7)], 12)

    return puzzle
