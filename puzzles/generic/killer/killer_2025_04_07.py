"""PuzzleMadness Killer Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/4/7'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0), (1, 1)], 17)
    puzzle.add_killer_cage([(0, 2), (0, 3), (1, 2)], 11)
    puzzle.add_killer_cage([(1, 3), (2, 3)], 13)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 24)
    puzzle.add_killer_cage([(0, 5), (0, 6), (1, 6)], 17)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 7), (1, 8)], 18)
    puzzle.add_killer_cage([(2, 8), (3, 8), (4, 8)], 18)
    puzzle.add_killer_cage([(4, 7), (5, 7), (5, 8)], 8)
    puzzle.add_killer_cage([(2, 7), (3, 7)], 14)
    puzzle.add_killer_cage([(2, 6), (3, 6)], 10)
    puzzle.add_killer_cage([(1, 5), (2, 5)], 10)
    puzzle.add_killer_cage([(3, 5), (4, 5), (4, 6)], 21)
    puzzle.add_killer_cage([(2, 0), (3, 0), (4, 0)], 14)
    puzzle.add_killer_cage([(2, 1), (3, 1)], 4)
    puzzle.add_killer_cage([(2, 2), (3, 2)], 10)
    puzzle.add_killer_cage([(3, 3), (4, 2), (4, 3)], 15)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 23)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2), (6, 3)], 22)
    puzzle.add_killer_cage([(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 4)], 31)
    puzzle.add_killer_cage([(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 4)], 32)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7), (6, 8)], 15)
    puzzle.add_killer_cage([(7, 7), (7, 8), (8, 8)], 23)
    puzzle.add_killer_cage([(8, 5), (8, 6), (8, 7)], 6)
    puzzle.add_killer_cage([(7, 0), (7, 1), (8, 0)], 12)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 17)

    return puzzle
