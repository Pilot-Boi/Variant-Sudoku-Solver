"""PuzzleMadness Killer Sudoku — 2026-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2026-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2026/10/6'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2)], 15)
    puzzle.add_killer_cage([(1, 0), (2, 0)], 13)
    puzzle.add_killer_cage([(0, 3), (1, 1), (1, 2), (1, 3)], 17)
    puzzle.add_killer_cage([(0, 4), (0, 5), (0, 6)], 9)
    puzzle.add_killer_cage([(0, 7), (1, 6), (1, 7)], 16)
    puzzle.add_killer_cage([(0, 8), (1, 8)], 13)
    puzzle.add_killer_cage([(2, 5), (2, 6), (2, 7), (2, 8)], 19)
    puzzle.add_killer_cage([(1, 4), (1, 5), (2, 4)], 21)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3)], 12)
    puzzle.add_killer_cage([(3, 0), (3, 1)], 7)
    puzzle.add_killer_cage([(3, 2), (3, 3)], 9)
    puzzle.add_killer_cage([(3, 4), (3, 5)], 5)
    puzzle.add_killer_cage([(3, 6), (4, 6)], 8)
    puzzle.add_killer_cage([(3, 7), (4, 7)], 11)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 15)
    puzzle.add_killer_cage([(5, 7), (5, 8)], 6)
    puzzle.add_killer_cage([(6, 8), (7, 8)], 9)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 16)
    puzzle.add_killer_cage([(7, 5), (7, 6), (7, 7), (8, 5)], 24)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7)], 18)
    puzzle.add_killer_cage([(5, 5), (5, 6)], 11)
    puzzle.add_killer_cage([(4, 3), (4, 4), (4, 5)], 16)
    puzzle.add_killer_cage([(5, 3), (5, 4)], 15)
    puzzle.add_killer_cage([(6, 4), (7, 3), (7, 4)], 11)
    puzzle.add_killer_cage([(8, 2), (8, 3), (8, 4)], 12)
    puzzle.add_killer_cage([(7, 1), (7, 2), (8, 1)], 15)
    puzzle.add_killer_cage([(7, 0), (8, 0)], 11)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2), (6, 3)], 19)
    puzzle.add_killer_cage([(4, 0), (5, 0)], 7)
    puzzle.add_killer_cage([(4, 1), (5, 1)], 8)
    puzzle.add_killer_cage([(4, 2), (5, 2)], 17)

    return puzzle
