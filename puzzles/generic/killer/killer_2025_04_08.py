"""PuzzleMadness Killer Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/4/8'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0), (2, 0), (3, 0)], 26)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3), (2, 1)], 16)
    puzzle.add_killer_cage([(0, 2), (0, 3)], 13)
    puzzle.add_killer_cage([(0, 4), (0, 5), (1, 4), (1, 5)], 20)
    puzzle.add_killer_cage([(0, 6), (0, 7), (1, 6)], 12)
    puzzle.add_killer_cage([(0, 8), (1, 7), (1, 8)], 19)
    puzzle.add_killer_cage([(2, 7), (2, 8)], 12)
    puzzle.add_killer_cage([(3, 6), (3, 7), (3, 8)], 8)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 12)
    puzzle.add_killer_cage([(2, 3), (3, 3)], 11)
    puzzle.add_killer_cage([(2, 2), (3, 1), (3, 2)], 18)
    puzzle.add_killer_cage([(4, 0), (4, 1), (4, 2)], 10)
    puzzle.add_killer_cage([(5, 0), (5, 1), (5, 2)], 16)
    puzzle.add_killer_cage([(6, 0), (6, 1)], 9)
    puzzle.add_killer_cage([(7, 0), (7, 1), (8, 0)], 21)
    puzzle.add_killer_cage([(7, 2), (8, 1), (8, 2)], 13)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 16)
    puzzle.add_killer_cage([(5, 3), (5, 4)], 4)
    puzzle.add_killer_cage([(4, 3), (4, 4), (4, 5)], 21)
    puzzle.add_killer_cage([(3, 4), (3, 5)], 13)
    puzzle.add_killer_cage([(4, 6), (4, 7), (4, 8)], 14)
    puzzle.add_killer_cage([(5, 6), (5, 7), (6, 6)], 21)
    puzzle.add_killer_cage([(6, 7), (7, 5), (7, 6), (7, 7)], 22)
    puzzle.add_killer_cage([(5, 8), (6, 8), (7, 8), (8, 7), (8, 8)], 20)
    puzzle.add_killer_cage([(8, 5), (8, 6)], 10)
    puzzle.add_killer_cage([(7, 3), (7, 4), (8, 3), (8, 4)], 20)
    puzzle.add_killer_cage([(5, 5), (6, 5)], 8)

    return puzzle
