"""PuzzleMadness Killer Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/4/30'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0)], 20)
    puzzle.add_killer_cage([(0, 2), (0, 3), (0, 4)], 13)
    puzzle.add_killer_cage([(0, 5), (1, 5), (2, 5)], 20)
    puzzle.add_killer_cage([(0, 6), (1, 6), (2, 6)], 12)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 7)], 10)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 8)], 15)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 19)
    puzzle.add_killer_cage([(4, 8), (5, 8), (6, 8)], 16)
    puzzle.add_killer_cage([(7, 8), (8, 7), (8, 8)], 15)
    puzzle.add_killer_cage([(7, 5), (7, 6), (7, 7)], 16)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7)], 19)
    puzzle.add_killer_cage([(5, 5), (5, 6), (5, 7)], 16)
    puzzle.add_killer_cage([(3, 4), (3, 5), (3, 6)], 15)
    puzzle.add_killer_cage([(1, 4), (2, 4)], 11)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3)], 14)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3)], 11)
    puzzle.add_killer_cage([(3, 1), (3, 2), (3, 3)], 24)
    puzzle.add_killer_cage([(2, 0), (3, 0), (4, 0)], 7)
    puzzle.add_killer_cage([(4, 1), (5, 1), (6, 1)], 11)
    puzzle.add_killer_cage([(5, 0), (6, 0), (7, 0)], 18)
    puzzle.add_killer_cage([(7, 1), (8, 0), (8, 1)], 22)
    puzzle.add_killer_cage([(6, 2), (7, 2), (8, 2)], 10)
    puzzle.add_killer_cage([(6, 3), (7, 3), (8, 3)], 15)
    puzzle.add_killer_cage([(6, 4), (7, 4)], 9)
    puzzle.add_killer_cage([(8, 4), (8, 5), (8, 6)], 13)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 19)
    puzzle.add_killer_cage([(5, 2), (5, 3), (5, 4)], 15)

    return puzzle
