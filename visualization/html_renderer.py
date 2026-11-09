from html import escape
from pathlib import Path
import json
import math
import webbrowser

from sudoku.constraints import (
    AllDifferentConstraint,
    KillerCageConstraint,
    ThermometerConstraint,
    NotEqualConstraint,
    NonConsecutiveConstraint,
    GermanWhispersConstraint,
    RenbanConstraint,
    PalindromeConstraint,
    ArrowConstraint
)


# Icon and label for every supported variant, used by
# both the variant badges and the Constraint Inspector.
# Add new variants here to style them everywhere.
VARIANT_STYLES = {
    "thermometer": ("🌡️", "Thermometer"),
    "killer": ("∑", "Killer Cage"),
    "diagonal": ("╳", "Diagonal"),
    "anti-knight": ("♞", "Anti-Knight"),
    "anti-king": ("♚", "Anti-King"),
    "nonconsecutive": ("↔", "Nonconsecutive"),
    "whispers": ("≋", "German Whispers"),
    "renban": ("≡", "Renban"),
    "palindrome": ("⇄", "Palindrome"),
    "arrow": ("➤", "Arrow"),
}


def variant_title(kind):
    """Return the icon-prefixed display name of a variant."""
    icon, label = VARIANT_STYLES[kind]
    return f"{icon} {label}"


