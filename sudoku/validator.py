from sudoku.constraints import (
    KillerCageConstraint,
    ThermometerConstraint,
    NotEqualConstraint,
    GermanWhispersConstraint,
    RenbanConstraint,
    PalindromeConstraint,
    ArrowConstraint,
    KropkiConstraint,
    NegativeKropkiConstraint,
    InequalityConstraint,
    XVConstraint,
    NegativeXVConstraint,
    ParityConstraint,
    BetweenLineConstraint,
    LittleKillerConstraint,
)

def validate_solution(puzzle, solution):
    """
    Validate a solved Sudoku grid independently of the CSP solver.

    solution: dictionary mapping (row, column) -> digit
    Returns a list of error messages.
    An empty list means the solution passed all checks.
    """
    errors = []
    expected = set(range(1, 10))

    # Check that every cell has a valid digit.
    for r in range(9):
        for c in range(9):
            value = solution.get((r, c))

            if value not in expected:
                errors.append(
                    f"Invalid value at R{r + 1}C{c + 1}: {value}"
                )

    # Check rows.
    for r in range(9):
        values = [solution.get((r, c)) for c in range(9)]

        if set(values) != expected:
            errors.append(f"Row {r + 1} is invalid")

    # Check columns.
    for c in range(9):
        values = [solution.get((r, c)) for r in range(9)]

        if set(values) != expected:
            errors.append(f"Column {c + 1} is invalid")

    # Check 3x3 boxes.
    for box_r in range(3):
        for box_c in range(3):
            cells = [
                (r, c)
                for r in range(box_r * 3, box_r * 3 + 3)
                for c in range(box_c * 3, box_c * 3 + 3)
            ]

            values = [solution.get(cell) for cell in cells]

            if set(values) != expected:
                errors.append(
                    f"Box {box_r * 3 + box_c + 1} is invalid"
                )

    # Check given digits.
    for r in range(9):
        for c in range(9):
            given = puzzle.grid[r][c]

            if given and solution.get((r, c)) != given:
                errors.append(
                    f"Given digit mismatch at R{r + 1}C{c + 1}"
                )

    # Check variant constraints.
    for constraint in puzzle.constraints:

        if isinstance(constraint, ThermometerConstraint):
            values = [
                solution.get(cell)
                for cell in constraint.variables
            ]

            if any(
                a is None or b is None or a >= b
                for a, b in zip(values, values[1:])
            ):
                errors.append(
                    f"Invalid thermometer: {constraint.variables}"
                )

        elif isinstance(constraint, KillerCageConstraint):
            values = [
                solution.get(cell)
                for cell in constraint.variables
            ]

            if (
                any(v is None for v in values)
                or sum(v for v in values if v is not None)
                    != constraint.target_sum
                or len(values) != len(set(values))
            ):
                errors.append(
                    f"Invalid Killer cage "
                    f"(target {constraint.target_sum}): "
                    f"{constraint.variables}"
                )
        
        elif isinstance(constraint, NotEqualConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            if (
                value_a is None
                or value_b is None
                or value_a == value_b
            ):
                errors.append(
                    f"Not-equal constraint violation: ..."
                    f"R{a[0] + 1}C{a[1] + 1} and "
                    f"R{b[0] + 1}C{b[1] + 1}"
                )

        elif isinstance(constraint, GermanWhispersConstraint):
            cells = constraint.variables
            minimum = constraint.MINIMUM_DIFFERENCE

            for a, b in zip(cells, cells[1:]):
                value_a = solution.get(a)
                value_b = solution.get(b)

                if (
                    value_a is None
                    or value_b is None
                    or abs(value_a - value_b) < minimum
                ):
                    errors.append(
                        f"German Whispers violation: "
                        f"R{a[0] + 1}C{a[1] + 1} and "
                        f"R{b[0] + 1}C{b[1] + 1}"
                    )

        elif isinstance(constraint, RenbanConstraint):
            cells = constraint.variables
            values = [solution.get(cell) for cell in cells]

            if any(value is None for value in values):
                errors.append(
                    f"Renban line is incomplete: {cells}"
                )

            elif len(values) != len(set(values)):
                errors.append(
                    f"Renban line repeats a digit: {cells}"
                )

            elif max(values) - min(values) != len(cells) - 1:
                errors.append(
                    f"Renban line digits are not consecutive: "
                    f"{cells}"
                )

        elif isinstance(constraint, PalindromeConstraint):
            cells = constraint.variables

            if any(
                solution.get(cell) is None
                for cell in cells
            ):
                errors.append(
                    f"Palindrome line is incomplete: {cells}"
                )

            else:
                for a, b in constraint.mirrored_pairs:
                    if solution[a] != solution[b]:
                        errors.append(
                            f"Palindrome mismatch: "
                            f"R{a[0] + 1}C{a[1] + 1} and "
                            f"R{b[0] + 1}C{b[1] + 1}"
                        )

        elif isinstance(constraint, ArrowConstraint):
            circle = constraint.circle_cells
            arrow = constraint.arrow_cells

            values = [
                solution.get(cell)
                for cell in circle + arrow
            ]

            if any(value is None for value in values):
                errors.append(
                    f"Arrow is incomplete: circle {circle}, "
                    f"shaft {arrow}"
                )

            else:
                number = 0

                for cell in circle:
                    number = number * 10 + solution[cell]

                total = sum(
                    solution[cell] for cell in arrow
                )

                if number != total:
                    circle_text = ", ".join(
                        f"R{r + 1}C{c + 1}" for r, c in circle
                    )

                    errors.append(
                        f"Arrow violation: circle "
                        f"[{circle_text}] expects {number}, "
                        f"but the shaft sums to {total}"
                    )

        elif isinstance(constraint, KropkiConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            if value_a is None or value_b is None:
                errors.append(
                    f"Kropki dot is incomplete: "
                    f"{label_a} and {label_b}"
                )

            elif constraint.dot_type == "white":
                if abs(value_a - value_b) != 1:
                    errors.append(
                        f"White Kropki violation: {label_a} "
                        f"and {label_b} must differ by "
                        f"exactly 1"
                    )

            else:
                if (
                    value_a != 2 * value_b
                    and value_b != 2 * value_a
                ):
                    errors.append(
                        f"Black Kropki violation: {label_a} "
                        f"and {label_b} must be in a 1:2 "
                        f"ratio"
                    )

        elif isinstance(constraint, NegativeKropkiConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            if value_a is None or value_b is None:
                errors.append(
                    f"Negative Kropki pair is incomplete: "
                    f"{label_a} and {label_b}"
                )

            elif (
                abs(value_a - value_b) == 1
                or value_a == 2 * value_b
                or value_b == 2 * value_a
            ):
                errors.append(
                    f"Negative Kropki violation: the "
                    f"undotted pair {label_a} and {label_b} "
                    f"must not be consecutive or in a 1:2 "
                    f"ratio"
                )

        elif isinstance(constraint, InequalityConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            if value_a is None or value_b is None:
                errors.append(
                    f"Inequality is incomplete: "
                    f"{label_a} and {label_b}"
                )

            else:
                operator = constraint.operator

                satisfied = (
                    value_a < value_b
                    if operator == "<"
                    else value_a > value_b
                )

                if not satisfied:
                    errors.append(
                        f"Inequality violation: {label_a} "
                        f"must be {operator} {label_b}"
                    )

        elif isinstance(constraint, XVConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            expected = 5 if constraint.marker == "V" else 10

            if value_a is None or value_b is None:
                errors.append(
                    f"XV marker is incomplete: "
                    f"{label_a} and {label_b}"
                )

            elif value_a + value_b != expected:
                errors.append(
                    f"XV violation: {constraint.marker} "
                    f"marker requires {label_a} and "
                    f"{label_b} to sum to {expected}"
                )

        elif isinstance(constraint, NegativeXVConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            if value_a is None or value_b is None:
                errors.append(
                    f"Negative XV pair is incomplete: "
                    f"{label_a} and {label_b}"
                )

            elif value_a + value_b in (5, 10):
                errors.append(
                    f"Negative XV violation: the unmarked "
                    f"pair {label_a} and {label_b} must "
                    f"sum to neither 5 nor 10"
                )

        elif isinstance(constraint, ParityConstraint):
            cell = constraint.variables[0]

            value = solution.get(cell)

            label = f"R{cell[0] + 1}C{cell[1] + 1}"

            if value is None:
                errors.append(
                    f"Parity cell is incomplete: {label}"
                )

            else:
                is_odd = value % 2 == 1

                if constraint.parity == "odd" and not is_odd:
                    errors.append(
                        f"Parity violation: {label} must "
                        f"contain an odd digit"
                    )

                elif constraint.parity == "even" and is_odd:
                    errors.append(
                        f"Parity violation: {label} must "
                        f"contain an even digit"
                    )

        elif isinstance(constraint, BetweenLineConstraint):
            cells = constraint.variables

            values = [solution.get(cell) for cell in cells]

            if any(value is None for value in values):
                errors.append(
                    f"Between Line is incomplete: {cells}"
                )

            else:
                low, high = sorted((values[0], values[-1]))

                for cell, value in zip(
                    cells[1:-1], values[1:-1]
                ):
                    if not low < value < high:
                        errors.append(
                            f"Between Line violation: "
                            f"R{cell[0] + 1}C{cell[1] + 1} "
                            f"= {value} is not strictly "
                            f"between {low} and {high}"
                        )

        elif isinstance(constraint, LittleKillerConstraint):
            cells = constraint.variables

            values = [solution.get(cell) for cell in cells]

            if any(value is None for value in values):
                errors.append(
                    f"Little Killer is incomplete: {cells}"
                )

            else:
                total = sum(values)

                if total != constraint.target_sum:
                    errors.append(
                        f"Little Killer violation: diagonal "
                        f"{cells} sums to {total}, expected "
                        f"{constraint.target_sum}"
                    )
        
    return errors