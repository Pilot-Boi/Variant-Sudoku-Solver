"""PuzzleMadness Killer Sudoku — 2025-07-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-07-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/7/29'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 18)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 5)
    puzzle.add_killer_cage([(1, 1), (1, 2)], 7)
    puzzle.add_killer_cage([(2, 1), (2, 2)], 15)
    puzzle.add_killer_cage([(0, 3), (0, 4), (1, 3)], 8)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 15)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7), (2, 6), (3, 6)], 27)
    puzzle.add_killer_cage([(1, 8), (2, 7), (2, 8)], 16)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 17)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 9)
    puzzle.add_killer_cage([(6, 6), (6, 7)], 8)
    puzzle.add_killer_cage([(7, 6), (7, 7)], 13)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 12)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 12)
    puzzle.add_killer_cage([(7, 5), (8, 4), (8, 5)], 16)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 13)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 8)
    puzzle.add_killer_cage([(5, 2), (6, 2), (7, 1), (7, 2), (8, 0), (8, 1)], 29)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 18)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 16)
    puzzle.add_killer_cage([(6, 0), (6, 1), (7, 0)], 17)
    puzzle.add_killer_cage([(3, 2), (4, 2)], 4)
    puzzle.add_killer_cage([(3, 3), (4, 3)], 14)
    puzzle.add_killer_cage([(2, 3), (2, 4)], 7)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 16)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5), (4, 4), (5, 3), (5, 4), (6, 3)], 35)
    puzzle.add_killer_cage([(6, 4), (6, 5)], 13)
    puzzle.add_killer_cage([(4, 5), (5, 5)], 5)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 12)

    return puzzle