def render_puzzle(
    puzzle,
    title="Sudoku Puzzle",
    output="puzzle.html",
    solution=None
):
    """
    Render a standalone interactive Sudoku inspector.

    Supports:
    - Standard Sudoku and given digits
    - Killer cages
    - Thermometers
    - Diagonal AllDifferent constraints
    - Puzzle/solution toggle
    - Clickable cells and constraint inspection

    Does not run the solver.
    """
    cell_size = 60
    grid_size = 9 * cell_size
    elements = []

    def center(cell):
        r, c = cell
        return (
            c * cell_size + cell_size / 2,
            r * cell_size + cell_size / 2
        )

    def cell_label(cell):
        r, c = cell
        return f"R{r + 1}C{c + 1}"

    main_diagonal = {(i, i) for i in range(9)}
    anti_diagonal = {(i, 8 - i) for i in range(9)}
    
    def identify_standard_constraint(cells):
        cell_set = set(cells)

        if len(cell_set) != 9:
            return None

        # Check rows
        for r in range(9):
            if cell_set == {(r, c) for c in range(9)}:
                return f"Row {r + 1}"

        # Check columns
        for c in range(9):
            if cell_set == {(r, c) for r in range(9)}:
                return f"Column {c + 1}"

        # Check 3x3 boxes
        for box_r in range(3):
            for box_c in range(3):
                box_cells = {
                    (r, c)
                    for r in range(box_r * 3, box_r * 3 + 3)
                    for c in range(box_c * 3, box_c * 3 + 3)
                }

                if cell_set == box_cells:
                    box_number = box_r * 3 + box_c + 1
                    return f"Box {box_number}"

        return None

    # Serialize every constraint for the inspector.
    inspector_constraints = []
    cages = []
    thermometers = []
    whisper_lines = []
    renban_lines = []
    palindrome_lines = []
    arrows = []
    diagonal_cells = set()
    anti_knight_neighbors = {
        (r, c): set()
        for r in range(9)
        for c in range(9)
    }
    has_anti_knight = False
    
    anti_king_neighbors = {
        (r, c): set()
        for r in range(9)
        for c in range(9)
    }

    has_anti_king = False
    
    nonconsecutive_neighbors = {
        (r, c): set()
        for r in range(9)
        for c in range(9)
    }

    has_nonconsecutive = False

    for constraint in puzzle.constraints:
        cells = list(constraint.variables)
        cell_set = set(cells)
        details = None
        
        if isinstance(constraint, NotEqualConstraint):
            a, b = constraint.variables

            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            if (dr, dc) in ((1, 2), (2, 1)):
                has_anti_knight = True

                anti_knight_neighbors[a].add(b)
                anti_knight_neighbors[b].add(a)

            elif (dr, dc) == (1, 1):
                has_anti_king = True

                anti_king_neighbors[a].add(b)
                anti_king_neighbors[b].add(a)

            continue
        
        if isinstance(constraint, NonConsecutiveConstraint):
            a, b = constraint.variables

            has_nonconsecutive = True

            nonconsecutive_neighbors[a].add(b)
            nonconsecutive_neighbors[b].add(a)

            continue

        if isinstance(constraint, KillerCageConstraint):
            kind = "killer"
            label = (
                f"{variant_title(kind)} — "
                f"sum {constraint.target_sum}"
            )
            cages.append(constraint)

        elif isinstance(constraint, ThermometerConstraint):
            kind = "thermometer"
            label = (
                f"{variant_title(kind)} — "
                f"{cell_label(cells[0])} to "
                f"{cell_label(cells[-1])}"
            )
            thermometers.append(constraint)

        elif isinstance(constraint, GermanWhispersConstraint):
            kind = "whispers"
            label = (
                f"{variant_title(kind)} — "
                f"{cell_label(cells[0])} to "
                f"{cell_label(cells[-1])}"
            )
            whisper_lines.append(constraint)

        elif isinstance(constraint, RenbanConstraint):
            kind = "renban"
            label = (
                f"{variant_title(kind)} — "
                f"{cell_label(cells[0])} to "
                f"{cell_label(cells[-1])}"
            )
            renban_lines.append(constraint)

        elif isinstance(constraint, PalindromeConstraint):
            kind = "palindrome"
            label = (
                f"{variant_title(kind)} — "
                f"{cell_label(cells[0])} to "
                f"{cell_label(cells[-1])}"
            )
            palindrome_lines.append(constraint)

        elif isinstance(constraint, ArrowConstraint):
            kind = "arrow"
            label = (
                f"{variant_title(kind)} — circle "
                f"{cell_label(constraint.circle_cells[0])}"
            )
            details = (
                "Circle: "
                + ", ".join(
                    cell_label(c)
                    for c in constraint.circle_cells
                )
                + " — Shaft: "
                + ", ".join(
                    cell_label(c)
                    for c in constraint.arrow_cells
                )
            )
            arrows.append(constraint)

        elif (
            isinstance(constraint, AllDifferentConstraint)
            and cell_set == main_diagonal
        ):
            kind = "diagonal"
            label = f"{variant_title(kind)} — Main diagonal"
            diagonal_cells.update(cells)

        elif (
            isinstance(constraint, AllDifferentConstraint)
            and cell_set == anti_diagonal
        ):
            kind = "diagonal"
            label = f"{variant_title(kind)} — Anti-diagonal"
            diagonal_cells.update(cells)

        elif isinstance(constraint, AllDifferentConstraint):
            kind = "all-different"
            label = (
                identify_standard_constraint(cells)
                or "All-different"
            )

        else:
            kind = "other"
            label = type(constraint).__name__

        inspector_constraints.append({
            "id": len(inspector_constraints),
            "kind": kind,
            "label": label,
            "cells": [
                [r, c] for r, c in cells
            ],
            "details": details or (
                f"Cells: {', '.join(cell_label(c) for c in cells)}"
            )
        })

    # Layer 1: Not Equal AND Nonconsecutive constraints (grouped by cell)
    if has_anti_knight:
        for cell, neighbors in anti_knight_neighbors.items():
            if not neighbors:
                continue

            ordered_neighbors = sorted(neighbors)

            inspector_constraints.append({
                "id": len(inspector_constraints),
                "kind": "anti-knight",
                "label": variant_title("anti-knight"),
                "cells": [
                    list(cell),
                    *[list(n) for n in ordered_neighbors],
                ],
                "owner": list(cell),
                "details": (
                    "Cannot share a digit with: "
                    + ", ".join(
                        cell_label(n)
                        for n in ordered_neighbors
                    )
                ),
            })
    
    if has_anti_king:
        for cell in anti_king_neighbors:
            r, c = cell

            # All eight possible king moves,
            # including orthogonal directions.
            king_offsets = [
                (-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1),
            ]

            neighbors = []

            for dr, dc in king_offsets:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < 9 and 0 <= nc < 9:
                    neighbors.append((nr, nc))

            ordered_neighbors = sorted(neighbors)

            inspector_constraints.append({
                "id": len(inspector_constraints),
                "kind": "anti-king",
                "label": variant_title("anti-king"),
                "owner": list(cell),
                "cells": [
                    list(cell),
                    *[list(n) for n in ordered_neighbors],
                ],
                "details": (
                    "Cannot share a digit with any "
                    "orthogonally or diagonally adjacent cell. "
                    "Affected cells: "
                    + ", ".join(
                        cell_label(n)
                        for n in ordered_neighbors
                    )
                ),
            })
    
    if has_nonconsecutive:
        for cell, neighbors in nonconsecutive_neighbors.items():
            if not neighbors:
                continue

            ordered_neighbors = sorted(neighbors)

            inspector_constraints.append({
                "id": len(inspector_constraints),
                "kind": "nonconsecutive",
                "label": variant_title("nonconsecutive"),
                "owner": list(cell),
                "cells": [
                    list(cell),
                    *[list(n) for n in ordered_neighbors],
                ],
                "details": (
                    "Orthogonally adjacent cells cannot "
                    "contain consecutive digits. "
                    "Affected cells: "
                    + ", ".join(
                        cell_label(n)
                        for n in ordered_neighbors
                    )
                ),
            })  
            
    # Layer 2: Background
    elements.append(
        f'<rect width="{grid_size}" height="{grid_size}" '
        'fill="white"/>'
    )

    # Layer 3: Diagonal highlighting
    for r, c in sorted(diagonal_cells):
        elements.append(
            f'<rect class="diagonal-layer" '
            f'x="{c * cell_size}" '
            f'y="{r * cell_size}" '
            f'width="{cell_size}" '
            f'height="{cell_size}" '
            'fill="#dbeafe"/>'
        )
    
    # Layer 4: Constraint selection highlights
    for r in range(9):
        for c in range(9):
            elements.append(
                f'<rect id="highlight-{r}-{c}" '
                f'x="{c * cell_size}" '
                f'y="{r * cell_size}" '
                f'width="{cell_size}" '
                f'height="{cell_size}" '
                'fill="#DBEAFE" '
                'fill-opacity="0.75" '
                'stroke="none" '
                'visibility="hidden" '
                'pointer-events="none"/>'
            )

    # Layer 5: Thermometers
    for thermometer in thermometers:
        cells = list(thermometer.variables)

        if not cells:
            continue

        points = [center(cell) for cell in cells]

        if len(points) > 1:
            path = " ".join(
                f"{x},{y}" for x, y in points
            )

            elements.append(
                f'<polyline class="thermometer-layer" '
                f'points="{path}" fill="none" '
                'stroke="#b8bec8" stroke-width="17" '
                'stroke-linecap="round" '
                'stroke-linejoin="round"/>'
            )

        x, y = points[0]

        elements.append(
            f'<circle class="thermometer-layer" '
            f'cx="{x}" cy="{y}" r="17" '
            'fill="#b8bec8"/>'
        )

    # Layer 5b: German Whispers lines
    for line in whisper_lines:
        cells = list(line.variables)

        points = [center(cell) for cell in cells]

        path = " ".join(
            f"{x},{y}" for x, y in points
        )

        elements.append(
            f'<polyline class="whispers-layer" '
            f'points="{path}" fill="none" '
            'stroke="#16a34a" stroke-width="12" '
            'stroke-opacity="0.65" '
            'stroke-linecap="round" '
            'stroke-linejoin="round"/>'
        )

    # Layer 5c: Renban lines
    for line in renban_lines:
        cells = list(line.variables)

        points = [center(cell) for cell in cells]

        path = " ".join(
            f"{x},{y}" for x, y in points
        )

        elements.append(
            f'<polyline class="renban-layer" '
            f'points="{path}" fill="none" '
            'stroke="#9333ea" stroke-width="12" '
            'stroke-opacity="0.65" '
            'stroke-linecap="round" '
            'stroke-linejoin="round"/>'
        )

    # Layer 5d: Palindrome lines
    for line in palindrome_lines:
        cells = list(line.variables)

        points = [center(cell) for cell in cells]

        path = " ".join(
            f"{x},{y}" for x, y in points
        )

        elements.append(
            f'<polyline class="palindrome-layer" '
            f'points="{path}" fill="none" '
            'stroke="#ec4899" stroke-width="12" '
            'stroke-opacity="0.65" '
            'stroke-linecap="round" '
            'stroke-linejoin="round"/>'
        )

    # Layer 5e: Arrows
    for arrow_constraint in arrows:
        circle_cells = list(arrow_constraint.circle_cells)
        shaft_cells = list(arrow_constraint.arrow_cells)

        circle_points = [center(cell) for cell in circle_cells]
        shaft_points = [center(cell) for cell in shaft_cells]

        # Shaft: starts at the nearest circle cell center so
        # the circle visually caps the line.
        start = circle_points[-1]
        line_points = [start] + shaft_points

        path = " ".join(
            f"{x},{y}" for x, y in line_points
        )

        elements.append(
            f'<polyline class="arrow-layer" '
            f'points="{path}" fill="none" '
            'stroke="#06b6d4" stroke-width="3.5" '
            'stroke-linecap="round" '
            'stroke-linejoin="round"/>'
        )

        # Arrowhead at the final shaft cell.
        tip_x, tip_y = line_points[-1]
        prev_x, prev_y = line_points[-2]

        angle = math.atan2(tip_y - prev_y, tip_x - prev_x)
        head_length = 14
        spread = math.radians(150)

        wings = [
            (
                tip_x + head_length * math.cos(angle + sign * spread),
                tip_y + head_length * math.sin(angle + sign * spread),
            )
            for sign in (1, -1)
        ]

        elements.append(
            f'<polyline class="arrow-layer" '
            f'points="{wings[0][0]:.1f},{wings[0][1]:.1f} '
            f'{tip_x},{tip_y} '
            f'{wings[1][0]:.1f},{wings[1][1]:.1f}" '
            'fill="none" stroke="#06b6d4" '
            'stroke-width="3.5" '
            'stroke-linecap="round" '
            'stroke-linejoin="round"/>'
        )

        # Circle: a ring for one cell, a pill for several.
        if len(circle_points) == 1:
            x, y = circle_points[0]

            elements.append(
                f'<circle class="arrow-layer" '
                f'cx="{x}" cy="{y}" r="21" '
                'fill="white" '
                'stroke="#06b6d4" stroke-width="3"/>'
            )

        else:
            pill = " ".join(
                f"{x},{y}" for x, y in circle_points
            )

            elements.append(
                f'<polyline class="arrow-layer" '
                f'points="{pill}" fill="none" '
                'stroke="#06b6d4" stroke-width="45" '
                'stroke-linecap="round" '
                'stroke-linejoin="round"/>'
            )

            elements.append(
                f'<polyline class="arrow-layer" '
                f'points="{pill}" fill="none" '
                'stroke="white" '
                'stroke-width="39" '
                'stroke-linecap="round" '
                'stroke-linejoin="round"/>'
            )

    # Layer 6: Killer cages
    inset = 5

    for cage in cages:
        cells = set(cage.variables)

        for r, c in cells:
            x = c * cell_size
            y = r * cell_size

            edges = [
                (
                    (r - 1, c),
                    (x + inset, y + inset),
                    (x + cell_size - inset, y + inset)
                ),
                (
                    (r + 1, c),
                    (x + inset, y + cell_size - inset),
                    (x + cell_size - inset,
                     y + cell_size - inset)
                ),
                (
                    (r, c - 1),
                    (x + inset, y + inset),
                    (x + inset, y + cell_size - inset)
                ),
                (
                    (r, c + 1),
                    (x + cell_size - inset, y + inset),
                    (x + cell_size - inset,
                     y + cell_size - inset)
                ),
            ]

            for neighbor, start, end in edges:
                if neighbor not in cells:
                    elements.append(
                        f'<line class="killer-layer" '
                        f'x1="{start[0]}" y1="{start[1]}" '
                        f'x2="{end[0]}" y2="{end[1]}" '
                        'stroke="#334155" stroke-width="1.5" '
                        'stroke-dasharray="5 3"/>'
                    )

        r, c = min(cells)

        elements.append(
            f'<text class="killer-layer" '
            f'x="{c * cell_size + 9}" '
            f'y="{r * cell_size + 19}" '
            'font-size="14" font-weight="600" '
            f'fill="#1d4ed8">{cage.target_sum}</text>'
        )

    # Layer 7: Grid lines
    for i in range(10):
        pos = i * cell_size
        width = 3 if i % 3 == 0 else 0.8

        elements.append(
            f'<line x1="{pos}" y1="0" '
            f'x2="{pos}" y2="{grid_size}" '
            f'stroke="#111827" stroke-width="{width}"/>'
        )

        elements.append(
            f'<line x1="0" y1="{pos}" '
            f'x2="{grid_size}" y2="{pos}" '
            f'stroke="#111827" stroke-width="{width}"/>'
        )
    
    # Layer 8: Digits
    for r in range(9):
        for c in range(9):
            x, y = center((r, c))

            elements.append(
                f'<text id="cell-{r}-{c}" '
                f'x="{x}" y="{y + 9}" '
                'text-anchor="middle" '
                'font-size="28" font-weight="600" '
                'fill="#172033"></text>'
            )

    # Layer 9: Selected cell outline
    elements.append(
            '<rect id="selected-cell" '
            'x="0" y="0" '
            f'width="{cell_size - 6}" '
            f'height="{cell_size - 6}" '
            'fill="none" '
            'stroke="#2563EB" '
            'stroke-width="4" '
            'rx="3" '
            'visibility="hidden" '
            'pointer-events="none"/>'
        )
        
    # Layer 10: Transparent clickable cell overlays
    for r in range(9):
        for c in range(9):
            elements.append(
                f'<rect class="cell-hitbox" '
                f'x="{c * cell_size}" '
                f'y="{r * cell_size}" '
                f'width="{cell_size}" '
                f'height="{cell_size}" '
                f'onclick="selectCell({r}, {c})" '
                'fill="transparent"/>'
            )

    svg = "\n".join(elements)

    givens_json = json.dumps(puzzle.grid)
    solution_json = json.dumps(solution)
    constraints_json = json.dumps(inspector_constraints)
    
    active_variants = {
        "thermometer": bool(thermometers),
        "killer": bool(cages),
        "diagonal": bool(diagonal_cells),
        "anti-knight": has_anti_knight,
        "anti-king": has_anti_king,
        "nonconsecutive": has_nonconsecutive,
        "whispers": bool(whisper_lines),
        "renban": bool(renban_lines),
        "palindrome": bool(palindrome_lines),
        "arrow": bool(arrows),
    }

    variant_badges = [
        '<span class="variant-badge">'
        f'{variant_title(kind)}'
        '</span>'
        for kind in VARIANT_STYLES
        if active_variants[kind]
    ]

    variant_badges_html = "\n".join(variant_badges)

    has_solution = solution is not None

    toggle_button = (
        '<button id="solution-toggle" '
        'onclick="toggleSolution()">Show solution</button>'
        if has_solution else ""
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>

<style>
    * {{
        box-sizing: border-box;
    }}

    body {{
        font-family: Arial, sans-serif;
        background: #f1f5f9;
        margin: 0;
        padding: 28px 20px;
        color: #172033;
    }}

    header {{
        text-align: center;
        margin-bottom: 24px;
    }}

    h1 {{
        margin-bottom: 8px;
    }}

    header p {{
        color: #64748b;
    }}

    .layout {{
        display: grid;
        grid-template-columns: minmax(0, 580px) minmax(280px, 360px);
        gap: 24px;
        justify-content: center;
        align-items: start;
    }}

    .panel {{
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 20px #00000012;
    }}

    svg {{
        display: block;
        width: 100%;
        height: auto;
    }}

    .controls {{
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 18px;
        align-items: center;
    }}

    button {{
        background: #2563eb;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 14px;
        cursor: pointer;
    }}

    button:hover {{
        background: #1d4ed8;
    }}

    .inspector h2 {{
        margin-top: 0;
    }}

    .inspector p {{
        color: #64748b;
        line-height: 1.5;
    }}

    .constraint-item {{
        display: block;
        width: 100%;
        text-align: left;
        background: #f1f5f9;
        color: #172033;
        margin: 8px 0;
        padding: 10px 12px;
        border-radius: 8px;
        border: 1px solid #cbd5e1;
    }}

    .constraint-item:hover {{
        background: #DBEAFE;
    }}

    .constraint-item.active {{
        background: #DBEAFE;
        border-color: #2563EB;
        color: #1E40AF;
    }}

    .details {{
        font-size: 13px;
        color: #64748b;
        margin-top: 5px;
        overflow-wrap: anywhere;
    }}

    .cell-hitbox {{
        cursor: pointer;
        pointer-events: all;
    }}

    .diagonal-layer,
    .thermometer-layer,
    .whispers-layer,
    .renban-layer,
    .palindrome-layer,
    .arrow-layer,
    .killer-layer {{
        pointer-events: none;
    }}

    label {{
        font-size: 14px;
        cursor: pointer;
    }}

    @media (max-width: 850px) {{
        .layout {{
            grid-template-columns: minmax(0, 580px);
        }}
    }}
    
        .variant-badges {{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }}

    .variant-badge {{
        display: inline-block;
        background: #dbeafe;
        color: #1e40af;
        padding: 7px 12px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
    }}
</style>
</head>

<body>
<header>
    <h1>{escape(title)}</h1>
    <p id="mode-label">Unsolved puzzle</p>

    <div class="variant-badges">
        {variant_badges_html}
    </div>
</header>

<div class="layout">
    <div class="panel">
        <svg viewBox="0 0 540 540"
             xmlns="http://www.w3.org/2000/svg">
            {svg}
        </svg>

        <div class="controls">
            {toggle_button}

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('diagonal', this.checked)">
                Diagonals
            </label>

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('thermometer', this.checked)">
                Thermometers
            </label>

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('whispers', this.checked)">
                German Whispers
            </label>

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('renban', this.checked)">
                Renban
            </label>

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('palindrome', this.checked)">
                Palindrome
            </label>

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('arrow', this.checked)">
                Arrows
            </label>

            <label>
                <input type="checkbox" checked
                       onchange="toggleLayer('killer', this.checked)">
                Killer cages
            </label>
        </div>
    </div>

    <div class="panel inspector">
        <h2>Constraint Inspector</h2>
        <p>Click a cell to inspect its constraints.</p>

        <div id="selection-info">
            No cell selected.
        </div>

        <div id="constraint-list"></div>
    </div>
</div>

<script>
const givens = {givens_json};
const solution = {solution_json};
const constraints = {constraints_json};

let showingSolution = false;
let selectedConstraint = null;
let selectedCell = null;

function drawDigits(grid) {{
    for (let r = 0; r < 9; r++) {{
        for (let c = 0; c < 9; c++) {{
            const element = document.getElementById(
                `cell-${{r}}-${{c}}`
            );

            element.textContent = grid[r][c] || "";

            element.setAttribute(
                "fill",
                givens[r][c] ? "#172033" : "#2563eb"
            );
        }}
    }}
}}

function toggleSolution() {{
    if (!solution) return;

    showingSolution = !showingSolution;

    drawDigits(showingSolution ? solution : givens);

    document.getElementById("solution-toggle").textContent =
        showingSolution ? "Show puzzle" : "Show solution";

    document.getElementById("mode-label").textContent =
        showingSolution ? "Solved puzzle" : "Unsolved puzzle";
}}

function toggleLayer(kind, visible) {{
    document.querySelectorAll(
        `.${{kind}}-layer`
    ).forEach(element => {{
        element.style.display = visible ? "" : "none";
    }});
}}

function clearHighlights() {{
    for (let r = 0; r < 9; r++) {{
        for (let c = 0; c < 9; c++) {{
            document.getElementById(
                `highlight-${{r}}-${{c}}`
            ).setAttribute("visibility", "hidden");
        }}
    }}
}}

function highlightConstraint(constraintId) {{
    clearHighlights();

    const constraint = constraints.find(
        item => item.id === constraintId
    );

    if (!constraint) return;

    selectedConstraint = constraintId;

    for (const [r, c] of constraint.cells) {{
        document.getElementById(
            `highlight-${{r}}-${{c}}`
        ).setAttribute("visibility", "visible");
    }}

    document.querySelectorAll(
        ".constraint-item"
    ).forEach(button => {{
        button.classList.toggle(
            "active",
            Number(button.dataset.id) === constraintId
        );
    }});
}}

function selectCell(r, c) {{
    clearHighlights();
    selectedConstraint = null;
    selectedCell = [r, c];

    const outline = document.getElementById("selected-cell");

    outline.setAttribute("x", c * 60 + 3);
    outline.setAttribute("y", r * 60 + 3);
    outline.setAttribute("visibility", "visible");

    const label = `R${{r + 1}}C${{c + 1}}`;
    const given = givens[r][c];

    document.getElementById("selection-info").innerHTML =
        `<strong>${{label}}</strong> — ` +
        (given ? `Given: ${{given}}` : "No given digit");

        const matching = constraints.filter(constraint => {{
            if (
                constraint.kind === "anti-knight" ||
                constraint.kind === "anti-king" ||
                constraint.kind === "nonconsecutive"
            ) {{
                return (
                    constraint.owner[0] === r &&
                    constraint.owner[1] === c
                );
            }}

            return constraint.cells.some(
                cell => cell[0] === r && cell[1] === c
            );
        }});

    const list = document.getElementById("constraint-list");
    list.innerHTML = "";

    if (!matching.length) {{
        list.textContent = "No constraints found.";
        return;
    }}

    for (const constraint of matching) {{
        const button = document.createElement("button");
        button.className = "constraint-item";
        button.dataset.id = constraint.id;

        const heading = document.createElement("strong");
        heading.textContent = constraint.label;

        const details = document.createElement("div");
        details.className = "details";
        details.textContent = constraint.details;

        button.append(heading, details);
        button.onclick = () => highlightConstraint(constraint.id);

        list.appendChild(button);
    }}
}}

drawDigits(givens);
</script>
</body>
</html>
"""

    path = Path(output).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")

    return path


def show_puzzle(
    puzzle,
    title="Sudoku Puzzle",
    output="puzzle.html",
    solution=None
):
    """Generate HTML and open it in the browser."""
    path = render_puzzle(
        puzzle,
        title=title,
        output=output,
        solution=solution
    )

    webbrowser.open(path.as_uri())
    return path
