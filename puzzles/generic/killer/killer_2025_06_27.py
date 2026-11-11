"""PuzzleMadness Killer Sudoku — 2025-06-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-06-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/6/27'
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
    puzzle.add_killer_cage([(0, 1), (1, 1), (1, 2)], 18)
    puzzle.add_killer_cage([(2, 1), (3, 1), (3, 2)], 11)
    puzzle.add_killer_cage([(3, 0), (4, 0), (4, 1), (5, 0)], 12)
    puzzle.add_killer_cage([(3, 3), (4, 2), (4, 3), (5, 3)], 18)
    puzzle.add_killer_cage([(3, 6), (4, 4), (4, 5), (4, 6), (5, 6)], 20)
    puzzle.add_killer_cage([(3, 8), (4, 7), (4, 8), (5, 8)], 23)
    puzzle.add_killer_cage([(6, 8), (7, 7), (7, 8), (8, 8)], 14)
    puzzle.add_killer_cage([(7, 3), (7, 4), (7, 5), (7, 6)], 25)
    puzzle.add_killer_cage([(5, 1), (5, 2), (6, 1)], 20)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 21)
    puzzle.add_killer_cage([(7, 1), (7, 2), (8, 1)], 18)
    puzzle.add_killer_cage([(8, 2), (8, 3), (8, 4)], 9)
    puzzle.add_killer_cage([(8, 5), (8, 6), (8, 7)], 12)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 11)
    puzzle.add_killer_cage([(5, 4), (5, 5), (6, 5)], 16)
    puzzle.add_killer_cage([(5, 7), (6, 6), (6, 7)], 22)
    puzzle.add_killer_cage([(2, 5), (3, 4), (3, 5)], 14)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4)], 14)
    puzzle.add_killer_cage([(0, 2), (0, 3), (0, 4)], 24)
    puzzle.add_killer_cage([(1, 3), (1, 4), (1, 5), (1, 6)], 18)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 12)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8), (2, 8)], 20)
    puzzle.add_killer_cage([(2, 6), (2, 7), (3, 7)], 19)

    return puzzle
