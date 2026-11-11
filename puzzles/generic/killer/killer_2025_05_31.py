"""PuzzleMadness Killer Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/5/31'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 17)
    puzzle.add_killer_cage([(0, 3), (0, 4), (1, 3)], 12)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 17)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 14)
    puzzle.add_killer_cage([(1, 7), (2, 6), (2, 7)], 17)
    puzzle.add_killer_cage([(1, 4), (1, 5), (1, 6)], 16)
    puzzle.add_killer_cage([(1, 0), (2, 0), (3, 0)], 13)
    puzzle.add_killer_cage([(1, 1), (1, 2), (2, 1)], 10)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4)], 22)
    puzzle.add_killer_cage([(2, 5), (3, 5)], 4)
    puzzle.add_killer_cage([(3, 2), (3, 3), (3, 4)], 12)
    puzzle.add_killer_cage([(3, 1), (4, 0), (4, 1)], 22)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 25)
    puzzle.add_killer_cage([(3, 6), (3, 7), (3, 8)], 17)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 7)], 11)
    puzzle.add_killer_cage([(5, 8), (6, 8), (7, 8)], 17)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 13)
    puzzle.add_killer_cage([(6, 7), (7, 6), (7, 7)], 16)
    puzzle.add_killer_cage([(5, 4), (5, 5), (5, 6)], 23)
    puzzle.add_killer_cage([(6, 4), (6, 5), (6, 6)], 12)
    puzzle.add_killer_cage([(7, 5), (8, 4), (8, 5)], 19)
    puzzle.add_killer_cage([(7, 2), (7, 3), (7, 4)], 14)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 14)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 20)
    puzzle.add_killer_cage([(6, 1), (6, 2), (7, 1)], 14)
    puzzle.add_killer_cage([(5, 3), (6, 3)], 3)
    puzzle.add_killer_cage([(5, 0), (5, 1), (5, 2)], 11)

    return puzzle
