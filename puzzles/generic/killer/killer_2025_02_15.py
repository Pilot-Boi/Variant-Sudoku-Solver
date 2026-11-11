"""PuzzleMadness Killer Sudoku — 2025-02-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-02-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/2/15'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 15)
    puzzle.add_killer_cage([(0, 3), (0, 4), (1, 3)], 10)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 14)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 22)
    puzzle.add_killer_cage([(1, 7), (2, 6), (2, 7)], 11)
    puzzle.add_killer_cage([(1, 4), (1, 5), (1, 6)], 19)
    puzzle.add_killer_cage([(1, 0), (2, 0), (3, 0)], 14)
    puzzle.add_killer_cage([(1, 1), (1, 2), (2, 1)], 15)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4)], 16)
    puzzle.add_killer_cage([(2, 5), (3, 5)], 12)
    puzzle.add_killer_cage([(3, 2), (3, 3), (3, 4)], 12)
    puzzle.add_killer_cage([(3, 1), (4, 0), (4, 1)], 8)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 30)
    puzzle.add_killer_cage([(3, 6), (3, 7), (3, 8)], 17)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 7)], 18)
    puzzle.add_killer_cage([(5, 8), (6, 8), (7, 8)], 7)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 17)
    puzzle.add_killer_cage([(6, 7), (7, 6), (7, 7)], 19)
    puzzle.add_killer_cage([(5, 4), (5, 5), (5, 6)], 13)
    puzzle.add_killer_cage([(6, 4), (6, 5), (6, 6)], 17)
    puzzle.add_killer_cage([(7, 5), (8, 4), (8, 5)], 8)
    puzzle.add_killer_cage([(7, 2), (7, 3), (7, 4)], 12)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 16)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 19)
    puzzle.add_killer_cage([(6, 1), (6, 2), (7, 1)], 17)
    puzzle.add_killer_cage([(5, 3), (6, 3)], 10)
    puzzle.add_killer_cage([(5, 0), (5, 1), (5, 2)], 17)

    return puzzle
