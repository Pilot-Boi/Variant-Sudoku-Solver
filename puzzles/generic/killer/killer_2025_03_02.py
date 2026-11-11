"""PuzzleMadness Killer Sudoku — 2025-03-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-03-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/3/2'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (0, 3)], 12)
    puzzle.add_killer_cage([(1, 0), (1, 1), (1, 2), (2, 0)], 28)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3), (3, 3)], 16)
    puzzle.add_killer_cage([(0, 4), (1, 3), (1, 4)], 11)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 16)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8), (2, 7)], 18)
    puzzle.add_killer_cage([(2, 8), (3, 8), (4, 8)], 17)
    puzzle.add_killer_cage([(4, 7), (5, 6), (5, 7), (5, 8)], 18)
    puzzle.add_killer_cage([(2, 6), (3, 6), (3, 7), (4, 6)], 19)
    puzzle.add_killer_cage([(1, 5), (1, 6), (2, 5)], 18)
    puzzle.add_killer_cage([(2, 4), (3, 4)], 10)
    puzzle.add_killer_cage([(3, 5), (4, 3), (4, 4), (4, 5), (5, 3)], 31)
    puzzle.add_killer_cage([(5, 4), (6, 4)], 10)
    puzzle.add_killer_cage([(5, 5), (6, 5), (6, 6), (6, 7)], 26)
    puzzle.add_killer_cage([(6, 8), (7, 6), (7, 7), (7, 8)], 18)
    puzzle.add_killer_cage([(8, 5), (8, 6), (8, 7), (8, 8)], 14)
    puzzle.add_killer_cage([(7, 4), (7, 5), (8, 4)], 13)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (8, 0)], 19)
    puzzle.add_killer_cage([(8, 1), (8, 2), (8, 3)], 20)
    puzzle.add_killer_cage([(6, 3), (7, 2), (7, 3)], 12)
    puzzle.add_killer_cage([(4, 2), (5, 1), (5, 2), (6, 2)], 17)
    puzzle.add_killer_cage([(3, 0), (3, 1), (3, 2), (4, 1)], 24)
    puzzle.add_killer_cage([(4, 0), (5, 0), (6, 0)], 18)

    return puzzle
