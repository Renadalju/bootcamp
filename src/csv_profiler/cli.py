from pathlib import Path
import typer
import sys
from .io import read_csv_rows
from .profile import basic_profile
from .render import write_json, write_markdown


# Allow imports from src/
sys.path.append(str(Path(__file__).resolve().parent / "src"))
app = typer.Typer(help="CSV Profiler CLI")

@app.command()
def run(
    csv_path: Path = typer.Argument(..., help="Path to CSV file"),
    out_dir: Path = typer.Option(
        Path("outputs"),
        "--out",
        "-o",
        help="Output directory for reports"
    ),
):
    rows = read_csv_rows(csv_path)
    report = basic_profile(rows)

    out_dir.mkdir(parents=True, exist_ok=True)

    write_json(report, out_dir / "report.json")
    write_markdown(report, out_dir / "report.md")

    typer.echo(f"Reports written to {out_dir}")

if __name__ == "__main__":
    app()