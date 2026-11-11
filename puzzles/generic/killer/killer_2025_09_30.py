"""PuzzleMadness Killer Sudoku — 2025-09-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-09-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/9/30'
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

    puzzle.add_killer_cage([(0, 0), (0, 1)], 7)
    puzzle.add_killer_cage([(1, 0), (1, 1)], 15)
    puzzle.add_killer_cage([(2, 0), (3, 0)], 8)
    puzzle.add_killer_cage([(4, 0), (5, 0), (6, 0)], 11)
    puzzle.add_killer_cage([(7, 0), (8, 0), (8, 1)], 20)
    puzzle.add_killer_cage([(6, 1), (7, 1), (7, 2)], 13)
    puzzle.add_killer_cage([(5, 2), (6, 2), (6, 3)], 11)
    puzzle.add_killer_cage([(4, 3), (5, 3), (5, 4)], 16)
    puzzle.add_killer_cage([(3, 4), (4, 4), (4, 5)], 15)
    puzzle.add_killer_cage([(2, 5), (3, 5), (3, 6)], 12)
    puzzle.add_killer_cage([(1, 6), (1, 7), (2, 6), (2, 7)], 15)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 8)], 17)
    puzzle.add_killer_cage([(0, 2), (0, 3), (1, 3)], 15)
    puzzle.add_killer_cage([(0, 4), (0, 5), (0, 6)], 19)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 6)
    puzzle.add_killer_cage([(2, 3), (2, 4)], 9)
    puzzle.add_killer_cage([(1, 2), (2, 1), (2, 2), (3, 1)], 20)
    puzzle.add_killer_cage([(3, 2), (3, 3), (4, 2)], 20)
    puzzle.add_killer_cage([(4, 1), (5, 1)], 15)
    puzzle.add_killer_cage([(5, 5), (6, 4), (6, 5)], 18)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 11)
    puzzle.add_killer_cage([(3, 7), (4, 7)], 14)
    puzzle.add_killer_cage([(2, 8), (3, 8), (4, 8)], 16)
    puzzle.add_killer_cage([(5, 7), (5, 8), (6, 8)], 8)
    puzzle.add_killer_cage([(7, 8), (8, 8)], 8)
    puzzle.add_killer_cage([(7, 7), (8, 7)], 15)
    puzzle.add_killer_cage([(6, 6), (6, 7), (7, 5), (7, 6)], 18)
    puzzle.add_killer_cage([(8, 5), (8, 6)], 6)
    puzzle.add_killer_cage([(8, 2), (8, 3), (8, 4)], 18)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 9)

    return puzzle
