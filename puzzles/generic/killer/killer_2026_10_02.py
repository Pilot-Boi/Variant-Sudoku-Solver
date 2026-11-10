"""PuzzleMadness Killer Sudoku — 2026-10-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2026-10-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2026/10/2'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 16)
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0)], 17)
    puzzle.add_killer_cage([(2, 1), (3, 0), (3, 1)], 8)
    puzzle.add_killer_cage([(4, 0), (4, 1), (5, 0), (5, 1)], 20)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 13)
    puzzle.add_killer_cage([(7, 1), (8, 1)], 9)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 1), (6, 2)], 24)
    puzzle.add_killer_cage([(3, 2), (4, 2), (4, 3)], 16)
    puzzle.add_killer_cage([(1, 2), (2, 2)], 8)
    puzzle.add_killer_cage([(0, 3), (1, 3)], 9)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4)], 11)
    puzzle.add_killer_cage([(0, 5), (1, 5)], 8)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8)], 21)
    puzzle.add_killer_cage([(1, 6), (2, 6)], 9)
    puzzle.add_killer_cage([(2, 7), (3, 7), (3, 8)], 17)
    puzzle.add_killer_cage([(1, 7), (1, 8), (2, 8)], 12)
    puzzle.add_killer_cage([(3, 6), (4, 5), (4, 6)], 15)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 7), (5, 8)], 21)
    puzzle.add_killer_cage([(5, 5), (5, 6), (6, 6), (6, 7)], 18)
    puzzle.add_killer_cage([(6, 8), (7, 8), (8, 8)], 6)
    puzzle.add_killer_cage([(7, 7), (8, 7)], 17)
    puzzle.add_killer_cage([(7, 6), (8, 5), (8, 6)], 18)
    puzzle.add_killer_cage([(5, 4), (6, 3), (6, 4), (6, 5), (7, 3), (7, 5)], 31)
    puzzle.add_killer_cage([(7, 2), (8, 2), (8, 3)], 17)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 9)
    puzzle.add_killer_cage([(2, 3), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4)], 35)

    return puzzle
