"""PuzzleMadness Killer Sudoku — 2025-08-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-08-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/8/8'
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
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0)], 8)
    puzzle.add_killer_cage([(2, 1), (3, 0), (3, 1)], 17)
    puzzle.add_killer_cage([(4, 0), (4, 1), (5, 0), (5, 1)], 20)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 15)
    puzzle.add_killer_cage([(7, 1), (8, 1)], 8)
    puzzle.add_killer_cage([(5, 2), (5, 3), (6, 1), (6, 2)], 20)
    puzzle.add_killer_cage([(3, 2), (4, 2), (4, 3)], 10)
    puzzle.add_killer_cage([(1, 2), (2, 2)], 13)
    puzzle.add_killer_cage([(0, 3), (1, 3)], 12)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4)], 11)
    puzzle.add_killer_cage([(0, 5), (1, 5)], 17)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8)], 14)
    puzzle.add_killer_cage([(1, 6), (2, 6)], 4)
    puzzle.add_killer_cage([(2, 7), (3, 7), (3, 8)], 14)
    puzzle.add_killer_cage([(1, 7), (1, 8), (2, 8)], 18)
    puzzle.add_killer_cage([(3, 6), (4, 5), (4, 6)], 12)
    puzzle.add_killer_cage([(4, 7), (4, 8), (5, 7), (5, 8)], 27)
    puzzle.add_killer_cage([(5, 5), (5, 6), (6, 6), (6, 7)], 22)
    puzzle.add_killer_cage([(6, 8), (7, 8), (8, 8)], 9)
    puzzle.add_killer_cage([(7, 7), (8, 7)], 9)
    puzzle.add_killer_cage([(7, 6), (8, 5), (8, 6)], 19)
    puzzle.add_killer_cage([(5, 4), (6, 3), (6, 4), (6, 5), (7, 3), (7, 5)], 30)
    puzzle.add_killer_cage([(7, 2), (8, 2), (8, 3)], 15)
    puzzle.add_killer_cage([(7, 4), (8, 4)], 11)
    puzzle.add_killer_cage([(2, 3), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4)], 34)

    return puzzle
