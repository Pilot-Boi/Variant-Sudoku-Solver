"""PuzzleMadness Killer Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/30'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0)], 10)
    puzzle.add_killer_cage([(0, 2), (0, 3), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)], 34)
    puzzle.add_killer_cage([(0, 4), (1, 3), (1, 4)], 18)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 14)
    puzzle.add_killer_cage([(0, 8), (1, 6), (1, 7), (1, 8)], 21)
    puzzle.add_killer_cage([(1, 5), (2, 5), (2, 6)], 14)
    puzzle.add_killer_cage([(2, 7), (2, 8), (3, 7)], 19)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 12)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 12)
    puzzle.add_killer_cage([(5, 8), (6, 7), (6, 8), (7, 6), (7, 7), (8, 5), (8, 6)], 36)
    puzzle.add_killer_cage([(7, 8), (8, 7), (8, 8)], 13)
    puzzle.add_killer_cage([(2, 2), (3, 2)], 10)
    puzzle.add_killer_cage([(2, 3), (2, 4)], 10)
    puzzle.add_killer_cage([(3, 3), (3, 4), (4, 4), (5, 4), (5, 5)], 22)
    puzzle.add_killer_cage([(3, 5), (3, 6)], 11)
    puzzle.add_killer_cage([(4, 5), (4, 6)], 9)
    puzzle.add_killer_cage([(5, 6), (6, 6)], 5)
    puzzle.add_killer_cage([(6, 4), (6, 5)], 7)
    puzzle.add_killer_cage([(7, 4), (7, 5), (8, 4)], 19)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 14)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2), (8, 0)], 17)
    puzzle.add_killer_cage([(6, 2), (6, 3), (7, 3)], 16)
    puzzle.add_killer_cage([(5, 1), (6, 0), (6, 1)], 19)
    puzzle.add_killer_cage([(5, 2), (5, 3)], 12)
    puzzle.add_killer_cage([(4, 2), (4, 3)], 12)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 3)
    puzzle.add_killer_cage([(4, 0), (5, 0)], 16)

    return puzzle
