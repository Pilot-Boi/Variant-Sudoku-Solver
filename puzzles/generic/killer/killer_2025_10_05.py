"""PuzzleMadness Killer Sudoku — 2025-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/10/5'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0), (2, 0), (3, 0)], 31)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3), (2, 1)], 16)
    puzzle.add_killer_cage([(0, 2), (0, 3)], 10)
    puzzle.add_killer_cage([(0, 4), (0, 5), (1, 4), (1, 5)], 21)
    puzzle.add_killer_cage([(0, 6), (0, 7), (1, 6)], 17)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8)], 16)
    puzzle.add_killer_cage([(2, 7), (2, 8)], 9)
    puzzle.add_killer_cage([(3, 6), (3, 7), (3, 8)], 14)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 11)
    puzzle.add_killer_cage([(2, 3), (3, 3)], 10)
    puzzle.add_killer_cage([(2, 2), (3, 1), (3, 2)], 15)
    puzzle.add_killer_cage([(4, 0), (4, 1), (4, 2)], 14)
    puzzle.add_killer_cage([(5, 0), (5, 1), (5, 2)], 16)
    puzzle.add_killer_cage([(6, 0), (6, 1)], 8)
    puzzle.add_killer_cage([(7, 0), (7, 1), (8, 0)], 19)
    puzzle.add_killer_cage([(7, 2), (8, 1), (8, 2)], 16)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 10)
    puzzle.add_killer_cage([(5, 3), (5, 4)], 5)
    puzzle.add_killer_cage([(4, 3), (4, 4), (4, 5)], 15)
    puzzle.add_killer_cage([(3, 4), (3, 5)], 10)
    puzzle.add_killer_cage([(4, 6), (4, 7), (4, 8)], 16)
    puzzle.add_killer_cage([(5, 6), (5, 7), (6, 6)], 19)
    puzzle.add_killer_cage([(6, 7), (7, 5), (7, 6), (7, 7)], 12)
    puzzle.add_killer_cage([(5, 8), (6, 8), (7, 8), (8, 7), (8, 8)], 25)
    puzzle.add_killer_cage([(8, 5), (8, 6)], 12)
    puzzle.add_killer_cage([(7, 3), (7, 4), (8, 3), (8, 4)], 25)
    puzzle.add_killer_cage([(5, 5), (6, 5)], 13)

    return puzzle
