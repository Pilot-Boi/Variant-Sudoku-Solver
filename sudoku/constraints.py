from csp.constraint import Constraint
from itertools import combinations
from functools import lru_cache

class AllDifferentConstraint(Constraint):
    
    def __init__(
        self,
        variables,
        required_values=None,
        max_subset_size=4
    ):
        super().__init__(variables)

        if required_values is not None:
            required_values = set(required_values)

            if len(required_values) != len(self.variables):
                raise ValueError(
                    "Required values must match variable count."
                )

        if not isinstance(max_subset_size, int) or max_subset_size < 1:
            raise ValueError(
                "max_subset_size must be a positive integer"
            )

        self.required_values = required_values
        self.max_subset_size = max_subset_size

    def is_satisfied(self, assignment):
        values = [
            assignment[var]
            for var in self.variables
            if var in assignment
        ]

        if len(values) != len(set(values)):
            return False

        if self.required_values is not None:
            return all(
                value in self.required_values
                for value in values
            )

        return True
    
    def _propagate_naked_subsets(self, domains):
        """
        Detect naked subsets up to max_subset_size.

        Optimizations:
        - Filter candidates by domain size.
        - Stop building unions that exceed subset size.
        - Apply all eliminations from a discovered subset.
        - Restart after changes to avoid stale combinations.
        """
        max_size = min(
            self.max_subset_size,
            len(self.variables) - 1
        )

        changed = False

        while True:
            found_change = False

            for size in range(2, max_size + 1):

                candidates = [
                    var
                    for var in self.variables
                    if 1 < len(domains[var]) <= size
                ]

                if len(candidates) < size:
                    continue

                for group in combinations(candidates, size):
                    union = set()

                    for var in group:
                        union.update(domains[var])

                        if len(union) > size:
                            break

                    if len(union) != size:
                        continue

                    group_set = set(group)

                    # Calculate reductions before applying them.
                    reductions = {}

                    for var in self.variables:
                        if var in group_set:
                            continue

                        reduced = domains[var] - union

                        if not reduced:
                            raise ValueError(
                                "Naked subset caused contradiction"
                            )

                        if reduced != domains[var]:
                            reductions[var] = reduced

                    if reductions:
                        domains.update(reductions)

                        changed = True
                        found_change = True

                        # Restart using the updated domains.
                        break

                if found_change:
                    break

            if not found_change:
                return changed

    def propagate(self, domains):
        changed = False

        # Step 1: Enforce required values, if provided.
        if self.required_values is not None:
            for var in self.variables:
                allowed = domains[var] & self.required_values

                if not allowed:
                    raise ValueError("No valid candidates")

                if allowed != domains[var]:
                    domains[var] = allowed
                    changed = True

        # Step 2: Naked singles.
        singletons = [
            next(iter(domains[var]))
            for var in self.variables
            if len(domains[var]) == 1
        ]

        if len(singletons) != len(set(singletons)):
            raise ValueError("AllDifferent contradiction")

        forced_values = set(singletons)

        for var in self.variables:
            if len(domains[var]) == 1:
                continue

            allowed = domains[var] - forced_values

            if not allowed:
                raise ValueError("Empty domain")

            if allowed != domains[var]:
                domains[var] = allowed
                changed = True

        # Step 3: Hidden singles.
        if self.required_values is not None:
            for value in self.required_values:
                possible_cells = [
                    var for var in self.variables
                    if value in domains[var]
                ]

                if not possible_cells:
                    raise ValueError(
                        f"Required value {value} has no location"
                    )

                if len(possible_cells) == 1:
                    var = possible_cells[0]

                    if domains[var] != {value}:
                        domains[var] = {value}
                        changed = True


        # Step 4: Naked subsets.
        if self._propagate_naked_subsets(domains):
            changed = True

        return changed
        
