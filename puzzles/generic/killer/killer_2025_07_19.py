"""PuzzleMadness Killer Sudoku — 2025-07-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-07-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/7/19'
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

    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0)], 14)
    puzzle.add_killer_cage([(0, 1), (0, 2), (0, 3)], 18)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3)], 7)
    puzzle.add_killer_cage([(2, 1), (3, 1), (4, 1)], 16)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 18)
    puzzle.add_killer_cage([(5, 1), (6, 0), (6, 1)], 18)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2)], 14)
    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 12)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4), (3, 4)], 21)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 20)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 14)
    puzzle.add_killer_cage([(1, 5), (1, 6), (1, 7)], 16)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 5)], 8)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 11)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 21)
    puzzle.add_killer_cage([(5, 7), (6, 7), (6, 8)], 14)
    puzzle.add_killer_cage([(7, 6), (7, 7), (7, 8)], 12)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 15)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 17)
    puzzle.add_killer_cage([(4, 5), (5, 5), (6, 5), (6, 6)], 15)
    puzzle.add_killer_cage([(3, 6), (4, 6), (5, 6)], 17)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 24)
    puzzle.add_killer_cage([(4, 3), (5, 3), (6, 2), (6, 3)], 14)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 12)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 3)], 18)
    puzzle.add_killer_cage([(3, 2), (4, 2), (5, 2)], 19)

    return puzzle
