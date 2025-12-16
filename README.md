# CSV Profiler

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)

## Overview

**CSV Profiler** is a Python tool designed to quickly analyze CSV files and generate detailed column-level statistics.
It produces **JSON** and **Markdown** reports containing essential information such as missing values, unique counts, numeric statistics (e.g., min, max, mean, median), and top values for text columns.

---

## Features

* **Reads CSV files** and generates detailed column profiles.
* Computes **numeric statistics** for numeric columns:

  * `count`, `missing`, `unique`, `min`, `max`, `mean`, `median`.
* Computes **text statistics** for text/categorical columns:

  * `count`, `missing`, `unique`, `top values`.
* **Automatic column type detection** (`numeric` or `text`).
* Calculates **missing value percentages** per column.
* Generates reports in two formats:

  * **JSON**: for programmatic use or further analysis.
  * **Markdown**: for easy viewing and sharing.
* **CLI interface** using Typer to pass CSV files and generate reports.
* **Prevents overwriting** of existing reports or allows creating timestamped files.

---

## Project Structure

```
bootcamp/
├─ src/
│  └─ csv_profiler/
│     ├─ __init__.py
│     ├─ io.py
│     ├─ profile.py
│     ├─ render.py
│     ├─ typertest.py
├─ data/
│  └─ sample.csv
├─ outputs/
├─ requirements.txt
├─ README.md
└─ pyproject.toml
```

---

## Installation

### Step 1: Set up a virtual environment
```
uv venv -p 3.11
```

Activate On Windows (PowerShell):

```powershell
.venv\Scripts\activate
```

Activate On Linux / Mac:

```bash
. .venv/bin/activate
```

### Step 2: Install the dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
typer==0.9.0
click==8.1.3
```

---

## Usage(CLI)
use this command:

```bash 
uv run python -m src.csv_profiler.typertest data/sample.csv
```
