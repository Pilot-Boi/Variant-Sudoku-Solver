"""PuzzleMadness Killer Sudoku — 2025-06-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-06-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/6/12'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (1, 3)], 30)
    puzzle.add_killer_cage([(0, 3), (0, 4)], 11)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 5)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], 41)
    puzzle.add_killer_cage([(3, 8), (4, 8)], 12)
    puzzle.add_killer_cage([(3, 6), (3, 7)], 6)
    puzzle.add_killer_cage([(4, 6), (5, 6)], 10)
    puzzle.add_killer_cage([(4, 7), (5, 7)], 11)
    puzzle.add_killer_cage([(5, 8), (6, 8)], 11)
    puzzle.add_killer_cage([(6, 7), (7, 7)], 15)
    puzzle.add_killer_cage([(7, 5), (7, 6), (7, 8), (8, 6), (8, 7), (8, 8)], 25)
    puzzle.add_killer_cage([(8, 4), (8, 5)], 8)
    puzzle.add_killer_cage([(7, 3), (7, 4)], 5)
    puzzle.add_killer_cage([(8, 2), (8, 3)], 10)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (8, 0), (8, 1)], 38)
    puzzle.add_killer_cage([(2, 4), (2, 5), (3, 4), (4, 4), (5, 4), (6, 3), (6, 4)], 38)
    puzzle.add_killer_cage([(1, 4), (1, 5)], 10)
    puzzle.add_killer_cage([(3, 5), (4, 5)], 11)
    puzzle.add_killer_cage([(5, 5), (6, 5), (6, 6)], 17)
    puzzle.add_killer_cage([(4, 3), (5, 3)], 7)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 3)], 19)
    puzzle.add_killer_cage([(1, 1), (2, 1)], 9)
    puzzle.add_killer_cage([(2, 0), (3, 0)], 8)
    puzzle.add_killer_cage([(4, 0), (5, 0)], 6)
    puzzle.add_killer_cage([(5, 1), (5, 2)], 16)
    puzzle.add_killer_cage([(3, 2), (4, 2)], 10)
    puzzle.add_killer_cage([(3, 1), (4, 1)], 11)
    puzzle.add_killer_cage([(7, 2)], 5)

    return puzzle
