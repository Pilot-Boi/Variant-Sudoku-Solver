"""PuzzleMadness Killer Sudoku — 2026-10-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2026-10-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2026/10/25'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0)], 22)
    puzzle.add_killer_cage([(1, 1), (2, 0), (2, 1), (3, 0)], 18)
    puzzle.add_killer_cage([(1, 2), (2, 2)], 12)
    puzzle.add_killer_cage([(0, 3), (1, 3), (2, 3)], 16)
    puzzle.add_killer_cage([(0, 4), (1, 4)], 11)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 9)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 5), (1, 6), (1, 7)], 21)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 8), (4, 8)], 29)
    puzzle.add_killer_cage([(5, 8), (6, 7), (6, 8), (7, 7)], 24)
    puzzle.add_killer_cage([(7, 8), (8, 6), (8, 7), (8, 8)], 18)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7), (5, 6), (5, 7)], 18)
    puzzle.add_killer_cage([(6, 6), (7, 6)], 5)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 14)
    puzzle.add_killer_cage([(3, 5), (3, 6)], 15)
    puzzle.add_killer_cage([(3, 3), (3, 4)], 5)
    puzzle.add_killer_cage([(3, 1), (3, 2), (4, 1), (5, 1), (6, 1)], 26)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 15)
    puzzle.add_killer_cage([(6, 5), (7, 5), (8, 5)], 13)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 9)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 15)
    puzzle.add_killer_cage([(7, 1), (7, 2), (7, 3), (8, 0), (8, 1)], 30)
    puzzle.add_killer_cage([(4, 0), (5, 0), (6, 0), (7, 0)], 14)
    puzzle.add_killer_cage([(5, 2), (5, 3)], 11)
    puzzle.add_killer_cage([(5, 4), (5, 5)], 13)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 22)

    return puzzle
