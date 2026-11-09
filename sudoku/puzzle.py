from csp.solver import CSPSolver
from sudoku.constraints import (
    AllDifferentConstraint,
    ThermometerConstraint,
    KillerCageConstraint,
    NotEqualConstraint,
    NonConsecutiveConstraint,
    GermanWhispersConstraint,
    RenbanConstraint,
    PalindromeConstraint,
    ArrowConstraint,
    KropkiConstraint,
    NegativeKropkiConstraint,
    generate_king_pairs,
    generate_knight_pairs,
    generate_orthogonal_pairs
)

class SudokuPuzzle:
    def __init__(self, grid):
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise ValueError("Grid must be 9x9")

        if any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or value < 0
            or value > 9
            for row in grid
            for value in row
        ):
            raise ValueError("Cells must contain integers from 0 to 9")
        
        self.grid = [row.copy() for row in grid]
        
        self.variables = [
            (r, c)
            for r in range(9)
            for c in range(9)
        ]
        
        self.domains = {
            (r, c): set(range(1, 10))
            for r, c in self.variables
        }
        
        self.constraints = []

        # Kropki bookkeeping: dot type per unordered pair,
        # and pairs covered by negative constraints.
        self._kropki_pairs = {}
        self._negative_kropki_pairs = set()

        self.add_standard_constraints()
        
    
    def add_standard_constraints(self):
        digits = set(range(1, 10))

        # Rows
        for r in range(9):
            cells = [(r, c) for c in range(9)]

            self.constraints.append(
                AllDifferentConstraint(
                    cells,
                    required_values=digits
                )
            )

        # Columns
        for c in range(9):
            cells = [(r, c) for r in range(9)]

            self.constraints.append(
                AllDifferentConstraint(
                    cells,
                    required_values=digits
                )
            )

        # 3x3 boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                cells = [
                    (r, c)
                    for r in range(box_r, box_r + 3)
                    for c in range(box_c, box_c + 3)
                ]

                self.constraints.append(
                    AllDifferentConstraint(
                        cells,
                        required_values=digits
                    )
                )
    
    def add_diagonal_constraints(self):
        digits = set(range(1, 10))

        main_diagonal = [(i, i) for i in range(9)]
        anti_diagonal = [(i, 8 - i) for i in range(9)]

        self.add_constraint(
            AllDifferentConstraint(
                main_diagonal,
                required_values=digits
            )
        )

        self.add_constraint(
            AllDifferentConstraint(
                anti_diagonal,
                required_values=digits
            )
        )

    def add_anti_knight_constraints(self):
        """
        Add Anti-Knight Sudoku rules.

        Cells separated by a chess knight's move
        cannot contain the same digit.
        """
        for cell_a, cell_b in generate_knight_pairs():
            self.add_constraint(
                NotEqualConstraint(cell_a, cell_b)
            )
    
    def add_anti_king_constraints(self):
        """
        Enforce Anti-King Sudoku rules.

        Diagonally adjacent cells cannot contain
        the same digit.
        """
        for a, b in generate_king_pairs():
            self.add_constraint(NotEqualConstraint(a, b))
            
    
    def add_nonconsecutive_constraints(self):
        """
        Enforce global Nonconsecutive Sudoku rules.

        Orthogonally adjacent cells cannot contain
        consecutive digits.
        """
        for a, b in generate_orthogonal_pairs():
            self.add_constraint(
                NonConsecutiveConstraint(a, b)
            )
            
    def add_thermometer(self, cells):
        if len(cells) < 2:
            raise ValueError(
                "A thermometer must contain at least two cells."
            )

        if len(cells) > 9:
            raise ValueError(
                "A thermometer cannot exceed nine cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A thermometer cannot repeat a cell."
            )

        self.add_constraint(
            ThermometerConstraint(cells)
        )
        
    
    def add_killer_cage(self, cells, target_sum):
        """
        Add a Killer Sudoku cage.

        cells: list of (row, column) coordinates
        target_sum: required sum of the cage
        """
        if not cells:
            raise ValueError("Killer cage cannot be empty")

        if len(set(cells)) != len(cells):
            raise ValueError("Duplicate cage cells")

        if any(cell not in self.variables for cell in cells):
            raise ValueError("Invalid cage cell")

        self.add_constraint(
            KillerCageConstraint(cells, target_sum)
        )


    def add_german_whispers(self, cells):
        """
        Add a German Whispers line.

        cells: ordered list of (row, column) coordinates
        forming a connected path. Adjacent cells on the
        line must be orthogonally or diagonally adjacent
        on the grid.
        """
        cells = list(cells)

        if len(cells) < 2:
            raise ValueError(
                "A German Whispers line needs at least two cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A German Whispers line cannot repeat a cell."
            )

        if any(cell not in self.domains for cell in cells):
            raise ValueError(
                "German Whispers line references invalid cells."
            )

        for a, b in zip(cells, cells[1:]):
            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            if max(dr, dc) != 1:
                raise ValueError(
                    "German Whispers cells must be orthogonally "
                    "or diagonally adjacent."
                )

        self.add_constraint(
            GermanWhispersConstraint(cells)
        )


    def add_renban(self, cells):
        """
        Add a Renban line.

        cells: ordered list of (row, column) coordinates
        forming a connected path. Adjacent cells on the
        line must be orthogonally or diagonally adjacent
        on the grid.
        """
        cells = list(cells)

        if not 2 <= len(cells) <= 9:
            raise ValueError(
                "A Renban line needs between two and nine cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Renban line cannot repeat a cell."
            )

        if any(cell not in self.domains for cell in cells):
            raise ValueError(
                "Renban line references invalid cells."
            )

        for a, b in zip(cells, cells[1:]):
            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            if max(dr, dc) != 1:
                raise ValueError(
                    "Renban cells must be orthogonally "
                    "or diagonally adjacent."
                )

        self.add_constraint(
            RenbanConstraint(cells)
        )


    def add_palindrome(self, cells):
        """
        Add a Palindrome line.

        cells: ordered list of (row, column) coordinates
        forming a connected path. Adjacent cells on the
        line must be orthogonally or diagonally adjacent
        on the grid. Lines may exceed nine cells.
        """
        cells = list(cells)

        if len(cells) < 2:
            raise ValueError(
                "A Palindrome line needs at least two cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Palindrome line cannot repeat a cell."
            )

        if any(cell not in self.domains for cell in cells):
            raise ValueError(
                "Palindrome line references invalid cells."
            )

        for a, b in zip(cells, cells[1:]):
            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            if max(dr, dc) != 1:
                raise ValueError(
                    "Palindrome cells must be orthogonally "
                    "or diagonally adjacent."
                )

        self.add_constraint(
            PalindromeConstraint(cells)
        )


    def add_arrow(self, circle_cells, arrow_cells):
        """
        Add an Arrow constraint.

        circle_cells: ordered (row, column) coordinates of
        the circle. Multi-cell circles read as a base-10
        number in this order.
        arrow_cells: ordered coordinates of the shaft.

        The shaft must form a connected path starting
        adjacent to the circle. Adjacency includes
        diagonals.
        """
        circle_cells = list(circle_cells)
        arrow_cells = list(arrow_cells)

        if not circle_cells:
            raise ValueError(
                "An arrow needs at least one circle cell."
            )

        if not arrow_cells:
            raise ValueError(
                "An arrow needs at least one shaft cell."
            )

        all_cells = circle_cells + arrow_cells

        if len(set(all_cells)) != len(all_cells):
            raise ValueError(
                "Arrow circle and shaft cells must be distinct."
            )

        if any(cell not in self.domains for cell in all_cells):
            raise ValueError(
                "Arrow references invalid cells."
            )

        def adjacent(a, b):
            return max(abs(a[0] - b[0]), abs(a[1] - b[1])) == 1

        for a, b in zip(circle_cells, circle_cells[1:]):
            if not adjacent(a, b):
                raise ValueError(
                    "Circle cells must be orthogonally "
                    "or diagonally adjacent."
                )

        for a, b in zip(arrow_cells, arrow_cells[1:]):
            if not adjacent(a, b):
                raise ValueError(
                    "Arrow shaft cells must be orthogonally "
                    "or diagonally adjacent."
                )

        if not any(
            adjacent(arrow_cells[0], circle_cell)
            for circle_cell in circle_cells
        ):
            raise ValueError(
                "The arrow shaft must start adjacent "
                "to the circle."
            )

        self.add_constraint(
            ArrowConstraint(circle_cells, arrow_cells)
        )


    def add_kropki_dot(self, cell_a, cell_b, dot_type):
        """
        Add a Kropki dot between two orthogonally
        adjacent cells.

        dot_type: "white" (digits differ by 1) or
        "black" (digits in a 1:2 ratio).

        Each unordered cell pair may carry only one dot.
        Dots must be added before calling
        add_negative_kropki_constraints(); adding a dot
        to a pair that already has a negative constraint
        raises ValueError.
        """
        if dot_type not in KropkiConstraint.DOT_TYPES:
            raise ValueError(
                f"Invalid Kropki dot type: {dot_type!r}"
            )

        if cell_a == cell_b:
            raise ValueError(
                "A Kropki dot needs two distinct cells."
            )

        if (
            cell_a not in self.domains
            or cell_b not in self.domains
        ):
            raise ValueError(
                "Kropki dot references invalid cells."
            )

        dr = abs(cell_a[0] - cell_b[0])
        dc = abs(cell_a[1] - cell_b[1])

        if dr + dc != 1:
            raise ValueError(
                "Kropki dots connect orthogonally "
                "adjacent cells only."
            )

        pair = tuple(sorted((cell_a, cell_b)))

        if pair in self._kropki_pairs:
            raise ValueError(
                f"A Kropki dot is already defined for "
                f"{pair[0]} and {pair[1]}."
            )

        if pair in self._negative_kropki_pairs:
            raise ValueError(
                f"Negative Kropki constraints already "
                f"cover {pair[0]} and {pair[1]}. Add all "
                f"dots before calling "
                f"add_negative_kropki_constraints()."
            )

        self._kropki_pairs[pair] = dot_type

        self.add_constraint(
            KropkiConstraint(cell_a, cell_b, dot_type)
        )

    def add_negative_kropki_constraints(self):
        """
        Add negative Kropki constraints to every
        orthogonally adjacent pair without a dot.

        Undotted pairs must not contain consecutive
        digits or digits in a 1:2 ratio. Diagonal
        neighbors are unaffected. Repeated calls are
        idempotent.
        """
        for a, b in generate_orthogonal_pairs():
            pair = tuple(sorted((a, b)))

            if pair in self._kropki_pairs:
                continue

            if pair in self._negative_kropki_pairs:
                continue

            self._negative_kropki_pairs.add(pair)

            self.add_constraint(
                NegativeKropkiConstraint(a, b)
            )


    def add_constraint(self, constraint):
        if any(
            var not in self.domains
            for var in constraint.variables  
        ):
            raise ValueError("Constraint references invalid cells.")
        
        self.constraints.append(constraint)
    
    def check_uniqueness(self):
        """
        Determine whether the puzzle has exactly
        one solution.

        Returns:
            status: "none", "unique", or "multiple"
            solutions: up to two solution dictionaries
            solver: the solver used for the search
        """
        initial_assignment = {
            (r, c): self.grid[r][c]
            for r, c in self.variables
            if self.grid[r][c] != 0
        }

        solver = CSPSolver(
            self.variables,
            self.domains,
            self.constraints
        )

        solutions = solver.solve_all(
            initial_assignment,
            limit=2
        )

        if len(solutions) == 0:
            status = "none"
        elif len(solutions) == 1:
            status = "unique"
        else:
            status = "multiple"

        return status, solutions, solver
        
    def solve(self):
        initial_assignment = {
            (r, c): self.grid[r][c]
            for r, c in self.variables
            if self.grid[r][c] != 0
        }
            
        solver = CSPSolver(
            self.variables,
            self.domains,
            self.constraints,
        )
        
        solution = solver.solve(initial_assignment)
        
        return solution, solver
    
    @staticmethod
    def print_grid(assignment):
        if assignment is None:
            print("No solution found.")
            return
        
        for r in range(9):
            if r > 0 and r % 3 == 0 :
                print("------+-------+------")
                
            values = []
            
            for c in range(9):
                if c > 0 and c % 3 == 0:
                    values.append("|")
                    
                values.append(str(assignment[(r, c)]))
            print(" ".join(values))