class ThermometerConstraint(Constraint):
    def is_satisfied(self, assignment):
        n = len(self.variables)

        if n > 9:
            return False

        for i, cell in enumerate(self.variables):
            if cell not in assignment:
                continue

            value = assignment[cell]

            min_value = i + 1
            max_value = 9 - (n - 1 - i)

            if not min_value <= value <= max_value:
                return False

            for j in range(i):
                previous = self.variables[j]

                if previous in assignment:
                    if value - assignment[previous] < i - j:
                        return False

        return True

    def propagate(self, domains):
        changed = False
        cells = self.variables
        n = len(cells)

        if n > 9:
            raise ValueError("Thermometer too long")

        # First enforce positional bounds.
        for i, cell in enumerate(cells):
            minimum = i + 1
            maximum = 9 - (n - 1 - i)

            allowed = {
                value for value in domains[cell]
                if minimum <= value <= maximum
            }

            if not allowed:
                raise ValueError("Thermometer contradiction")

            if allowed != domains[cell]:
                domains[cell] = allowed
                changed = True

        # Forward pass: each value must have a
        # smaller supporting value in the prior cell.
        for i in range(1, n):
            previous = cells[i - 1]
            current = cells[i]

            smallest_previous = min(domains[previous])

            allowed = {
                value for value in domains[current]
                if value > smallest_previous
            }

            if not allowed:
                raise ValueError("Thermometer contradiction")

            if allowed != domains[current]:
                domains[current] = allowed
                changed = True

        # Backward pass: each value must have a
        # larger supporting value in the next cell.
        for i in range(n - 2, -1, -1):
            current = cells[i]
            following = cells[i + 1]

            largest_following = max(domains[following])

            allowed = {
                value for value in domains[current]
                if value < largest_following
            }

            if not allowed:
                raise ValueError("Thermometer contradiction")

            if allowed != domains[current]:
                domains[current] = allowed
                changed = True

        return changed

class KillerCageConstraint(Constraint):
    """
    Killer Sudoku cage with cached sum combinations
    and domain-aware propagation.
    """

    @staticmethod
    @lru_cache(maxsize=None)
    def _valid_combinations(size, target_sum):
        """
        Generate all unordered sets of distinct digits
        that satisfy the cage sum.

        Cached across all cages of the same size and sum.
        """
        return tuple(
            combo
            for combo in combinations(range(1, 10), size)
            if sum(combo) == target_sum
        )

    def __init__(self, variables, target_sum):
        super().__init__(variables)

        if not variables:
            raise ValueError("A cage cannot be empty")

        if len(set(variables)) != len(variables):
            raise ValueError("Duplicate cells in cage")

        if not isinstance(target_sum, int):
            raise ValueError("Target sum must be an integer")

        if len(variables) > 9:
            raise ValueError(
                "Killer cages cannot contain more than 9 cells"
            )

        n = len(variables)

        minimum = sum(range(1, n + 1))
        maximum = sum(range(10 - n, 10))

        if not minimum <= target_sum <= maximum:
            raise ValueError(
                "Target sum is impossible for cage size"
            )

        self.target_sum = target_sum
        
        self.full_digit_cage = (
            len(self.variables) == 9
            and target_sum == 45
        )

        self.full_digit_constraint = (
            AllDifferentConstraint(
                self.variables,
                required_values=set(range(1, 10))
            )
            if self.full_digit_cage
            else None
        )

        # Precomputed combinations for this cage.
        self.combinations = self._valid_combinations(
            n, target_sum
        )

        # Cache domain-specific propagation results.
        self._support_cache = {}

    def is_satisfied(self, assignment):
        assigned = [
            assignment[var]
            for var in self.variables
            if var in assignment
        ]

        if len(assigned) != len(set(assigned)):
            return False

        if any(value not in range(1, 10) for value in assigned):
            return False

        if sum(assigned) > self.target_sum:
            return False

        if len(assigned) == len(self.variables):
            return sum(assigned) == self.target_sum

        return True

    def _find_supports(self, domains):
        """
        Find every value that participates in at least
        one valid assignment of this cage.
        """
        supports = {
            var: set()
            for var in self.variables
        }
        
        targets = {
            var: set(domains[var])
            for var in self.variables
        }

        def fully_supported():
            return all(
                supports[var] == targets[var]
                for var in self.variables
            )

        # Examine only combinations compatible with
        # the current domains.
        for combo in self.combinations:
            digits = set(combo)

            # Every cell must be able to use at least
            # one digit from this combination.
            if any(
                not (domains[var] & digits)
                for var in self.variables
            ):
                continue

            # Every digit in the combination must
            # have at least one possible location.
            if any(
                not any(
                    digit in domains[var]
                    for var in self.variables
                )
                for digit in combo
            ):
                continue

            def assign(index, remaining, chosen):
                if fully_supported():
                    return

                if index == len(self.variables):
                    for var, value in chosen.items():
                        supports[var].add(value)
                    return

                var = self.variables[index]

                for value in domains[var] & remaining:
                    chosen[var] = value

                    assign(
                        index + 1,
                        remaining - {value},
                        chosen
                    )

                    del chosen[var]

                    if fully_supported():
                        return

            assign(0, digits, {})
            
            if fully_supported():
                break

        return supports

    def propagate(self, domains):
        """
        Eliminate values that cannot participate in
        any valid cage assignment.
        """
        if self.full_digit_cage:
            return self.full_digit_constraint.propagate(domains)
       
        key = tuple(
            frozenset(domains[var])
            for var in self.variables
        )

        if key in self._support_cache:
            cached = self._support_cache[key]

            if cached is None:
                raise ValueError(
                    "Killer cage has no valid assignments"
                )

            supports = {
                var: set(values)
                for var, values in zip(self.variables, cached)
            }

        else:
            supports = self._find_supports(domains)

            if any(
                not supports[var]
                for var in self.variables
            ):
                self._support_cache[key] = None
                raise ValueError(
                    "Killer cage has no valid assignments"
                )

            self._support_cache[key] = tuple(
                frozenset(supports[var])
                for var in self.variables
            )

        changed = False

        for var in self.variables:
            allowed = domains[var] & supports[var]

            if not allowed:
                raise ValueError(
                    "Killer cage has no valid assignments"
                )

            if allowed != domains[var]:
                domains[var] = allowed
                changed = True

        return changed
    
