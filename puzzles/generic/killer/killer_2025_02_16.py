"""PuzzleMadness Killer Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/2/16'
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

    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0)], 10)
    puzzle.add_killer_cage([(0, 1), (0, 2), (0, 3)], 17)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3)], 19)
    puzzle.add_killer_cage([(2, 1), (3, 1), (4, 1)], 19)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 16)
    puzzle.add_killer_cage([(5, 1), (6, 0), (6, 1)], 18)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2)], 18)
    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 11)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4), (3, 4)], 23)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 9)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 19)
    puzzle.add_killer_cage([(1, 5), (1, 6), (1, 7)], 13)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 5)], 19)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 21)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 8)
    puzzle.add_killer_cage([(5, 7), (6, 7), (6, 8)], 14)
    puzzle.add_killer_cage([(7, 6), (7, 7), (7, 8)], 18)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 14)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 10)
    puzzle.add_killer_cage([(4, 5), (5, 5), (6, 5), (6, 6)], 22)
    puzzle.add_killer_cage([(3, 6), (4, 6), (5, 6)], 13)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 22)
    puzzle.add_killer_cage([(4, 3), (5, 3), (6, 2), (6, 3)], 22)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 14)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 3)], 10)
    puzzle.add_killer_cage([(3, 2), (4, 2), (5, 2)], 6)

    return puzzle
