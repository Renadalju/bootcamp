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

On Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On Linux / Mac:

```bash
python3 -m venv venv
source venv/bin/activate
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

## Usage

```bash

use this command: 
uv run python -m src.csv_profiler.typertest data/sample.csv
---

## Example Output

### JSON Example

```json
{
  "rows": 4,
  "n_cols": 4,
  "columns": [
    "name",
    " age",
    " city",
    " salary"
  ],
  "missing": {
    "name": 0,
    " age": 1,
    " city": 1,
    " salary": 1
  },
  "non_empty": {
    "name": 4,
    " age": 3,
    " city": 3,
    " salary": 3
  },
  "dtype": {
    "name": "text",
    " age": "numeric",
    " city": "text",
    " salary": "numeric"
  },
  "stats": {
    "name": {
      "count": 4,
      "missing": 0,
      "unique": 4,
      "top_values": [
        {
          "value": "Aisha",
          "count": 1
        },
        {
          "value": "Fahad",
          "count": 1
        },
        {
          "value": "Noor",
          "count": 1
        },
        {
          "value": "Salem",
          "count": 1
        }
      ]
    },
    " age": {
      "count": 3,
      "unique": 3,
      "missing": 1,
      "min": 23.0,
      "max": 31.0,
      "mean": 27.666666666666668,
      "median": 29.0
    },
    " city": {
      "count": 3,
      "missing": 1,
      "unique": 3,
      "top_values": [
        {
          "value": " Riyadh",
          "count": 1
        },
        {
          "value": " Jeddah",
          "count": 1
        },
        {
          "value": " Dammam",
          "count": 1
        }
      ]
    },
    " salary": {
      "count": 3,
      "unique": 3,
      "missing": 1,
      "min": 9000.0,
      "max": 15000.0,
      "mean": 12000.0,
      "median": 12000.0
    }
  }
}

```

### Markdown Example

```markdown
# CSV Profiling Report

- Rows: **4**
- Columns: **4**

## Missing values

| column | missing |
|--------|--------:|
| name | 0 |
|  age | 1 |
|  city | 1 |
|  salary | 1 |

## Non-empty counts

| column | non-empty |
|--------|-----------:|
| name | 4 |
|  age | 3 |
|  city | 3 |
|  salary | 3 |

## Column Data Types

| column | type |
|--------|------|
| name | text |
|  age | numeric |
|  city | text |
|  salary | numeric |

## Column Statistics

### name (text)
- count: 4, unique: 4, missing: 0
- top values: Aisha (1), Fahad (1), Noor (1), Salem (1)
###  age (numeric)
- count: 3, unique: 3, missing: 1
- min: 23.0, max: 31.0, mean: 27.666666666666668, median: 29.0
###  city (text)
- count: 3, unique: 3, missing: 1
- top values:  Riyadh (1),  Jeddah (1),  Dammam (1)
###  salary (numeric)
- count: 3, unique: 3, missing: 1
- min: 9000.0, max: 15000.0, mean: 12000.0, median: 12000.0

```

