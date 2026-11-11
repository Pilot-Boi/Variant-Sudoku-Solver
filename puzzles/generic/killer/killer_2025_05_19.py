"""PuzzleMadness Killer Sudoku — 2025-05-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-05-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/5/19'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0), (1, 1)], 24)
    puzzle.add_killer_cage([(0, 2), (0, 3), (1, 2)], 12)
    puzzle.add_killer_cage([(1, 3), (2, 3)], 15)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 25)
    puzzle.add_killer_cage([(0, 5), (0, 6), (1, 6)], 22)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 7), (1, 8)], 19)
    puzzle.add_killer_cage([(2, 8), (3, 8), (4, 8)], 14)
    puzzle.add_killer_cage([(4, 7), (5, 7), (5, 8)], 15)
    puzzle.add_killer_cage([(2, 7), (3, 7)], 10)
    puzzle.add_killer_cage([(2, 6), (3, 6)], 10)
    puzzle.add_killer_cage([(1, 5), (2, 5)], 4)
    puzzle.add_killer_cage([(3, 5), (4, 5), (4, 6)], 17)
    puzzle.add_killer_cage([(2, 0), (3, 0), (4, 0)], 10)
    puzzle.add_killer_cage([(2, 1), (3, 1)], 15)
    puzzle.add_killer_cage([(2, 2), (3, 2)], 7)
    puzzle.add_killer_cage([(3, 3), (4, 2), (4, 3)], 18)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 12)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2), (6, 3)], 18)
    puzzle.add_killer_cage([(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 4)], 29)
    puzzle.add_killer_cage([(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 4)], 31)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7), (6, 8)], 19)
    puzzle.add_killer_cage([(7, 7), (7, 8), (8, 8)], 10)
    puzzle.add_killer_cage([(8, 5), (8, 6), (8, 7)], 19)
    puzzle.add_killer_cage([(7, 0), (7, 1), (8, 0)], 10)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 20)

    return puzzle
