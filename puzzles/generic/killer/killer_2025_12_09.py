"""PuzzleMadness Killer Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/12/9'
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

    puzzle.add_killer_cage([(0, 0), (1, 0)], 7)
    puzzle.add_killer_cage([(2, 0), (3, 0), (4, 0)], 24)
    puzzle.add_killer_cage([(5, 0), (5, 1)], 7)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)], 27)
    puzzle.add_killer_cage([(6, 1), (6, 2), (7, 1), (7, 2)], 18)
    puzzle.add_killer_cage([(0, 1), (0, 2), (1, 1)], 8)
    puzzle.add_killer_cage([(1, 2), (2, 1), (2, 2)], 23)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 11)
    puzzle.add_killer_cage([(3, 2), (3, 3), (3, 4)], 18)
    puzzle.add_killer_cage([(1, 4), (2, 3), (2, 4)], 12)
    puzzle.add_killer_cage([(0, 3), (1, 3)], 6)
    puzzle.add_killer_cage([(0, 4), (0, 5)], 17)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8), (1, 8), (2, 8)], 27)
    puzzle.add_killer_cage([(1, 5), (1, 6), (1, 7), (2, 7), (3, 7)], 24)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 10)
    puzzle.add_killer_cage([(5, 7), (5, 8)], 11)
    puzzle.add_killer_cage([(4, 6), (4, 7), (5, 6)], 19)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 5), (3, 6)], 15)
    puzzle.add_killer_cage([(4, 5), (5, 5), (6, 5)], 15)
    puzzle.add_killer_cage([(6, 6), (6, 7), (7, 6)], 15)
    puzzle.add_killer_cage([(6, 8), (7, 7), (7, 8)], 12)
    puzzle.add_killer_cage([(8, 7), (8, 8)], 12)
    puzzle.add_killer_cage([(8, 4), (8, 5), (8, 6)], 11)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 12)
    puzzle.add_killer_cage([(7, 4), (7, 5)], 12)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (5, 4), (6, 4)], 16)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 3)], 16)

    return puzzle
