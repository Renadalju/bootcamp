from __future__ import annotations

import json
from pathlib import Path


def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )



def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    cols = report.get("columns", [])
    missing = report.get("missing", {})
    non_empty = report.get("non_empty", {})
    dtype = report.get("dtype", {})
    stats = report.get("stats", {})

    lines: list[str] = []
    lines.append("# CSV Profiling Report\n")
    lines.append(f"- Rows: **{report.get('rows', 0)}**")
    lines.append(f"- Columns: **{report.get('n_cols', 0)}**\n")

    # Missing values
    lines.append("## Missing values\n")
    lines.append("| column | missing |")
    lines.append("|--------|--------:|")
    for c in cols:
        lines.append(f"| {c} | {missing.get(c, 0)} |")

    # Non-empty counts
    lines.append("\n## Non-empty counts\n")
    lines.append("| column | non-empty |")
    lines.append("|--------|-----------:|")
    for c in cols:
        lines.append(f"| {c} | {non_empty.get(c, report.get('rows', 0) - missing.get(c, 0))} |")

    # Data Types
    lines.append("\n## Column Data Types\n")
    lines.append("| column | type |")
    lines.append("|--------|------|")
    for c in cols:
        lines.append(f"| {c} | {dtype.get(c, 'unknown')} |")

    # Statistics
    lines.append("\n## Column Statistics\n")
    for c in cols:
        s = stats.get(c, {})
        lines.append(f"### {c} ({dtype.get(c)})")
        if dtype.get(c) == "numeric":
            lines.append(f"- count: {s.get('count')}, unique: {s.get('unique')}, missing: {s.get('missing')}")
            lines.append(f"- min: {s.get('min')}, max: {s.get('max')}, mean: {s.get('mean')}, median: {s.get('median')}")
        else:
            lines.append(f"- count: {s.get('count')}, unique: {s.get('unique')}, missing: {s.get('missing')}")
            top_values = s.get("top_values", [])
            if top_values:
                top_str = ", ".join(f"{v['value']} ({v['count']})" for v in top_values)
                lines.append(f"- top values: {top_str}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


