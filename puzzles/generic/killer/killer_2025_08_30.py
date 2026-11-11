"""PuzzleMadness Killer Sudoku — 2025-08-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-08-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/8/30'
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
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0)], 14)
    puzzle.add_killer_cage([(2, 1), (3, 1)], 14)
    puzzle.add_killer_cage([(1, 2), (2, 2), (3, 2)], 10)
    puzzle.add_killer_cage([(0, 3), (0, 4), (1, 3), (2, 3)], 18)
    puzzle.add_killer_cage([(0, 5), (1, 5)], 15)
    puzzle.add_killer_cage([(0, 6), (0, 7), (1, 6)], 13)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8), (2, 7)], 25)
    puzzle.add_killer_cage([(2, 8), (3, 7), (3, 8), (4, 7)], 22)
    puzzle.add_killer_cage([(4, 8), (5, 8)], 6)
    puzzle.add_killer_cage([(5, 7), (6, 7)], 3)
    puzzle.add_killer_cage([(6, 8), (7, 7), (7, 8)], 18)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 14)
    puzzle.add_killer_cage([(5, 6), (6, 6), (7, 6)], 16)
    puzzle.add_killer_cage([(3, 6), (4, 6)], 13)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 5)], 15)
    puzzle.add_killer_cage([(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)], 30)
    puzzle.add_killer_cage([(6, 5), (7, 5), (8, 4), (8, 5)], 20)
    puzzle.add_killer_cage([(4, 5), (5, 5)], 8)
    puzzle.add_killer_cage([(3, 0), (4, 0)], 9)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1), (6, 0)], 21)
    puzzle.add_killer_cage([(6, 1), (7, 0), (7, 1), (8, 0)], 20)
    puzzle.add_killer_cage([(7, 2), (8, 1), (8, 2)], 14)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 12)
    puzzle.add_killer_cage([(4, 2), (5, 2)], 15)
    puzzle.add_killer_cage([(5, 3), (6, 2), (6, 3)], 16)
    puzzle.add_killer_cage([(3, 3), (4, 3)], 8)

    return puzzle