class NotEqualConstraint(Constraint):
    """
    Binary inequality constraint: A != B.

    Used by Anti-Knight and potentially Anti-King Sudoku.
    """

    def __init__(self, cell_a, cell_b):
        super().__init__((cell_a, cell_b))

        if cell_a == cell_b:
            raise ValueError(
                "NotEqualConstraint requires two distinct cells"
            )

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return assignment[a] != assignment[b]

    def propagate(self, domains):
        a, b = self.variables

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        # If both cells have the same forced value,
        # the constraint cannot be satisfied.
        if (
            len(domain_a) == 1
            and len(domain_b) == 1
            and domain_a == domain_b
        ):
            raise ValueError(
                "NotEqualConstraint contradiction"
            )

        changed = False

        # If A is fixed, remove its value from B.
        if len(domain_a) == 1:
            value = next(iter(domain_a))

            if value in domain_b:
                domains[b] = domain_b - {value}
                changed = True

        # If B is fixed, remove its value from A.
        if len(domain_b) == 1:
            value = next(iter(domain_b))

            if value in domains[a]:
                domains[a] = domains[a] - {value}
                changed = True

        if not domains[a] or not domains[b]:
            raise ValueError(
                "NotEqualConstraint emptied a domain"
            )

        return changed


class NonConsecutiveConstraint(Constraint):
    """
    Two cells cannot contain consecutive digits.

    Valid examples:
        (1, 3), (4, 7), (5, 5)

    Invalid examples:
        (3, 4), (7, 6)
    """

    def __init__(self, cell_a, cell_b):
        super().__init__((cell_a, cell_b))

        if cell_a == cell_b:
            raise ValueError(
                "NonConsecutiveConstraint requires two distinct cells"
            )

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return abs(assignment[a] - assignment[b]) != 1

    def propagate(self, domains):
        a, b = self.variables

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        # Keep only values that have at least one
        # compatible value in the other domain.
        supported_a = {
            x for x in domain_a
            if any(abs(x - y) != 1 for y in domain_b)
        }

        supported_b = {
            y for y in domain_b
            if any(abs(x - y) != 1 for x in domain_a)
        }

        if not supported_a or not supported_b:
            raise ValueError(
                "NonConsecutiveConstraint contradiction"
            )

        changed = (
            supported_a != domain_a
            or supported_b != domain_b
        )

        if changed:
            domains[a] = supported_a
            domains[b] = supported_b

        return changed


def generate_knight_pairs():
    """
    Generate every unique pair of cells connected
    by a chess knight's move on a 9x9 Sudoku grid.
    """
    offsets = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1),
    ]

    pairs = set()

    for r in range(9):
        for c in range(9):
            for dr, dc in offsets:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < 9 and 0 <= nc < 9:
                    a = (r, c)
                    b = (nr, nc)

                    pairs.add(tuple(sorted((a, b))))

    return sorted(pairs)

def generate_king_pairs():
    """
    Return all unique diagonally adjacent cell pairs.

    Horizontal and vertical king moves are already
    covered by standard Sudoku row/column constraints.
    """
    offsets = [
        (-1, -1), (-1, 1),
        (1, -1), (1, 1),
    ]

    pairs = set()

    for r in range(9):
        for c in range(9):
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc

                if 0 <= nr < 9 and 0 <= nc < 9:
                    a = (r, c)
                    b = (nr, nc)

                    pairs.add(tuple(sorted((a, b))))

    return sorted(pairs)

def generate_orthogonal_pairs():
    """
    Return every unique pair of orthogonally
    adjacent cells in a 9x9 Sudoku grid.
    """
    pairs = []

    for r in range(9):
        for c in range(9):

            # Right neighbor
            if c + 1 < 9:
                pairs.append((
                    (r, c),
                    (r, c + 1)
                ))

            # Bottom neighbor
            if r + 1 < 9:
                pairs.append((
                    (r, c),
                    (r + 1, c)
                ))

    return pairs
