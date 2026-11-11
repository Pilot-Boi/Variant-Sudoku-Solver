"""PuzzleMadness Killer Sudoku — 2025-10-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-10-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/10/28'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 7)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 15)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 13)
    puzzle.add_killer_cage([(2, 1), (2, 2)], 10)
    puzzle.add_killer_cage([(0, 3), (0, 4), (1, 3)], 12)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 16)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7), (2, 6), (3, 6)], 28)
    puzzle.add_killer_cage([(1, 8), (2, 7), (2, 8)], 12)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 18)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 19)
    puzzle.add_killer_cage([(6, 6), (6, 7)], 8)
    puzzle.add_killer_cage([(7, 6), (7, 7)], 11)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 16)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 10)
    puzzle.add_killer_cage([(7, 5), (8, 4), (8, 5)], 23)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 5)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 10)
    puzzle.add_killer_cage([(5, 2), (6, 2), (7, 1), (7, 2), (8, 0), (8, 1)], 31)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 12)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 18)
    puzzle.add_killer_cage([(6, 0), (6, 1), (7, 0)], 19)
    puzzle.add_killer_cage([(3, 2), (4, 2)], 7)
    puzzle.add_killer_cage([(3, 3), (4, 3)], 11)
    puzzle.add_killer_cage([(2, 3), (2, 4)], 17)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 7)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5), (4, 4), (5, 3), (5, 4), (6, 3)], 30)
    puzzle.add_killer_cage([(6, 4), (6, 5)], 5)
    puzzle.add_killer_cage([(4, 5), (5, 5)], 11)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 4)

    return puzzle
